############     imported libraries    ############
import numpy as np

###########   loading the data    ###########

# we have to do this only once to create .csv file

mnist_train_x = "/home/omkharat/Desktop/IvLabs/DeepLearning/train-images.idx3-ubyte"
mnist_train_y = "/home/omkharat/Desktop/IvLabs/DeepLearning/train-labels.idx1-ubyte"
mnist_test_x = "/home/omkharat/Desktop/IvLabs/DeepLearning/t10k-images.idx3-ubyte"
mnist_test_y = "/home/omkharat/Desktop/IvLabs/DeepLearning/t10k-labels.idx1-ubyte"

def convert(image, label, file, n):

#######       opening the files
    
    image = open(image, "rb")
    label = open(label, "rb")
    csvfile = open(file, "w")

    image.read(16)
    label.read(8)
    images = []



#####         reading the file

    for i in range(n):
        img = [ord(label.read(1))]
        for j in range(28*28):
            img.append(ord(image.read(1)))
        images.append(img)



#####         writing to .csv file

    for img in images:
        csvfile.write(",".join(str(pix) for pix in img)+"\n")


#####         closing the files
    image.close()
    label.close()
    csvfile.close()

convert(mnist_train_x, mnist_train_y, "/home/omkharat/Desktop/IvLabs/DeepLearning/train.csv", 60000)
convert(mnist_test_x, mnist_test_y, "/home/omkharat/Desktop/IvLabs/DeepLearning/test.csv", 10000)