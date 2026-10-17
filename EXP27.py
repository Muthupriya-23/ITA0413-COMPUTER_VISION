import cv2

# Load the image
img = cv2.imread(r"C:\Users\Priya\Downloads\face.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade face detector
cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if cascade.empty():
    print("Error: Face detector could not be loaded!")
    exit()

# Detect faces
faces = cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the result
print("Number of faces detected:", len(faces))

cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
