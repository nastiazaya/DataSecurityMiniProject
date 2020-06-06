import PIL.Image
from PIL import ImageTk # pip install Pillow
from tkinter import *
import os
from GUI import *

def convertDataToBinary(data):
    newd = []
    for i in data:
        # convert encoding data into 8-bit binary
        newd.append(format(ord(i), '08b'))
    return newd

# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):
    datalist = convertDataToBinary(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                if (pix[j] % 2 != 0):
                    pix[j] -= 1

            elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                pix[j] -= 1

        # Eigh^th pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means the
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                pix[-1] -= 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

# still need fixings
def encodeGuiMethod(imageNameToEncode, textToEnconde, outPutImageName):
    copyImage = PIL.Image.open(imageNameToEncode, 'r').copy()
    encode_enc(copyImage, textToEnconde)
    finalName = "out-"+outPutImageName+".png"
    path = "C:/Users/benja/Desktop/"
    copyImage.save(path+finalName, str(finalName.split(".")[1].upper()))


# still need fixings
def decodeGuiMethod(imageNameToDecode):
    # img = input("Enter image name(with extension): ")
    image = PIL.Image.open(imageNameToDecode, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]
        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data

# def mainGUI():
#     ## Initialize
#     window = Tk()
#     window.title("Welcome to KGB Decryption system")
#     window.geometry('500x200')
#
#     # must be here before decleration of the labels
#     def retrieveTextInputFromEncodeLabel(textLabele):
#         imageNameE = textLabele.get()
#         encodeGuiMethod(imageNameE)
#
#     ## must be here before decleration of the labels
#     def retrieveTextInputFromDecodeLabel(textLabeld):
#         imageNameD = textLabeld.get()
#         print(decodeGuiMethod(imageNameD))
#
#     # Encode Attributes & positioning
#     lblEncode = Label(window)
#     lblEncode.configure(text="Enter Image name to encode")
#     lblEncode.grid(column=1, row=0)
#     txtEncode = Entry(window, width=30)
#     txtEncode.grid(column=2, row=0)
#     buttonCommit = Button(window, text="Encode Image", command=lambda: retrieveTextInputFromEncodeLabel(txtEncode))
#     buttonCommit.grid(column=3, row=0)
#
#     # Decode Attributes & positioning
#     lblDecode = Label(window)
#     lblDecode.configure(text="Enter Image name to decode")
#     lblDecode.grid(column=1, row=1)
#     txtDecode = Entry(window, width=30)
#     txtDecode.grid(column=2, row=1)
#     buttonCommit = Button(window, text="Decode Image", command=lambda: retrieveTextInputFromDecodeLabel(txtDecode))
#     buttonCommit.grid(column=3, row=1)
#
#     window.mainloop() # DONT TOUCH OR REMOVE THAT LINE, this is the last line of the GUI

# if __name__ == '__main__':
#
#     mainGUI()

# Encode:
#     'H' is 72 is 01001000.
#                 (red, green, blue)
#     original:   (27, 64, 164), (248, 244, 194), (174, 246, 250)
#     new:        (26, 63, 164), (248, 243, 194), (174, 246, 250)
#
# Decode:
#     same until the last value is odd