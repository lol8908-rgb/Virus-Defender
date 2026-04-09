# SafeGuard - Detaillierte Installationsanleitung

Vollständige Schritt-für-Schritt Anleitung um SafeGuard funktionsfähig zu machen.

---

## Windows - Komplette Anleitung

### Voraussetzung: Python installieren

1. **Gehe zu** https://www.python.org/downloads/
2. **Download Python 3.11 oder neuer** (roter Download-Button)
3. **Starte den Installer**
4. **WICHTIG:** Aktiviere BEIDE Häkchen:
   - ☑️ "Add Python to PATH"
   - ☑️ "Install pip"
5. Klick auf "Install Now"
6. Warte bis Installation fertig ist

**Verify Installation:**
- Öffne Command Prompt (Win + R, tippe `cmd`, Enter)
- Tippe: `python --version`
- Du solltest sehen: `Python 3.11.x` (oder höher)

### SafeGuard installieren

1. **Repository herunterladen:**
   - Gehe auf https://github.com/lol8908-rgb/Virus-Defender
   - Klick auf grünen "Code" Button
   - Wähle "Download ZIP"
   - Entpack die ZIP-Datei (Rechtsklick → "Extract All")

2. **Navigiere zum Ordner:**
   - Öffne Command Prompt
   - Tippe: `cd /path/to/Virus-Defender` (oder nutze "cd" mit Copy-Paste)
   - Beispiel: `cd C:\Users\YourName\Downloads\Virus-Defender`

3. **Setup starten:**
   - Tippe: `setup_safeguard.bat`
   - Oder doppelklick auf `setup_safeguard.bat` im Explorer

4. **Warte bis fertig**
   - Sollte ~1-2 Minuten dauern
   - Am Ende siehst du: "Setup abgeschlossen!"

5. **SafeGuard nutzen:**
   ```
   cd dist
   SafeGuard.exe --help
   SafeGuard.exe --scan "C:\Windows\Temp"
   ```

---

## Linux - Komplette Anleitung

### Voraussetzung: Python und pip

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv

# Verify
python3 --version   # sollte Python 3.8+ sein
pip3 --version      # sollte pip für Python anzeigen
```

### SafeGuard installieren

```bash
# 1. Repository klonen
git clone https://github.com/lol8908-rgb/Virus-Defender.git
cd Virus-Defender

# 2. Setup starten
chmod +x setup_safeguard.sh
./setup_safeguard.sh

# 3. Warte bis fertig (1-2 Minuten)

# 4. SafeGuard nutzen
cd dist
./SafeGuard --help
./SafeGuard --scan ~/Documents
```

---

## macOS - Komplette Anleitung

### Voraussetzung: Homebrew und Python

```bash
# Installiere Homebrew (falls noch nicht installiert)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installiere Python
brew install python3

# Verify
python3 --version
pip3 --version
```

### SafeGuard installieren

```bash
# 1. Repository klonen
git clone https://github.com/lol8908-rgb/Virus-Defender.git
cd Virus-Defender

# 2. Setup starten
chmod +x setup_safeguard.sh
./setup_safeguard.sh

# 3. Warte bis fertig

# 4. SafeGuard nutzen
cd dist
./SafeGuard --help
./SafeGuard --scan ~/Documents
```

---

## Fehlerbehebung

### Problem: "Python is not installed"

**Windows:**
- Gehe zu https://www.python.org/
- Download die neueste Version
- **WICHTIG:** Aktiviere "Add Python to PATH" beim Install
- Starte Command Prompt neu

**Linux/macOS:**
```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-pip

# macOS
brew install python3
```

### Problem: "No module named 'pip'"

```bash
# Windows
python -m ensurepip

# Linux/macOS
python3 -m ensurepip
```

### Problem: "Permission denied" (Linux/Mac)

```bash
# Mache Script ausführbar
chmod +x setup_safeguard.sh
./setup_safeguard.sh
```

### Problem: Setup bricht ab

- Stelle sicher dass Python installiert ist
- Probiere manuell:
```bash
pip install -r requirements.txt
pip install pyinstaller
pyinstaller safeguard.spec
```

---

## Manueller Build (Alternativ zum Setup-Script)

Falls das Setup-Script irgendwelche Probleme hat:

```bash
# 1. Im SafeGuard-Verzeichnis
cd Virus-Defender

# 2. Abhängigkeiten
pip install -r requirements.txt

# 3. PyInstaller
pip install pyinstaller

# 4. Build
pyinstaller safeguard.spec

# 5. Fertig!
# Windows: dist/SafeGuard.exe
# Linux/Mac: dist/SafeGuard
```

---

## Wo ist meine ausführbare Datei?

Nach erfolgreichem Setup/Build findest du:

- **Windows:** `Virus-Defender\dist\SafeGuard.exe`
- **Linux/Mac:** `Virus-Defender/dist/SafeGuard`

Du kannst diese Datei überall hin kopieren und nutzen!

---

## Weitere Hilfe

- Schau dir `QUICKSTART.md` für die Kurzversion an
- Öffne ein Issue auf GitHub: https://github.com/lol8908-rgb/Virus-Defender/issues
- Schreib einen Kommentar auf der Release-Seite
