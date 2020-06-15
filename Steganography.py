import PIL.Image
from PIL import ImageTk # pip install Pillow
from tkinter import *
import os
from GUI import *

binaryData = []

def encodeImageMainMethod(copy, encodeData):
    width = copy.size[0]
    (x, y) = (0, 0)

    for p in modifyImage(copy.getdata(), encodeData):
        copy.putpixel((x, y), p)
        if (x == width - 1):
            y = y+1
            x = 0
        else:
            x = x+1

def convertDataToBinary(nonBinaryData):
    for index in nonBinaryData:
        binaryData.append(format(ord(index), '08b'))
    return binaryData

def modifyImage(imagePixels, data):
    listofdata = convertDataToBinary(data)
    dataimage = iter(imagePixels)

    for i in range(len(listofdata)):
        imagePixels = [value for value in dataimage.__next__()[:3] + dataimage.__next__()[:3] + dataimage.__next__()[:3]]

        for j in range(0, 8):
            if (listofdata[i][j] == '0') and (imagePixels[j] % 2 != 0):
                if (imagePixels[j] % 2 != 0):
                    imagePixels[j] -= 1
            elif (listofdata[i][j] == '1') and (imagePixels[j] % 2 == 0):
                imagePixels[j] -= 1

        if (i == len(listofdata) - 1):
            if (imagePixels[-1] % 2 == 0):
                imagePixels[-1] -= 1
        else:
            if (imagePixels[-1] % 2 != 0):
                imagePixels[-1] -= 1

        imagePixels = tuple(imagePixels)
        yield imagePixels[0:3]
        yield imagePixels[3:6]
        yield imagePixels[6:9]

def decodeGuiMethod(imageNameToDecode):
    image = PIL.Image.open(imageNameToDecode, 'r')
    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]
        string = ''

        for i in pixels[:8]:
            if (i % 2 != 0):
                string += '1'
            else:
                string += '0'

        data = data+chr(int(string, 2))
        if (pixels[-1] % 2 != 0):
            return data

def encodeGuiMethod(imageNameToEncode, textToEnconde, outPutImageName, path):
    copyImage = PIL.Image.open(imageNameToEncode, 'r').copy()
    encodeImageMainMethod(copyImage, textToEnconde)
    finalName = outPutImageName+"-out.png"
    path1 = path + "decryptedImages/"
    path2 = path
    copyImage.save(path1+finalName, str(finalName.split(".")[1].upper()))
    copyImage.save(path2+finalName, str(finalName.split(".")[1].upper()))