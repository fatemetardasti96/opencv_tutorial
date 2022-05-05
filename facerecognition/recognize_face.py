import cv2 as cv
import os

cv2_base_dir = os.path.dirname(os.path.abspath(cv.__file__))
face_haar_model_path = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')

haar_cascade = cv.CascadeClassifier(face_haar_model_path)
img_path = "/home/fateme/Documents/computer_vision/opencv_tutorial/facerecognition/val/madonna/2.jpg"

people = ["ben afflek", "elton john", "jerry seinfeld", "madonna", "mindy kaling"]

# load model
recognizer =  cv.face.LBPHFaceRecognizer_create()
recognizer.read("face_recognizer_model.yml")

# load a validation image
img = cv.imread(img_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# detect feature from validation
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    feature = gray[y:y+h, x:x+w]
    face_frame = cv.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)


# predict using the model
label, confidence = recognizer.predict(feature)
face_frame = cv.putText(face_frame, f"{people[label]}, {round(confidence, 1)}%", (20,20), cv.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
cv.imshow("face recognition", face_frame)

cv.waitKey(0)