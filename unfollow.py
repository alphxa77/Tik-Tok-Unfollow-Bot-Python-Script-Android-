import xml.etree.ElementTree as ET
import subprocess
import os
import time
import sys
import threading

# ──────────────────────────────────────────
#  Keyboard input depending on OS
# ──────────────────────────────────────────
if sys.platform == "win32":
    import msvcrt
    def get_key():
        if msvcrt.kbhit():
            return msvcrt.getch().decode("utf-8", errors="ignore").lower()
        return None
else:
    import tty, termios, select
    def get_key():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            if select.select([sys.stdin], [], [], 0)[0]:
                return sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return None

# ──────────────────────────────────────────
#  Settings
# ──────────────────────────────────────────
node_tag = "node"
followed_btn_class = "android.widget.Button"
uiautomator_file_name = "window_dump.xml"
list_container_class = "androidx.recyclerview.widget.RecyclerView"

# All known "Following" button texts across languages
# "Friends" is intentionally excluded – mutual follows are kept!
FOLLOWING_TEXTS = [
    "Following",     # English
    "Folge ich",     # German
    "Abonniert",     # German (older versions)
    "Siguiendo",     # Spanish
    "Abonné(e)",     # French
    "Seguindo",      # Portuguese
    "Sto seguendo",  # Italian
    "フォロー中",       # Japanese
    "팔로잉",          # Korean
    "正在关注",         # Chinese
]

BTN_WIDTH_MIN  = 50
BTN_WIDTH_MAX  = 200
BTN_HEIGHT_MIN = 20
BTN_HEIGHT_MAX = 60

# Global controls
paused   = False
restart  = False
quitting = False


# ──────────────────────────────────────────
#  Keyboard listener (runs in background)
# ──────────────────────────────────────────
def keyboard_listener():
    global paused, restart, quitting
    while not quitting:
        key = get_key()
        if key == "s":
            paused = True
            print("\n[S] Script paused - press P to continue")
        elif key == "p":
            paused = False
            print("\n[P] Resuming...")
        elif key == "r":
            print("\n[R] Restarting...")
            restart = True
            paused  = False
        elif key == "q":
            print("\n[Q] Stopping script...")
            quitting = True
        time.sleep(0.05)


# ──────────────────────────────────────────
#  Helper functions
# ──────────────────────────────────────────
def get_bounds(bound):
    try:
        [left_top, right_bottom] = bound.split("][")
        left, top     = left_top[1:].split(",")
        right, bottom = right_bottom[:-1].split(",")
        return int(left), int(top), int(right), int(bottom)
    except Exception:
        return 0, 0, 0, 0


