#!/bin/bash
# SafeGuard Setup Script für Linux/Mac
# Dieses Script installiert alles und baut die SafeGuard executable

echo ""
echo "========================================"
echo "  SafeGuard Setup"
echo "========================================"
echo ""

# Prüfe ob Python installiert ist
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 ist nicht installiert!"
    echo ""
    echo "Bitte installiere Python3:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
    echo "  macOS: brew install python3"
    echo ""
    exit 1
fi

echo "[OK] Python3 gefunden!"
python3 --version
echo ""

# Installiere Abhängigkeiten
echo "[1/3] Installiere Python-Abhängigkeiten..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Fehler beim Installieren der Abhängigkeiten!"
    exit 1
fi
echo "[OK] Abhängigkeiten installiert!"
echo ""

# Installiere PyInstaller
echo "[2/3] Installiere PyInstaller..."
pip3 install pyinstaller
if [ $? -ne 0 ]; then
    echo "[ERROR] Fehler beim Installieren von PyInstaller!"
    exit 1
fi
echo "[OK] PyInstaller installiert!"
echo ""

# Baue die Executable
echo "[3/3] Baue SafeGuard executable..."
pyinstaller safeguard.spec
if [ $? -ne 0 ]; then
    echo "[ERROR] Fehler beim Build!"
    exit 1
fi
echo "[OK] Build erfolgreich!"
echo ""

# Mache executable ausführbar
chmod +x dist/SafeGuard

# Informiere Nutzer
echo "========================================"
echo "  Setup abgeschlossen!"
echo "========================================"
echo ""
echo "SafeGuard wurde erstellt in:"
echo "  dist/SafeGuard"
echo ""
echo "Du kannst SafeGuard jetzt starten mit:"
echo "  ./dist/SafeGuard --help"
echo "  ./dist/SafeGuard --scan ~/Documents"
echo ""
