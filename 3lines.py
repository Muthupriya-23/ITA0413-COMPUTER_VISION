import cv2
import numpy as np
img = np.zeros((300, 300, 3), dtype=np.uint8)
cv2.line(img, (50, 50), (250, 50), (0, 0, 255), 3)
cv2.line(img, (50, 150), (250, 150), (0, 255, 0), 3)
cv2.line(img, (50, 250), (250, 250), (255, 0, 0), 3)
cv2.imshow("Three Lines", img)
