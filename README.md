# Smart Attendance System Using Face Detection & Recognition

## 📌 Project Overview

Smart Attendance System is an AI-based attendance management system that uses **Face Detection and Face Recognition** technology to automatically mark attendance. The system identifies registered users through a camera and records their attendance along with date and time.

This project eliminates manual attendance work, reduces errors, and provides a secure and efficient attendance tracking solution.

---

## 🚀 Features

- Real-time face detection using webcam
- Face recognition of registered users
- Automatic attendance marking
- Stores attendance records with date and time
- Prevents duplicate attendance entries
- Easy user registration process
- AI-based automated attendance system

---

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Computer Vision:** OpenCV
- **Face Recognition:** Face Recognition Library
- **Database:** CSV / SQLite (according to implementation)
- **Machine Learning Concepts:** Face Encoding and Recognition

---

Smart-Attendance-System/
│
├── dataset/
│ └── Registered user face images
│
├── attendance.csv
│
├── encode_faces.py
│
├── attendance_system.py
│
├── requirements.txt
│
└── README.md



---

# ⚙️ Installation & Setup Guide

Follow these steps to run the project successfully.


## Step 1: Clone the Repository

Open terminal and run:


git clone https://github.com/your-username/Smart-Attendance-System.git

move into the project folder

cd Smart-Attendance-System




Step 2: Create Virtual Environment (Recommended)

Create environment:

python -m venv venv

Activate environment:

Windows:
venv\Scripts\activate
Linux/Mac:
source venv/bin/activate



Step 3: Install Required Libraries

Install all dependencies:

pip install -r requirements.txt

If requirements.txt is not available, install manually:

pip install opencv-python
pip install face-recognition
pip install numpy


👤 Step 4: Add User Face Images
Open the dataset folder.
Create a folder with the person's name.
Add clear face images of the person.

Example:

dataset/
   ├── Naveen/
       ├── image1.jpg
       ├── image2.jpg

Make sure:

Face should be clearly visible
Good lighting is recommended
Multiple images give better accuracy


🧠 Step 5: Generate Face Encodings

Run:

python encode_faces.py

This step converts face images into numerical face encodings used for recognition.

▶️ Step 6: Run Attendance System

Start the application:

python attendance_system.py

The webcam will open.

When a registered face is detected:

User name will be recognized
Attendance will be automatically marked
Date and time will be stored

📊 Attendance Output

Attendance file example:

Name        Date          Time

Naveen      30-06-2026    10:30 AM
User2       30-06-2026    10:35 AM

🔐 How It Works
User images are collected.
Face features are extracted using face encoding.
Webcam captures real-time faces.
System compares detected face with stored encodings.
If a match is found, attendance is recorded automatically.


🎯 Future Improvements
Web-based attendance dashboard
Cloud database integration
Mobile application support
Better accuracy using deep learning models
Multiple camera support

👨‍💻 Author

Your Name
somineni naveen

# 📂 Project Structure

