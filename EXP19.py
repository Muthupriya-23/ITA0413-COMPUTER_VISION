
import cv2
import numpy as np

img = cv2.imread(
    r"C:\Users\Priya\Downloads\pic.jpeg", 0
)

if img is None:
    print("Image not found")
else:
    _, binary = cv2.threshold(
        img, 127, 255, cv2.THRESH_BINARY
    )

    kernel = np.ones((3, 3), np.uint8)
    result = cv2.erode(binary, kernel, iterations=1)

    original = cv2.resize(binary, (300, 400))
    output = cv2.resize(result, (300, 400))
    combined = np.hstack((original, output))

    cv2.imshow("Original | Erosion", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
