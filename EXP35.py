import cv2
import numpy as np

# Get text from user
text = input("Enter text to display: ")

# Create a white image
img = np.ones((400, 600, 3), dtype=np.uint8) * 255

# Display text on image
cv2.putText(
    img, text, (50, 200),
    cv2.FONT_HERSHEY_SIMPLEX, 1,
    (0, 0, 255), 2
)

# Save output image
cv2.imwrite(r"C:\Users\Priya\Downloads\text_output.png", img)

# Show output
cv2.imshow("Text on Image", img)

print("Text displayed successfully!")
print("Output saved as text_output.png")

cv2.waitKey(0)
cv2.destroyAllWindows()
