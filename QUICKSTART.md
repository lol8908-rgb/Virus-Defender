# SafeGuard - Schnellstart Anleitung

Du hast SafeGuard heruntergeladen aber weißt nicht, wie es geht? Hier ist der einfachste Weg!

---

## 🪟 Für Windows-Nutzer

### Schritt 1: Repository herunterladen
- Gehe auf https://github.com/lol8908-rgb/Virus-Defender
- Klicke auf **Code** (grüner Button) → **Download ZIP**
- Entpack die ZIP-Datei irgendwo

### Schritt 2: Setup ausführen
- Öffne `setup_safeguard.bat` (doppelklick)
- Warte bis alles installiert ist
- Am Schluss wird angezeigt wo `SafeGuard.exe` ist

### Schritt 3: SafeGuard nutzen
```
SafeGuard.exe --help
SafeGuard.exe --scan "C:\Meine Dateien"
```

**Fertig!** SafeGuard ist jetzt einsatzbereit.

---

## 🐧 Für Linux/Mac-Nutzer

### Schritt 1: Repository klonen
```bash
git clone https://github.com/lol8908-rgb/Virus-Defender.git
cd Virus-Defender
```

### Schritt 2: Setup ausführen
```bash
chmod +x setup_safeguard.sh
./setup_safeguard.sh
```

### Schritt 3: SafeGuard nutzen
```bash
./dist/SafeGuard --help
./dist/SafeGuard --scan ~/Documents
```

**Fertig!** SafeGuard ist jetzt einsatzbereit.

---

## ❌ Falls etwas nicht funktioniert

### Fehler: "Python ist nicht installiert"
**Lösung:**
- **Windows:** Download von https://www.python.org/ (wichtig: "Add Python to PATH" ankreuzen!)
- **Mac:** `brew install python3`
- **Linux:** `sudo apt-get install python3 python3-pip`

### Fehler: "pyinstaller: command not found"
Das Setup-Script sollte das installieren. Falls nicht:
```bash
pip install pyinstaller
```

### Fehler: Dateien öffnen sich im Editor statt auszuführen
Das ist normal! Du brauchst die **kompilierte Datei** aus dem `dist/` Verzeichnis, nicht die Python-Quellen.

Nutze das Setup-Script um sie zu bauen!

---

## 💡 Tipps

- SafeGuard brauchst die `.exe` / `-Datei aus dem `dist/` Verzeichnis
- Du kannst sie überall hin kopieren und nutzen
- Keine Python-Installation auf dem Ziel-Computer nötig!

---

Fragen? Öffne ein Issue auf GitHub: https://github.com/lol8908-rgb/Virus-Defender/issues
