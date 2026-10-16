
import cv2

cap = cv2.VideoCapture(
    r"C:\Users\Priya\Downloads\video.mp4"
)

if not cap.isOpened():
    print("Video not found")
else:
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    if len(frames) == 0:
        print("No frames found")
    else:
        h, w = frames[0].shape[:2]

        out = cv2.VideoWriter(
            r"C:\Users\Priya\Downloads\reverse.mp4",
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps if fps > 0 else 25,
            (w, h)
        )

        for frame in reversed(frames):
            out.write(frame)

        out.release()
        print("Reverse video saved successfully")
