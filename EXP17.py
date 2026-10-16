
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Priya\Downloads\pic.jpeg")

if img is None:
    print("Image not found")
else:
    watermark = img.copy()

    cv2.putText(
        watermark, "MY WATERMARK",
        (20, img.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        1, (255, 255, 255), 2
    )

    result = cv2.addWeighted(img, 0.7, watermark, 0.3, 0)

    original = cv2.resize(img, (300, 400))
    output = cv2.resize(result, (300, 400))
    combined = np.hstack((original, output))

    cv2.imwrite(
        r"C:\Users\Priya\Downloads\watermarked.jpg",
        result
    )

    cv2.imshow("Original | Watermarked Image", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
