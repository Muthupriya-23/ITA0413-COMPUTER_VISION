import cv2
import numpy as np

# Load image
img = cv2.imread(r"C:\Users\Priya\Downloads\red.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define blue color range
lower = np.array([90, 50, 50])
upper = np.array([130, 255, 255])

# Create foreground mask
mask = cv2.inRange(hsv, lower, upper)

# Extract foreground color
result = cv2.bitwise_and(img, img, mask=mask)

# Save output
cv2.imwrite(
    r"C:\Users\Priya\Downloads\foreground_subtraction.png",
    result
)

# Display output
cv2.imshow("Original Image", img)
cv2.imshow("Foreground Mask", mask)
cv2.imshow("Foreground Subtraction", result)

print("Foreground subtraction completed!")
print("Output saved as foreground_subtraction.png")

cv2.waitKey(0)
cv2.destroyAllWindows()
