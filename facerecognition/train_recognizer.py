import cv2 as cv
import numpy as np
import os

features = []
labels = []

cv2_base_dir = os.path.dirname(os.path.abspath(cv.__file__))
face_haar_model_path = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')

haar_cascade = cv.CascadeClassifier(face_haar_model_path)

# create the training set
for label, person in enumerate(os.listdir("train")):
    person_path = os.path.join("train", person)
    for img_path in os.listdir(person_path):
        img = cv.imread(os.path.join("train", person, img_path))
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
        
        for (x, y, w, h) in faces_rect:
            feature = gray[y:y+h, x:x+w]
            features.append(feature)
            labels.append(label)

features =np.array(features, dtype="object")        
labels = np.array(labels)
print("features shape", len(features))
print("labels shape", len(labels))

def train_recognizer(features, labels):
    recognizer =  cv.face.LBPHFaceRecognizer_create()
    recognizer.train(features, labels)

    recognizer.save("face_recognizer_model.yml")

train_recognizer(features, labels)
print("training done------")