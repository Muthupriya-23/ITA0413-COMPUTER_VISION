
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Priya\Downloads\pic.jpeg")

if img is None:
    print("Image not found")
else:
    h, w = img.shape[:2]

    if h < 200 or w < 200:
        print("Image is too small")
    else:
        roi = img[0:100, 0:100]
        copied = roi.copy()

        result = img.copy()
        result[100:200, 100:200] = copied

        original = cv2.resize(img, (300, 400))
        output = cv2.resize(result, (300, 400))
        combined = np.hstack((original, output))

        cv2.imshow("Original | ROI Pasted", combined)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
