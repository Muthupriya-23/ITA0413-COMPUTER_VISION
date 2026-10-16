

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Priya\Downloads\pic.jpeg")

if img is None:
    print("Image not found")
else:
    rotated = cv2.rotate(
        img, cv2.ROTATE_90_COUNTERCLOCKWISE
    )

    original = cv2.resize(img, (300, 400))
    output = cv2.resize(rotated, (300, 400))
    combined = np.hstack((original, output))

    cv2.imshow("Original | 270 Degree Rotation", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


