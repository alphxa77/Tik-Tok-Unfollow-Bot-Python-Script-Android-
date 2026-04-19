# TikTok Auto-Unfollow Script 🚀

Dieses Script entfolgt automatisch allen Accounts auf TikTok denen du folgst – **außer deinen Freunden** (gegenseitiges Folgen bleibt erhalten).

---

## ✅ Unterstützte Sprachen

Das Script funktioniert mit TikTok in folgenden Sprachen:
- 🇺🇸 Englisch
- 🇩🇪 Deutsch
- 🇪🇸 Spanisch
- 🇫🇷 Französisch
- 🇧🇷 Portugiesisch
- 🇮🇹 Italienisch
- 🇯🇵 Japanisch
- 🇰🇷 Koreanisch
- 🇨🇳 Chinesisch

---

## 📋 Was du brauchst

- Ein Windows, Mac oder Linux PC
- Ein Android Handy mit TikTok
- Ein USB Kabel
- Python 3 (kostenlos)
- ADB (kostenlos)

> ⚠️ **Funktioniert NUR mit Android!** iPhones werden nicht unterstützt.

---

## 🔧 Installation – Schritt für Schritt

### 1. Python installieren

1. Geh auf [python.org/downloads](https://www.python.org/downloads/)
2. Klick auf **"Download Python"**
3. Installiere es – **wichtig:** beim Installieren den Haken bei **"Add Python to PATH"** setzen!
4. Um zu prüfen ob es geklappt hat: öffne CMD (Windows-Taste → `cmd` eingeben) und tippe:
   ```
   python --version
   ```
   Es sollte sowas wie `Python 3.x.x` erscheinen.

---

### 2. ADB installieren

ADB (Android Debug Bridge) ist ein Tool womit dein PC mit deinem Handy kommunizieren kann.

**Windows:**
1. Geh auf [developer.android.com/tools/releases/platform-tools](https://developer.android.com/tools/releases/platform-tools)
2. Klick auf **"Download SDK Platform-Tools for Windows"**
3. Entpacke die ZIP-Datei z.B. auf deinen Desktop
4. Merke dir den Pfad zu dem Ordner (z.B. `C:\Users\DeinName\Desktop\platform-tools`)
5. Öffne CMD in diesem Ordner: Shift + Rechtsklick im Ordner → **"PowerShell/CMD hier öffnen"**
6. Tippe `adb version` – wenn eine Versionsnummer erscheint hat es geklappt ✅

**Mac:**
1. Installiere [Homebrew](https://brew.sh) falls noch nicht vorhanden
2. Öffne Terminal und tippe:
   ```
   brew install android-platform-tools
   ```

**Linux:**
```bash
sudo apt install adb
```

---

### 3. USB-Debugging auf dem Handy aktivieren

1. Geh in die **Einstellungen** deines Handys
2. Tippe auf **"Über das Telefon"**
3. Tippe **7x schnell hintereinander** auf **"Build-Nummer"** bis eine Meldung erscheint dass du Entwickler bist
4. Geh zurück zu den Einstellungen → jetzt gibt es **"Entwickleroptionen"**
5. Öffne Entwickleroptionen und aktiviere **"USB-Debugging"**

---

### 4. Handy mit PC verbinden

1. Verbinde dein Handy per USB mit dem PC
2. Auf dem Handy erscheint ein Popup: **"USB-Debugging erlauben?"** → auf **"Erlauben"** tippen
3. Prüfe die Verbindung indem du in CMD tippst:
   ```
   adb devices
   ```
   Es sollte dein Gerät erscheinen, z.B.:
   ```
   List of devices attached
   ABC123XYZ    device
   ```
   Wenn dort `unauthorized` steht, schau nochmal auf dein Handy – der Popup muss bestätigt werden.

---

### 5. Script herunterladen

1. Lade die Datei `unfollow.py` von dieser Seite herunter (oben rechts auf **"Code"** → **"Download ZIP"**)
2. Entpacke die ZIP und lege `unfollow.py` in denselben Ordner wie ADB

---

## ▶️ Script starten

### TikTok vorbereiten:
1. Öffne TikTok auf deinem Handy
2. Geh auf dein **Profil**
3. Tippe auf **"Following"** (die Liste der Leute denen du folgst)
4. Lass diese Liste offen und den Bildschirm entsperrt!

### Script starten:
1. Öffne CMD im Ordner wo `unfollow.py` liegt
2. Tippe:
   ```
   python unfollow.py
   ```
3. Das Script startet und zeigt dir alles an was du wissen musst!

---

## ⌨️ Steuerung während das Script läuft

| Taste | Funktion |
|-------|----------|
| **S** | ⏸ Pause – Script hält an |
| **P** | ▶ Weiter – Script läuft weiter nach der Pause |
| **R** | 🔄 Neustart – fängt nochmal von vorne an |
| **Q** | ⏹ Beenden – Script wird sauber beendet |

> **Tipp:** Drücke **S** wenn du zwischendurch manuell auf dem Handy scrollen willst, und danach **P** um weiterzumachen.

Falls es keine Buttons findet fragt es dich außerdem:
```
Try again? (y/n):
```
- **y** drücken → versucht es nochmal
- **n** drücken → Script beendet sich

---

## ⚠️ Wichtige Hinweise

- **Freunde werden NICHT entfolgt** – nur einseitige Follows werden entfernt
- **Nicht zu viele auf einmal** – mach nach 300-500 eine Pause von ein paar Stunden damit TikTok nichts sperrt
- **Handy entsperrt lassen** – das Script braucht Zugriff auf den Bildschirm
- **TikTok offen lassen** – nicht in andere Apps wechseln während das Script läuft

---

## ❓ Häufige Probleme

**"adb devices" zeigt nichts an:**
→ USB-Kabel prüfen, anderes Kabel probieren, Popup auf dem Handy bestätigen

**Script findet keine Buttons:**
→ Stelle sicher dass du wirklich in der Following-Liste bist und nicht auf dem Profil

**TikTok reagiert nicht mehr:**
→ TikTok neu starten, zur Following-Liste navigieren, **R** drücken zum Neustart

**"Python wird nicht erkannt":**
→ Python nochmal installieren und diesmal **"Add to PATH"** anhaken

---

## 📜 Lizenz

Dieses Script ist kostenlos und für jeden nutzbar. Nutz es auf eigene Gefahr – automatisierte Tools verstoßen gegen TikToks Nutzungsbedingungen.
