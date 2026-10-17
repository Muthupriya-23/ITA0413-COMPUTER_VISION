import cv2

# Load image
img = cv2.imread(r"C:\Users\Priya\Downloads\smile.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load smile detector
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

if face_cascade.empty() or smile_cascade.empty():
    print("Error: Detection file not found!")
    exit()

# Detect faces
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

count = 0

# Detect smiles inside each face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    face_gray = gray[y:y+h, x:x+w]
    face_color = img[y:y+h, x:x+w]

    smiles = smile_cascade.detectMultiScale(
        face_gray,
        scaleFactor=1.7,
        minNeighbors=20,
        minSize=(20, 20)
    )

    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(
            face_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2
        )
        count += 1

print("Number of smiles detected:", count)

# Display output
cv2.imshow("Smile Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
