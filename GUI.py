from tkinter import *
from tkinter.ttk import *
from PIL import Image
import os
from Steganography import *
from aes import *

def mainGUI():
    normalImages, encImages = 4, 0
    enc={}
    enc2={}
    window = Tk()
    window.title("CryptoPal")
    window.resizable(False, False)
    window.geometry('1400x700')
    winWidth = window.winfo_reqwidth()
    winHeight = window.winfo_reqheight()
    positionRight = int(window.winfo_screenwidth() / 2 - winWidth * 3.75)
    positionDown = int(window.winfo_screenheight() / 2 - winHeight * 2.04)
    window.geometry("+{}+{}".format(positionRight, positionDown))

    def beforeEncodeGuiMethod(imageNameToEncode):
        # Data to encrypt
        # destroy previous from frame
        for f in paneData.winfo_children():
            f.destroy()

        dataLabel = Label(paneData, text="Enter data to encrypt", font='Helvetica 10')
        dataLabel.pack(side=LEFT)
        dataText = Entry(paneData, width=66)
        dataText.pack(side=LEFT)

        for f in paneSave.winfo_children():
            f.destroy()
        nameLabel = Label(paneSave, text="Enter new image name with extension", font='Helvetica 10')
        nameLabel.pack(side=LEFT)
        nameText = Entry(paneSave, width=30)
        nameText.pack(side=LEFT)

        Button(paneSave, width=15, text="Encode",
                              command=lambda: encodeGuiMethod(imageNameToEncode,encrypt(
                                                              dataText.get(), 123),
                                                              nameText.get())).pack(side=LEFT, fill=X, padx=5)
        # Button(paneSave, width=15, text="Encode",
        #                       command=lambda: encodeGuiMethod(imageNameToEncode,
        #                                                       dataText.get(),
        #                                                       nameText.get())).pack(side=LEFT, fill=X, padx=5)

    paneLogo = Frame(window)
    panePassword = Frame(window)
    paneEncrypt = Frame(window)
    paneEncImages = Frame(window)
    paneData = Frame(window)
    paneSave = Frame(window)
    paneDecrypt = Frame(window)

    logo = PhotoImage(file=r"logo-removebg-preview.png", width=187, height=60)
    Label(paneLogo, image=logo).pack()

    # Password Attributes & positioning
    txtDecode = Entry(panePassword, width=30)
    txtDecode.config(show="*")
    txtDecode.pack(side=LEFT)
    buttonCommit = Button(panePassword, width=15, text="Enter Password")
    buttonCommit.pack(side=LEFT, fill = X, padx = 5)

    # Encode Attributes & positioning
    lblEncode = Label(paneEncrypt, text="Choose a photo to encrypt", font='Helvetica 12')
    lblEncode.pack(side = LEFT)

    # Encode Images Attributes & positioning + Image Button definitions
    for i in range(normalImages):
        enc["image{0}".format(i+1)] = [PhotoImage(file=r"image"+str(i+1)+".png", width=250,
                                                  height=140), "image{0}{1}".format(i+1, ".png")]
        Button(paneEncImages, image=enc["image"+str(i+1)][0],
                command= lambda i=i: beforeEncodeGuiMethod(enc["image"+str(i+1)][1])).pack(side = LEFT)


    # Decode Attributes & positioning
    # for i in range(encImages):
    #     enc2["out".format(i+1)] = [PhotoImage(file=r"image"+str(i+1)+".png", width=250,
    #                                               height=140), "image{0}{1}".format(i+1, ".png")]
    #     Button(paneEncImages, image=enc["image"+str(i+1)][0],
    #             command= lambda i=i: beforeEncodeGuiMethod(enc["image"+str(i+1)][1])).pack(side = LEFT)

    lblDecode = Label(paneDecrypt, text="Choose a photo to decrypt", font='Helvetica 12')
    lblDecode.pack(side = LEFT)

    paneLogo.pack(fill = BOTH)
    panePassword.pack()
    paneEncrypt.pack(fill = X, pady = 3)
    paneEncImages.pack(fill = X)
    paneData.pack(fill = X)
    paneSave.pack(fill = X)
    paneDecrypt.pack(fill = X, pady = 3)

    mainloop()

if __name__ == '__main__':
    mainGUI()
