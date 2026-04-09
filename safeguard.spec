# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller Spec File für SafeGuard
Nutze dies auf Windows: pyinstaller safeguard.spec
"""

a = Analysis(
    ['safeguard/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['click', 'colorama', 'watchdog', 'psutil', 'pycryptodome', 'yaml'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SafeGuard',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
