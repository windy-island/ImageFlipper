# -*- mode: python ; coding: utf-8 -*-

# 定義済みの変数がある
print(SPEC);			# specファイルのパス
print(SPECPATH);		# specファイルのあるフォルダパス
print(f"{SPECPATH}/src/imageflip/");

a = Analysis(
    [f"{SPECPATH}/src/imageflip/Main.py"],					# 処理対象のpyファイル（mainだけでいい）
    pathex=[f"{SPECPATH}/src/imageflip/"],					# pythonスクリプトのパス（デフォではカレントディレクトリが使われる）
    binaries=[],
    datas=[(f"{SPECPATH}/ImageFlipper2_256.ico", "./")],	# 追加のデータファイル（画像など）
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,

	# a.binaries,
	# a.datas,

    [],
    exclude_binaries=True,
    name='App',										# 出力されるEXEの名前
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,

	# upx_exclude=[],
	# runtime_tmpdir=None,

    console=False,									# consoleがいるかどうか
	icon="./ImageFlipper2_256.ico",					# アイコンのパス
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='左右反転',					# 出力されるディレクトリの名前
)
