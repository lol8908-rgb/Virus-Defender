# SafeGuard EXE - Build Anleitung für Windows

Für Rich und andere Nutzer: So erstellst du die **SafeGuard.exe** auf Windows.

## 🚀 Schnellstart (Windows)

### Option 1: Automatischer Build (Empfohlen)

```bash
# 1. Klone das Repository
git clone https://github.com/lol8908-rgb/Virus-Defender.git
cd Virus-Defender

# 2. Installiere Python-Abhängigkeiten
pip install -r requirements.txt

# 3. Installiere PyInstaller
pip install pyinstaller

# 4. Baue die EXE mit dem Spec-File
pyinstaller safeguard.spec

# Fertig! Die EXE findest du in: dist/SafeGuard.exe
```

### Option 2: Manueller PyInstaller-Befehl

```bash
pyinstaller --onefile --console --name SafeGuard --hidden-import=click --hidden-import=colorama safeguard/__main__.py
```

## 📦 Was brauchst du?

- **Python 3.8+** (von python.org)
- **pip** (läuft mit Python)
- **PyInstaller** (`pip install pyinstaller`)
- Alle Dependencies aus `requirements.txt`

## ✅ Nach dem Build

Wenn der Build erfolgreich war:
- `dist/SafeGuard.exe` - Die fertige Anwendung
- Diese `.exe` kannst du überall weitergeben und nutzen!

## 🔧 Die EXE nutzen

```bash
SafeGuard.exe --scan C:\path\to\folder
SafeGuard.exe --version
