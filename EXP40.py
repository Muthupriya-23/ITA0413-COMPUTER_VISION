import cv2
import pytesseract

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Load video
video = cv2.VideoCapture(
    r"C:\Users\Priya\Downloads\video.mp4"
)

if not video.isOpened():
    print("Error: Video not found!")
    exit()

print("Extracted Text:")

frame_count = 0
all_text = []

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Process every 30th frame
    if frame_count % 30 == 0:

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Improve text visibility
        gray = cv2.threshold(
            gray, 0, 255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        # Extract text from frame
        text = pytesseract.image_to_string(gray)

        if text.strip():
            print("Frame", frame_count)
            print(text.strip())
            all_text.append(text.strip())

        # Display video frame
        cv2.imshow("Video Text Extraction", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    frame_count += 1

# Release resources
video.release()
cv2.destroyAllWindows()

# Save extracted text
with open(
    r"C:\Users\Priya\Downloads\extracted_text.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("\n\n".join(all_text))

print("Text extraction completed!")
print("Output saved as extracted_text.txt")
