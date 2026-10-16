
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Priya\Downloads\pic.jpeg", 0)

if img is None:
    print("Image not found")
else:
    kernel = np.ones((9, 9), np.uint8)
    result = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

    original = cv2.resize(img, (300, 400))
    output = cv2.resize(result, (300, 400))

    cv2.imshow("Original | Top Hat", np.hstack((original, output)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
