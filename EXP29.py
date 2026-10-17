import cv2

# Load image
img = cv2.imread(r"C:\Users\Priya\Downloads\eyes.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load eye detection classifier
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

if eye_cascade.empty():
    print("Error: Eye detector not found!")
    exit()

# Detect eyes
eyes = eye_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20)
)

# Draw rectangles around eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print("Number of eyes detected:", len(eyes))

# Display output
cv2.imshow("Eye Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
