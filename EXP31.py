import cv2

# Load image
img = cv2.imread(r"C:\Users\Priya\Downloads\pic.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold segmentation
threshold_value = 127
max_value = 255

ret, segmented = cv2.threshold(
    gray, threshold_value, max_value, cv2.THRESH_BINARY
)

# Display original and segmented images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Segmented Image", segmented)

print("Threshold value:", threshold_value)
print("Image segmentation completed!")

cv2.waitKey(0)
cv2.destroyAllWindows()
