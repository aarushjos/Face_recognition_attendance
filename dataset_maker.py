import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('enter user id (eg. 1,2,3,4): ')

print("\nInitializing face capture. Look at the camera and wait ...")
#count of photos/samples taken
count = 0

while(True):

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    instruction = ""
    if count < 30:
        instruction = "Normal - Look Straight"
    elif 30 <= count < 60:
        instruction = "Move Closer"
    elif 60 <= count < 90:
        instruction = "Move Back"
    else:
        instruction = "Done"

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        cv2.imwrite(f"dataset/User.{face_id}.{count}.jpg", gray[y:y + h, x:x + w])#writing the file in dataset folder of user's samples

    # Display instructions on screen
    cv2.putText(img, instruction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) #telling the user to move forward or back for better training of the model

    cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff #ESC to exit
    if k == 27:
        break
    elif count >= 100:
        break

print("\nExiting Program....")
cam.release()
cv2.destroyAllWindows()


