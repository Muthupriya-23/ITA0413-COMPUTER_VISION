import cv2
import numpy as np

# Get image size from user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Create white image
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Box size
box = min(width, height) // 5

# Draw colored boxes at four corners
cv2.rectangle(img, (0, 0), (box, box), (0, 0, 0), -1)             # Black
cv2.rectangle(img, (width-box, 0), (width-1, box), (255, 0, 0), -1)  # Blue
cv2.rectangle(img, (0, height-box), (box, height-1), (0, 255, 0), -1)  # Green
cv2.rectangle(img, (width-box, height-box),
              (width-1, height-1), (0, 0, 255), -1)              # Red

# Display image
cv2.imshow("White Image with Colored Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