def find_node_bounds(xml_path, density_scale):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    btn_centers           = []
    list_container_bounds = []

    for elem in root.iter(node_tag):
        if list_container_class in elem.attrib.get("class", ""):
            list_container_bounds = get_bounds(elem.attrib.get("bounds", ""))

        if len(list_container_bounds) == 0:
            continue

        text = elem.attrib.get("text", "")
        cls  = elem.attrib.get("class", "")

        if cls != followed_btn_class or text not in FOLLOWING_TEXTS:
            continue

        bounds = elem.attrib.get("bounds", "")
        if not bounds:
            continue

        left, top, right, bottom = get_bounds(bounds)
        btn_w_dp = int((right - left) / density_scale)
        btn_h_dp = int((bottom - top) / density_scale)

        if BTN_WIDTH_MIN <= btn_w_dp <= BTN_WIDTH_MAX and BTN_HEIGHT_MIN <= btn_h_dp <= BTN_HEIGHT_MAX:
            btn_centers.append([(left + right) // 2, (top + bottom) // 2])

    return btn_centers, list_container_bounds


def ask_retry():
    answer = input("Try again? (y/n): ").strip().lower()
    return answer == "y"


def cleanup():
    global quitting
    quitting = True
    subprocess.run("adb shell settings put global animator_duration_scale 1".split())
    if os.path.exists(uiautomator_file_name):
        os.remove(uiautomator_file_name)


# ──────────────────────────────────────────
#  Main
# ──────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 52)
    print("        TikTok Auto-Unfollow Script")
    print("=" * 52)
    print("  Friends (mutual follows) will NOT be unfollowed!")
    print("=" * 52)
    print()
    print("  Controls:")
    print("  -----------------------------------------")
    print("  [S]  Pause the script")
    print("  [P]  Resume after pause")
    print("  [R]  Restart from current position")
    print("  [Q]  Quit the script")
    print("  -----------------------------------------")
    print()
    print("  Before starting make sure:")
    print("  1. TikTok is open on your phone")
    print("  2. You are on the Following list")
    print("  3. The screen is unlocked")
    print("=" * 52)
    print()

    # Check ADB connection
    devices      = subprocess.run("adb devices".split(), capture_output=True)
    device_lines = devices.stdout.decode("utf-8").strip().split("\n")
    if len(device_lines) < 2 or "device" not in device_lines[1]:
        print("ERROR: No device found!")
        print("  Make sure:")
        print("  1. Your phone is connected via USB")
        print("  2. USB Debugging is enabled")
        print("  3. You confirmed the popup on your phone")
        exit(1)
    print(f"Device connected: {device_lines[1].split()[0]}")

    # Get screen density
    density_result = subprocess.run("adb shell wm density".split(), capture_output=True)
    if "ERROR" in str(density_result.stderr):
        print("ERROR: Could not read screen density")
        exit(1)

    density       = int(density_result.stdout.split()[-1].decode("utf-8"))
    density_scale = density / 160
    print(f"Screen density: {density} dpi")
    print()
    print("Starting... Press S to pause at any time.")
    print("=" * 52)

    # Start keyboard listener thread
    t = threading.Thread(target=keyboard_listener, daemon=True)
    t.start()

    try_stop_anim    = False
    total_unfollowed = 0

    while not quitting:

        # Pause loop
        if paused:
            time.sleep(0.2)
            continue

        # Reset restart flag
        if restart:
            restart = False
            print("Restarting...\n")

        print("Reading UI layout...")

        result = subprocess.run(
            "adb shell uiautomator dump --compressed".split(), capture_output=True
        )

        if "ERROR" in str(result.stderr):
            if not try_stop_anim:
                try_stop_anim = True
                print("Warning: Error reading UI layout, disabling animations and retrying...")
                subprocess.run("adb shell settings put global animator_duration_scale 0".split())
                continue
            else:
                print("Error: Could not read UI layout.")
                if ask_retry():
                    try_stop_anim = False
                    continue
                else:
                    break
        try_stop_anim = False

        subprocess.run("adb pull /sdcard/window_dump.xml .".split(), capture_output=True)
        btn_centers, container_bounds = find_node_bounds(uiautomator_file_name, density_scale)

        if not container_bounds:
            print("Error: No list container found.")
            print("Tip: Make sure you are on the Following list in TikTok!")
            if ask_retry():
                continue
            else:
                break

        if not btn_centers:
            print("No Following buttons found.")
            print("Tip: Try scrolling manually a bit and then retry.")
            if ask_retry():
                continue
            else:
                break

        print(f"Found {len(btn_centers)} button(s), clicking...")
        for center in btn_centers:
            if quitting:
                break
            if paused:
                print("Paused... press P to resume")
                while paused and not quitting:
                    time.sleep(0.2)
            subprocess.run(f"adb shell input tap {center[0]} {center[1]}".split())
            total_unfollowed += 1
            time.sleep(0.6)

        print(f"Total unfollowed so far: {total_unfollowed}")

        if quitting:
            break

        # Scroll down
        h_center        = (container_bounds[0] + container_bounds[2]) // 2
        top             = container_bounds[1]
        bottom          = container_bounds[3]
        scroll_distance = int((bottom - top) * 0.4)

        print("Scrolling...")
        subprocess.run(
            f"adb shell input swipe {h_center} {bottom - 100} {h_center} {bottom - 100 - scroll_distance} 400".split()
        )
        time.sleep(0.8)
        print("=" * 52)

    cleanup()
    print(f"\nDone! Unfollowed {total_unfollowed} accounts in total.")
