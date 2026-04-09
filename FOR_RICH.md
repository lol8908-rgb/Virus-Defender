## 📦 Für Rich: So bauen Sie SafeGuard.exe

### 🎯 Schnellste Methode (Windows)

1. **Diesen Ordner auf Windows kopieren**
2. **`build_exe.bat` doppelklicken** ← Fertig! ✨

Das Skript macht alles automatisch:
- Installiert Python-Abhängigkeiten
- Lädt PyInstaller
- Erstellt `dist/SafeGuard.exe`

### 📋 Manuelle Methode

Falls das Batch-Skript nicht funktioniert:

```bash
# 1. Terminal hier öffnen (Shift + Rechtsklick)
# 2. Diese Befehle eingeben:

pip install -r requirements.txt
pip install pyinstaller
pyinstaller safeguard.spec
```

**Ergebnis:** `dist/SafeGuard.exe`

### 🚀 Nutzen der EXE

```bash
SafeGuard.exe --scan C:\zu\scannendes\Verzeichnis
SafeGuard.exe --version
SafeGuard.exe --help
```

### 📦 Alternative: Python-Paket

Wer Python nutzt, kann auch direkt installieren:

```bash
pip install .
safeguard --scan <DIR>
```

---

**Fragen?** Schreib ein Issue auf GitHub!
