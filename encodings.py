import face_recognition
import cv2
import os
import pickle

path = "dataset"
images = []
names = []

for file in os.listdir(path):
    img = cv2.imread(f"{path}/{file}")
    images.append(img)
    names.append(os.path.splitext(file)[0])

encodings = []

for img in images:
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    enc = face_recognition.face_encodings(rgb)[0]
    encodings.append(enc)

data = {"encodings": encodings, "names": names}

with open("encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("Training Completed")