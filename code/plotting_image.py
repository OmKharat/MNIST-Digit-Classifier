import numpy as np
import cv2

file = open("/home/omkharat/Desktop/IvLabs/DeepLearning/train.csv", "r")
img =file.readlines()
file.close()

values = img[2321].split(",")
print(values[0])
image = np.asfarray(values[1:]).reshape(28, 28)
large = cv2.resize(image, (280,280))
cv2.imshow("Image", large)
cv2.waitKey(0)
