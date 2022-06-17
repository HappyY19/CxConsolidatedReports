# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
    'win32ctypes.core.ctypes',
    'win32ctypes.core.ctypes._common',
    'win32ctypes.core.ctypes._dll',
    'win32ctypes.core.ctypes._resource',
    'win32ctypes.core.ctypes._system_information',
    'win32ctypes.core.ctypes._time',
    'win32ctypes.core.ctypes._authentication',
    'win32ctypes.pywin32.pywintypes',
    'win32ctypes.pywin32.win32cred'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='run',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
