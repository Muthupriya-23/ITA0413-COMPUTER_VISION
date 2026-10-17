import cv2

# Load image
img = cv2.imread(r"C:\Users\Priya\Downloads\faces.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    print("Error: Face detector not found!")
    exit()

# Detect faces
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display face count
count = len(faces)
print("Number of faces detected:", count)

cv2.putText(
    img, "Faces: " + str(count), (20, 35),
    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
)

# Save and display output
cv2.imwrite(r"C:\Users\Priya\Downloads\face_count.png", img)
cv2.imshow("Face Counting", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
