# Tik-Tok-Unfollow-Bot-Python-Script-Android-
Python Script for unfollowing People on Tik Tok automaticly

# TikTok Auto-Unfollow Script 🚀

This script automatically unfollows all accounts you follow on TikTok – **except your friends** (mutual follows are kept).

---

## ✅ Supported Languages

The script works with TikTok in the following languages:
- 🇺🇸 English
- 🇩🇪 German
- 🇪🇸 Spanish
- 🇫🇷 French
- 🇧🇷 Portuguese
- 🇮🇹 Italian
- 🇯🇵 Japanese
- 🇰🇷 Korean
- 🇨🇳 Chinese

---

## 📋 What you need

- A Windows, Mac or Linux PC
- An Android phone with TikTok installed
- A USB cable
- Python 3 (free)
- ADB (free)

> ⚠️ **Android only!** iPhones are not supported.

---

## 🔧 Installation – Step by Step

### 1. Install Python

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Click **"Download Python"**
3. Run the installer – **important:** check the box **"Add Python to PATH"** before clicking install!
4. To verify it worked, open CMD (press Windows key → type `cmd`) and type:
   ```
   python --version
   ```
   You should see something like `Python 3.x.x`.

---

### 2. Install ADB

ADB (Android Debug Bridge) is a tool that lets your PC communicate with your phone.

**Windows:**
1. Go to [developer.android.com/tools/releases/platform-tools](https://developer.android.com/tools/releases/platform-tools)
2. Click **"Download SDK Platform-Tools for Windows"**
3. Extract the ZIP file somewhere easy to find (e.g. your Desktop)
4. Open CMD inside that folder: Shift + Right-click in the folder → **"Open PowerShell/CMD here"**
5. Type `adb version` – if you see a version number it worked ✅

**Mac:**
1. Install [Homebrew](https://brew.sh) if you don't have it
2. Open Terminal and type:
   ```
   brew install android-platform-tools
   ```

**Linux:**
```bash
sudo apt install adb
```

---

### 3. Enable USB Debugging on your phone

1. Open **Settings** on your phone
2. Tap **"About phone"**
3. Tap **"Build number"** **7 times quickly** until you see a message saying you are now a developer
4. Go back to Settings → you will now see **"Developer options"**
5. Open Developer options and enable **"USB Debugging"**

---

### 4. Connect your phone to your PC

1. Plug your phone into your PC via USB
2. A popup will appear on your phone: **"Allow USB Debugging?"** → tap **"Allow"**
3. Verify the connection by typing in CMD:
   ```
   adb devices
   ```
   Your device should appear, for example:
   ```
   List of devices attached
   ABC123XYZ    device
   ```
   If it says `unauthorized`, check your phone – you need to confirm the popup.

---

### 5. Download the script

1. Download `unfollow.py` from this page (top right → **"Code"** → **"Download ZIP"**)
2. Extract the ZIP and place `unfollow.py` in the same folder as ADB

---

## ▶️ Running the script

### Prepare TikTok:
1. Open TikTok on your phone
2. Go to your **Profile**
3. Tap **"Following"** to open your following list
4. Keep this list open and your screen unlocked!

### Start the script:
1. Open CMD in the folder where `unfollow.py` is located
2. Type:
   ```
   python unfollow.py
   ```
3. The script will start and show you everything you need to know!

---

## ⌨️ Controls while the script is running

| Key | Action |
|-----|--------|
| **S** | ⏸ Pause the script |
| **P** | ▶ Resume after pause |
| **R** | 🔄 Restart from current position |
| **Q** | ⏹ Quit the script cleanly |

> **Tip:** Press **S** if you want to manually scroll on your phone, then press **P** to continue.

If no buttons are found, the script will also ask:
```
Try again? (y/n):
```
- Press **y** → tries again (useful if you scrolled manually)
- Press **n** → script exits

---

## ⚠️ Important notes

- **Friends are NOT unfollowed** – only one-sided follows are removed
- **Don't do too many at once** – take a break after 300-500 unfollows so TikTok doesn't temporarily block you
- **Keep your screen unlocked** – the script needs access to the screen
- **Keep TikTok open** – don't switch to other apps while the script is running

---

## ❓ Common issues

**"adb devices" shows nothing:**
→ Check your USB cable, try a different one, confirm the popup on your phone

**Script can't find any buttons:**
→ Make sure you are actually on the Following list and not on your profile page

**TikTok stops responding:**
→ Restart TikTok, navigate back to the Following list, press **R** to restart the script

**"Python is not recognized":**
→ Reinstall Python and make sure to check **"Add to PATH"** this time

---

## 📜 License

This script is free to use for everyone. Use it at your own risk – automated tools violate TikTok's Terms of Service.
