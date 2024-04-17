import cv2
import matplotlib.pyplot as plt


imagePath="./2.jpg"

casePath="haarcascade_frontalface_default.xml"

faceCascade= cv2.CascadeClassifier(casePath)

image = cv2.imread(imagePath)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(RGB_image)


plt.show()

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minSize = (30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces !".format(len(faces)))

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)    

RGB_image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(RGB_image)

plt.show()


