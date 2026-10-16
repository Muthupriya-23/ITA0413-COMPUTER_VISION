
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Priya\Downloads\pic.jpeg")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.cornerHarris(gray, 2, 3, 0.04)
    corners = cv2.dilate(corners, None)

    result = img.copy()
    result[corners > 0.01 * corners.max()] = [0, 0, 255]

    original = cv2.resize(img, (300, 400))
    output = cv2.resize(result, (300, 400))
    combined = np.hstack((original, output))

    cv2.imshow("Original | Harris Corners", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
