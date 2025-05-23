import cv2
from datetime import date
from create_csv import data_frame,student_list
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
def add_attendance(name):
    today = date.today().strftime("%d-%m-%Y")
    if today not in data_frame.columns:
        data_frame[today]='A' #mark everyone absent
    #mark the given student present
    data_frame.loc[data_frame['Students']==name,today]='P'
    data_frame.to_csv("Attendance_Records.csv", index=False) #update the csv



#iniciate id counter
id = 0
# names that are related to id entered during dataset making
names = ['None']+student_list

#start video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) #cam width
cam.set(4, 480) #cam height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:

    ret, img =cam.read() #read the image (video from webcam)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #turn it to grayscale cause LBPH works on grayscale

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Lower the confidence more the surety that the face matches
        if (confidence < 100):
            name_of_person = names[id] #grab the name using the id
            confidence = "  {0}%".format(round(100 - confidence))
            add_attendance(name_of_person)
            cv2.putText(img,f"Attendance of {name_of_person} marked!",(x-35,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,0.75,(255,255,255),2)
        else:
            name_of_person = "random person"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(name_of_person), (x+5,y-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,255,0), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255,255,255), 1)

    cv2.imshow('camera',img)

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("Exiting Program...\n")
cam.release()
cv2.destroyAllWindows()
