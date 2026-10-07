import cv2
import numpy as np
img = np.zeros((250, 250, 3), dtype=np.uint8)
cv2.line(img, (50, 125), (200, 125), (0, 255, 0), 3)
cv2.imshow("Green Straight Line", img)
