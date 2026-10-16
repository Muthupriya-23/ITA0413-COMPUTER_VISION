
import cv2
import numpy as np

img = cv2.imread(
    r"C:\Users\Priya\Downloads\pic.jpeg", 0
)

if img is None:
    print("Image not found")
else:
    sx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    sx = cv2.convertScaleAbs(sx)
    sy = cv2.convertScaleAbs(sy)

    result = cv2.addWeighted(sx, 0.5, sy, 0.5, 0)

    original = cv2.resize(img, (300, 400))
    output = cv2.resize(result, (300, 400))
    combined = np.hstack((original, output))

    cv2.imshow("Original | Sobel Result", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
