
import cv2

img = cv2.imread(r"C:\Users\Priya\Downloads\watch.jpg")

if img is None:
    print("Watch image not found")
else:
    h, w = img.shape[:2]

    # Select watch as template
    template = img[20:180, 20:180].copy()

    th, tw = template.shape[:2]

    result = cv2.matchTemplate(
        img, template, cv2.TM_CCOEFF_NORMED
    )

    _, score, _, location = cv2.minMaxLoc(result)

    x, y = location

    cv2.rectangle(
        img, (x, y), (x + tw, y + th),
        (0, 255, 0), 2
    )

    print("Matching score:", score)
    print("Watch template matching completed")

    cv2.imshow("Watch Recognition", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
