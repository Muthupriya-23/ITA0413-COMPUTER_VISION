import cv2
import numpy as np

# Load image
img = cv2.imread(r"C:\Users\Priya\Downloads\blue.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define background color range (example: blue)
lower = np.array([90, 50, 50])
upper = np.array([130, 255, 255])

# Create background color mask
mask = cv2.inRange(hsv, lower, upper)

# Remove blue background pixels
result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

# Save output
cv2.imwrite(r"C:\Users\Priya\Downloads\background_subtraction.png", result)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Background Mask", mask)
cv2.imshow("Background Subtraction", result)

print("Background subtraction completed!")
print("Output saved as background_subtraction.png")

cv2.waitKey(0)
cv2.destroyAllWindows()
