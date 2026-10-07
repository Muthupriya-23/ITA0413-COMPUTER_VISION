import cv2
import numpy as np
img = np.zeros((200, 200, 3), dtype=np.uint8)
cv2.rectangle(img, (40, 40), (160, 160), (0, 255, 0), 3)
cv2.imshow("Rectangle", img)
