from pathlib import Path;
import os;

# 画像判定用の拡張子一覧
IMG_EXT_LIST = [".png", ".bmp", ".jpg", ".jpeg", ".webp", ".gif", ".ico"];

def find_images(dir):

	if (not os.path.isdir(dir)):
		return [];
		
	# 指定されたディレクトリ下を走査
	p = Path(dir);
	pathList = list(p.glob("**/*"));

	# 画像ファイルだけ取得
	imgFiles = [];
	for path in pathList:
		if path.is_file() == True:
			ext = path.suffix;
			for imgExt in IMG_EXT_LIST:
				if (ext == imgExt):
					imgFiles.append(str(path.resolve()));
					continue;
	
	return imgFiles;
