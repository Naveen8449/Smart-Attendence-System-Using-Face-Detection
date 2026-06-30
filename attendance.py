import cv2
import face_recognition
import pickle
from datetime import datetime
import numpy as np

with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

cap = cv2.VideoCapture(0)

def markAttendance(name):
    with open("attendance.csv", "a") as f:
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        f.write(f"{name},{time}\n")

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb)
    encs = face_recognition.face_encodings(rgb, boxes)

    for enc, box in zip(encs, boxes):
        matches = face_recognition.compare_faces(data["encodings"], enc)
        name = "Unknown"

        if True in matches:
            matchIndex = matches.index(True)
            name = data["names"][matchIndex]
            markAttendance(name)

        y1,x2,y2,x1 = box
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.putText(frame,name,(x1,y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

    cv2.imshow("Attendance", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()