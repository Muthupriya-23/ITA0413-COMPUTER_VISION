
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Priya\Downloads\pic.jpeg")

if img is None:
    print("Image not found")
else:
    h, w = img.shape[:2]

    src = np.float32([
        [0, 0], [w-1, 0],
        [0, h-1], [w-1, h-1]
    ])

    dst = np.float32([
        [50, 50], [w-50, 0],
        [0, h-50], [w-1, h-1]
    ])

    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, matrix, (w, h))

    original = cv2.resize(img, (300, 400))
    output = cv2.resize(result, (300, 400))
    combined = np.hstack((original, output))

    cv2.imshow("Original | Perspective", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
