
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(
    r"C:\Users\Priya\Downloads\pic.jpeg",
    0
)

if img is None:
    print("Image not found")
else:
    equalized = cv2.equalizeHist(img)

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(equalized, cmap="gray")
    plt.title("Histogram Equalized")
    plt.axis("off")

    plt.show()
