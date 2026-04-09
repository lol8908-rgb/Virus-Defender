@echo off
REM SafeGuard Setup Script für Windows
REM Dieses Script installiert alles und baut die SafeGuard.exe

echo.
echo ========================================
echo   SafeGuard Setup
echo ========================================
echo.

REM Prüfe ob Python installiert ist
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python ist nicht installiert oder nicht in PATH!
    echo.
    echo Bitte installiere Python von https://www.python.org/
    echo Wichtig: Aktiviere "Add Python to PATH" beim Install!
    echo.
    pause
    exit /b 1
)

echo [OK] Python gefunden!
python --version
echo.

REM Installiere Abhängigkeiten
echo [1/3] Installiere Python-Abhängigkeiten...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Fehler beim Installieren der Abhängigkeiten!
    pause
    exit /b 1
)
echo [OK] Abhängigkeiten installiert!
echo.

REM Installiere PyInstaller
echo [2/3] Installiere PyInstaller...
pip install pyinstaller
if errorlevel 1 (
    echo [ERROR] Fehler beim Installieren von PyInstaller!
    pause
    exit /b 1
)
echo [OK] PyInstaller installiert!
echo.

REM Baue die EXE
echo [3/3] Baue SafeGuard.exe...
pyinstaller safeguard.spec
if errorlevel 1 (
    echo [ERROR] Fehler beim Build!
    pause
    exit /b 1
)
echo [OK] Build erfolgreich!
echo.

REM Informiere Nutzer
echo ========================================
echo   Setup abgeschlossen!
echo ========================================
echo.
echo SafeGuard.exe wurde erstellt in:
echo   dist\SafeGuard.exe
echo.
echo Du kannst SafeGuard.exe jetzt überall starten!
echo.
echo Beispiele:
echo   SafeGuard.exe --help
echo   SafeGuard.exe --scan C:\Users\YourName\Documents
echo.
pause
