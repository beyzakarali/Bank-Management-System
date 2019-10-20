import cv2
import face_recognition
from matplotlib import pyplot as plt
import os


def FaceDatasetsReading():

    knownPersonsEncoding = []
    knownPersonsNames = []

    os.chdir("/home/buzun/Desktop/CODE/task/knownPersons/")
    print(os.listdir(os.getcwd()))
    knownPersonsPhotos = os.listdir(os.getcwd())

    for i in range(len(knownPersonsPhotos)-1):
        person = face_recognition.load_image_file(
            "/home/buzun/Desktop/CODE/task/knownPersons/" + knownPersonsPhotos[i])
        personEncoding = face_recognition.face_encodings(person)[0]
        knownPersonsEncoding.append(personEncoding)
        knownPersonsNames.append(
        knownPersonsPhotos[i][0:len(knownPersonsPhotos[0])-4])


def TakePhoto(frame):

    FrameRGB = frame[:, :, ::-1]
    plt.imshow(FrameRGB)
    photoName = input("Kişi Adı : ")
    plt.imsave("/home/buzun/Desktop/CODE/task/knownPersons/" +
               photoName + ".jpg", FrameRGB)





webcamCapture = cv2.VideoCapture(0)

if not webcamCapture.isOpened():
    raise Exception("Could not open video device")


FaceDatasetsReading()

print("\nPress 's' for take photo.")
print("\nPress 'q' for exit.")
while True:
    ret, frame = webcamCapture.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow("WebCam Frame", frame)

    if cv2.waitKey(1) == ord("s"):
        TakePhoto(frame)
    elif cv2.waitKey(1) & 0xFF == ord("q"):
        break
        cv2.destroyAllWindows()
