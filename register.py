import cv2
import os

name = input("Enter Student Name: ")

path = "dataset"
if not os.path.exists(path):
    os.makedirs(path)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Register", frame)

    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite(f"{path}/{name}.jpg", frame)
        print("Student Registered")
        break

cap.release()
cv2.destroyAllWindows()