import cv2
import face_recognition
from matplotlib import pyplot as plt


webcamCapture = cv2.VideoCapture(0)

if not webcamCapture.isOpened():
    raise Exception("Could not open video device")

person1 = face_recognition.load_image_file("/home/buzun/Desktop/CODE/task/knownPersons/batuhan.jpg")
person1Encoding = face_recognition.face_encodings(person1)[0]


knownPersons = [person1]
knownPersonsNames = ["Batuhan"]


def takePhoto(frame):

    FrameRGB = frame[:, :, ::-1]
    plt.imshow(FrameRGB)
    photoName = input("Kişi Adı : ")
    plt.imsave("/home/buzun/Desktop/CODE/task/knownPersons/" + photoName + ".jpg", FrameRGB)


print("\nPress 'd' for take photo.")
print("\nPress 'ESC' for exit.")
while True:
    ret, frame = webcamCapture.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow("WebCam Frame", frame)
    if cv2.waitKey(1) == ord("s"):
        takePhoto(frame)
    elif cv2.waitKey(1) == ord("q"):
        break
        cv2.destroyAllWindows()
