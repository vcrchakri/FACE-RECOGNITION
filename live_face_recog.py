import cv2
from deepface import DeepFace
import os

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

KNOWN_FACES_DIR = "known_faces"

cap = cv2.VideoCapture(0)

print("Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]

        name = "Unknown"

        try:
            results = DeepFace.find(
                img_path=face_img,
                db_path=KNOWN_FACES_DIR,
                model_name="Facenet",
                enforce_detection=False
            )

            if len(results) > 0 and len(results[0]) > 0:
                identity = results[0].iloc[0]["identity"]
                name = os.path.basename(os.path.dirname(identity))

        except Exception:
            pass

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display name
        cv2.putText(
            frame,
            name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

    cv2.imshow("Live Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
