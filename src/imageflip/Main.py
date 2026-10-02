import FreeSimpleGUI as gui;
import os;
import sys;
import FindImages;
import Flip;

# specファイルなしなら下記のように長いコマンドが要る
# uv run pyinstaller .\src\imageflip\Main.py --onefile --noconsole --icon=ImageFlipper2_256.ico
# specありなら下記で可
# uv run pyinstaller .\Main.spec 

# 1ファイルにまとめると起動が遅くなる
# あえてそうする理由はないか

# pyinstallerでまとめた画像ファイル等は実行時に展開される
# ただし、展開先はカレントディレクトリではなく専用のディレクトリだ
# そちらを使う場合（exe化した後など）は、そっちから読み込んでくるようにパスを修正する
# 1ファイル化していないケースでも効いた
def resource_path(relativePass):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relativePass);
    return os.path.join(os.path.abspath('.'), relativePass);

# テーマ
gui.theme("DarkBlue10");

# レイアウト
layout = [
	[gui.Text("指定したディレクトリ内の画像をすべて左右反転します。\nサブディレクトリ内も処理対象です。", size=(50, 2))],
	[gui.Text("なんか問題起こっても責任取れないので注意してください！", size=(50, 1))],
	[gui.Text("フォルダパス"), gui.InputText(size=(50, 1), key="-INPUT-"), gui.FolderBrowse(key="-BROWSE-", target="-INPUT-")],
	[gui.Button("処理開始", key="-START-")]
];

# メインループ
window = gui.Window("左右反転プログラム", layout, icon=resource_path("ImageFlipper2_256.ico"));
while True:
	event, values = window.read();

	if event == gui.WIN_CLOSED or event == "-EXIT-":
		break;

	if event == "-START-":
		pathList = FindImages.find_images(values["-INPUT-"]);
		if (pathList == []):
			gui.popup_ok("画像が見つかりませんでした。あるいはフォルダが指定されてないか。", title="Info");
			continue;
		
		imgCount = len(pathList);
		result = gui.popup_ok_cancel(f"{imgCount}個の画像が見つかりました。処理を開始してもよろしいですか？", title="Info");

		if result == "OK":
			Flip.flip_images(pathList);
			gui.popup_ok("完了しました。", title="Info");

window.close();
