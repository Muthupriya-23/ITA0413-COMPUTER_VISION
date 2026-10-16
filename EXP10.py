
import cv2

img = cv2.imread(
    r"C:\Users\Priya\Downloads\pic.jpeg"
)

if img is None:
    print("Image not found")
else:
    rotated = cv2.rotate(
        img, cv2.ROTATE_90_CLOCKWISE
    )

    cv2.imshow("Original Image", img)
    cv2.imshow("90 Degree Clockwise Rotation", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
