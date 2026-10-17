import cv2

# Load video
video = cv2.VideoCapture(
    r"C:\Users\Priya\Downloads\vehicle.mp4"
)

if not video.isOpened():
    print("Error: Video not found!")
    exit()

# Read all video frames
frames = []

while True:
    ret, frame = video.read()

    if not ret:
        break

    frames.append(frame)

video.release()

if len(frames) == 0:
    print("Error: No frames found!")
    exit()

print("Playing video in reverse slow motion...")

# Play frames in reverse order
for frame in reversed(frames):
    cv2.imshow("Reverse Slow Motion Video", frame)

    # 150 milliseconds delay for slow motion
    if cv2.waitKey(150) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
print("Video playback completed!")
