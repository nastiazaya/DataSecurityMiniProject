import PIL.Image
from PIL import ImageTk # pip install Pillow
from tkinter import *
import os
from GUI import *

def convertDataToBinary(data):
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

def modPix(imagePixels, data):
    datalist = convertDataToBinary(data)
    lendata = len(datalist)
    imdata = iter(imagePixels)

    for i in range(lendata):

        imagePixels = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]

        for j in range(0, 8):
            if (datalist[i][j] == '0') and (imagePixels[j] % 2 != 0):

                if (imagePixels[j] % 2 != 0):
                    imagePixels[j] -= 1

            elif (datalist[i][j] == '1') and (imagePixels[j] % 2 == 0):
                imagePixels[j] -= 1

        if (i == lendata - 1):
            if (imagePixels[-1] % 2 == 0):
                imagePixels[-1] -= 1
        else:
            if (imagePixels[-1] % 2 != 0):
                imagePixels[-1] -= 1

        imagePixels = tuple(imagePixels)
        yield imagePixels[0:3]
        yield imagePixels[3:6]
        yield imagePixels[6:9]


def encodeImageMainMethod(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

# still need fixings
def encodeGuiMethod(imageNameToEncode, textToEnconde, outPutImageName, path):
    copyImage = PIL.Image.open(imageNameToEncode, 'r').copy()
    encodeImageMainMethod(copyImage, textToEnconde)
    finalName = outPutImageName+"-out.png"
    path1 = path + "decryptedImages/"
    path2 = path
    copyImage.save(path1+finalName, str(finalName.split(".")[1].upper()))
    copyImage.save(path2+finalName, str(finalName.split(".")[1].upper()))

# still need fixings
def decodeGuiMethod(imageNameToDecode):
    image = PIL.Image.open(imageNameToDecode, 'r')
    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data