import cv2
import numpy as np

# Create a white image
img = np.ones((400, 600, 3), dtype=np.uint8) * 255

# Draw a rectangle
cv2.rectangle(img, (150, 100), (450, 300), (0, 0, 255), 3)

# Save output image
cv2.imwrite(r"C:\Users\Priya\Downloads\rectangle.png", img)

# Display output
cv2.imshow("Rectangle", img)

print("Rectangle created successfully!")
print("Output saved as rectangle.png")

cv2.waitKey(0)
cv2.destroyAllWindows()
