# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['HelloUniversal.py'],
    pathex=[],
    binaries=[],
    datas=[('requirements.txt', '.'), ('/app/HelloUniversal/data/*', 'data')],
    hiddenimports=[],
    hookspath=['.'],
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
    name='hellouniversal',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    output_dir='bin'  # Specify the output directory
)
