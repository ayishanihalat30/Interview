# import cv2
#
# # Load the pre-trained face detection classifier
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)  # Use 0 for the default camera, or specify the camera index if you have multiple cameras
#
# while True:
#     # Capture a frame from the webcam
#     ret, frame = cap.read()
#
#     if not ret:
#         break
#
#     # Convert the frame to grayscale for face detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Perform face detection
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#     # Draw bounding boxes around the detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Display the frame with bounding boxes
#     cv2.imshow("Face Detection", frame)
#
#     # Exit the loop when the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the webcam and close the OpenCV window
# cap.release()
# cv2.destroyAllWindows()


# Detecting faces,smile,and eye:
# import cv2
#
# # Load the pre-trained classifiers for face, eye, and smile detection
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)  # Use 0 for the default camera, or specify the camera index if you have multiple cameras
#
# while True:
#     # Capture a frame from the webcam
#     ret, frame = cap.read()
#
#     if not ret:
#         break
#
#     # Convert the frame to grayscale for face, eye, and smile detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Perform face detection
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#     # Draw bounding boxes around the detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#         # Region of interest (ROI) for eyes and smiles within the detected face
#         roi_gray = gray[y:y + h, x:x + w]
#         roi_color = frame[y:y + h, x:x + w]
#
#         # Perform eye detection within the face region
#         eyes = eye_cascade.detectMultiScale(roi_gray)
#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
#
#         # Perform smile detection within the face region
#         smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))
#         for (sx, sy, sw, sh) in smiles:
#             cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
#
#     # Display the frame with bounding boxes
#     cv2.imshow("Object Detection", frame)
#
#     # Exit the loop when the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the webcam and close the OpenCV window
# cap.release()
# cv2.destroyAllWindows()
#  Experiment with different parameters for the detectMultiScale function to fine-tune
# the detection sensitivity.

import cv2

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Experiment with different parameters for detectMultiScale
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,  # Adjust this value (e.g., 1.1, 1.2, 1.3, etc.)
        minNeighbors=5,   # Adjust this value (e.g., 3, 5, 10, etc.)
        minSize=(30, 30)  # Adjust this value (e.g., (20, 20), (30, 30), etc.)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

