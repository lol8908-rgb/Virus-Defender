@echo off
REM SafeGuard - Windows Batch Wrapper
REM Dieses Skript ermöglicht einfache Nutzung von SafeGuard auf Windows

setlocal enabledelayedexpansion

REM Finde Python im System
for /f "delims=" %%i in ('where python') do set PYTHON_EXE=%%i

if not defined PYTHON_EXE (
    echo [ERROR] Python nicht gefunden! Bitte Python installieren und zum PATH hinzufuegen.
    pause
    exit /b 1
)

REM Starten Sie SafeGuard
"%PYTHON_EXE%" -m safeguard %*

endlocal
