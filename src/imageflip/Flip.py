import cv2;
import numpy as np;
import os;

def flip_images(imgPathList):

	# 反転
	for path in imgPathList:
		ext = os.path.splitext(path)[1];

		# cv2は日本語ファイルやパスを扱えないため、numpy経由で開く
		buf = np.fromfile(path, np.uint8);
		img = cv2.imdecode(buf, cv2.IMREAD_UNCHANGED);

		# 反転
		imgFlipped = cv2.flip(img, 1);

		# 保存
		ret, buf = cv2.imencode(ext, imgFlipped);
		with open(path, mode="w+b") as f:
			buf.tofile(f);
		print(f"finished: {path}");
