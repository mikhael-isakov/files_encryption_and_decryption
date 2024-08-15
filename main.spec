# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:\\FilesEncryption\\main.py'],
             pathex=['E:\\FilesEncryption'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('main_icon.ico', 'E:\\FilesEncryption\\icons\\main_icon.ico', "DATA"), 
            ('key.png', 'E:\\FilesEncryption\\icons\\key.png', "DATA"), 
            ('green.png', 'E:\\FilesEncryption\\icons\\green.png', "DATA"), 
           ]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='FilesEncryption',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='E:\\FilesEncryption\\icons\\main_icon.ico')
