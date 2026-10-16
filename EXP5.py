
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(
    r"C:\Users\Priya\Downloads\pic.jpeg"
)

if img is None:
    print("Image not found")
else:
    colors = ("b", "g", "r")
    names = ("Blue", "Green", "Red")

    for i, color in enumerate(colors):
        hist = cv2.calcHist(
            [img], [i], None, [256], [0, 256]
        )

        plt.plot(hist, color=color, label=names[i])

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.legend()
    plt.show()
