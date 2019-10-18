import os
import numpy as np
from PIL import Image,ImageFilter
import matplotlib.pyplot as plt

def main():
    for root, dirs, files in os.walk(".\\Assignment1Images\\"):
        #print(files)
        i = 0
        imagesAsArray =np.zeros((20,200, 200, 3))
        for filename in files:
            #print(i)
            if filename.endswith(".jpg"):
                #print(filename)
                im = Image.open(root+filename)
                im = im.resize((200, 200), Image.ANTIALIAS)
                #print(im)
                img = np.array(im)
                #print(type(img))
                #print(img.shape)
                #imgplot = plt.imshow(img)
                #plt.show()
                imagesAsArray[i] = img
                i = i+1
    print(imagesAsArray)


if __name__ == '__main__':
    main()