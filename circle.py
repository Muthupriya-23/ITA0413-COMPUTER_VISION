import cv2
import numpy as np
img = np.zeros((200, 200, 3), dtype=np.uint8)
cv2.circle(img, (100, 100), 50, (0, 0, 255), 3)
cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
