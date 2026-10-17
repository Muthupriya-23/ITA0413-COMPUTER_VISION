import cv2

# Load video
video = cv2.VideoCapture(
    r"C:\Users\Priya\Downloads\video.mp4"
)

if not video.isOpened():
    print("Error: Video not found!")
    exit()

# Background subtraction
back_sub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Detect moving objects
    mask = back_sub.apply(frame)

    # Remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Find object contours
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    count = 0

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 1500:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame, (x, y), (x + w, y + h), (0, 255, 0), 2
            )

            count += 1

    cv2.putText(
        frame, "Moving Objects: " + str(count),
        (20, 35), cv2.FONT_HERSHEY_SIMPLEX,
        0.8, (0, 0, 255), 2
    )

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
