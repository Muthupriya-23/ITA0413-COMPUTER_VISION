
import cv2

cap = cv2.VideoCapture(
    r"C:\Users\Priya\Downloads\video.mp4"
)

if not cap.isOpened():
    print("Video not found")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Slow Motion", frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
