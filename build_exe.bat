@echo off
REM SafeGuard Windows Build Script
REM Erstelle die SafeGuard.exe auf Windows

echo.
echo ========================================
echo SafeGuard EXE Builder
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python nicht gefunden!
    echo Bitte Python von https://python.org installieren
    pause
    exit /b 1
)

echo [1/4] Installiere Abhangigkeiten...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Fehler beim Installieren der Abhangigkeiten
    pause
    exit /b 1
)

echo [2/4] Installiere PyInstaller...
pip install -q pyinstaller
if errorlevel 1 (
    echo [ERROR] Fehler beim Installieren von PyInstaller
    pause
    exit /b 1
)

echo [3/4] Baue SafeGuard.exe...
pyinstaller safeguard.spec -y
if errorlevel 1 (
    echo [ERROR] Fehler beim Bauen der EXE
    pause
    exit /b 1
)

echo [4/4] Cleanup...
rmdir /s /q build >nul 2>&1
del SafeGuard.spec >nul 2>&1

echo.
echo ========================================
echo ERFOLGREICH!
echo ========================================
echo.
echo SafeGuard.exe erstellt in: dist\SafeGuard.exe
echo.
echo Testen Sie die EXE:
echo   dist\SafeGuard.exe --version
echo.
pause
