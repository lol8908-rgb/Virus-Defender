# SafeGuard

Ein leistungsstarker und benutzerfreundlicher Antivirus-Scanner für sicheres Computing.

---

## 🚀 Schnellstart

### Download
[![Download SafeGuard](https://img.shields.io/badge/Download-SafeGuard%20v1.0.0-green?style=for-the-badge&logo=github)](https://github.com/lol8908-rgb/Virus-Defender/releases/download/v1.0.0/safeguard-v1.0.0.zip)

> Klicke oben auf den Button um die neueste Version herunterzuladen.

---

## 🔧 Installation & Setup

### Automatisches Setup (Empfohlen) ⭐

Das einfachste - führe einfach ein Setup-Script aus!

**Windows:**
```bash
# Lade das Repository herunter oder klone es
git clone https://github.com/lol8908-rgb/Virus-Defender.git
cd Virus-Defender

# Starte das Setup (erzeugt eine ausführbare SafeGuard.exe)
setup_safeguard.bat
```

**Linux/Mac:**
```bash
# Lade das Repository herunter oder klone es
git clone https://github.com/lol8908-rgb/Virus-Defender.git
cd Virus-Defender

# Starte das Setup
chmod +x setup_safeguard.sh
./setup_safeguard.sh
```

Das Setup-Script macht alles automatisch:
1. ✅ Installiert Python-Abhängigkeiten
2. ✅ Installiert PyInstaller
3. ✅ Baut die ausführbare Datei

Nach dem Setup findest du:
- **Windows:** `dist/SafeGuard.exe` - die ausführbare Datei!
- **Linux/Mac:** `dist/SafeGuard` - die ausführbare Datei!

---

### Manuelle Installation

Falls du das Setup-Script nicht nutzen möchtest:

```bash
# Projekt klonen
git clone https://github.com/lol8908-rgb/Virus-Defender.git
cd Virus-Defender

# Abhängigkeiten installieren
pip install -r requirements.txt

# PyInstaller installieren
pip install pyinstaller

# SafeGuard bauen
pyinstaller safeguard.spec
```

---

🏗️ Bauen mit Python

Das Projekt nutzt **PyInstaller** um eine eigenständige ausführbare Datei zu erstellen.

### Automatischer Build (Empfohlen)

```bash
# Windows
setup_safeguard.bat

# Linux/Mac
./setup_safeguard.sh
```

### Manueller Build

Falls du mehr Kontrolle brauchst:

```bash
# 1. Abhängigkeiten
pip install -r requirements.txt

# 2. PyInstaller
pip install pyinstaller

# 3. Build mit Spec-File
pyinstaller safeguard.spec

# Fertig! Deine ausführbare Datei ist in: dist/SafeGuard (oder dist/SafeGuard.exe auf Windows)
```

### Build-Optionen (Advanced)

Falls du das Spec-File anpassen möchtest:

```bash
# Onefile-Build (eine einzelne EXE statt Bundle)
pyinstaller --onefile --console --name SafeGuard safeguard/__main__.py

# Mit Icon (Windows)
pyinstaller safeguard.spec --icon=icon.ico
```

---

## ▶️ Verwendung

### Nach dem Setup (Empfohlen)

Die ausführbare Datei nutzen (kein Python nötig!):

**Windows:**
```bash
dist/SafeGuard.exe --help
dist/SafeGuard.exe --scan "C:\Users\YourName\Documents"
```

**Linux/Mac:**
```bash
./dist/SafeGuard --help
./dist/SafeGuard --scan ~/Documents
```

### Direktes Python-Skript

Falls du das Script direkt ausführen möchtest:

```bash
# SafeGuard starten
python -m safeguard

# Mit Scan-Verzeichnis
python -m safeguard --scan ~/Documents

# Vollständiger Help
python -m safeguard --help
```

---

## 📋 Features

- ✅ Echtzeit-Bedrohungserkennung
- ✅ Schnelle Dateiscans
- ✅ Quarantäne-System
- ✅ Automatische Updates
- ✅ Benutzerfreundliche CLI

---

## 📝 Lizenz

MIT License - Siehe LICENSE für Details.