from tkinter import *
from tkinter.ttk import *
from PIL import Image
import os
from Steganography import *
from aes import *
from tkinter import filedialog

path = ''

def mainGUI():
    enc={}
    dec={}

    window = Tk()
    window.title("CryptoPal")
    window.resizable(False, False)
    window.geometry('1280x700')
    winWidth = window.winfo_reqwidth()
    winHeight = window.winfo_reqheight()
    positionRight = int(window.winfo_screenwidth() / 2 - winWidth * 3.75)
    positionDown = int(window.winfo_screenheight() / 2 - winHeight * 2.04)
    window.geometry("+{}+{}".format(positionRight, positionDown))

    def getPath():
        path = filedialog.askdirectory()

    def updatePaneDecImages():
        # Decode Attributes & positioning
        for f in paneDecImages.winfo_children():
            f.destroy()

        filelistDecrypted = os.listdir(path + 'decryptedImages/')
        for fichier in filelistDecrypted[:]:
            if not (fichier.endswith("out.png")):
                filelistDecrypted.remove(fichier)

        for i in range(len(filelistDecrypted)):
            dec["out{0}".format(i + 1)] = [PhotoImage(file=filelistDecrypted[i], width=250, height=140),
                                           filelistDecrypted[i]]
            Button(paneDecImages, image=dec["out" + str(i + 1)][0],
                   command=lambda i=i: beforeDecodeGuiMethod(dec["out" + str(i + 1)][1])).pack(side=LEFT)

    def decodeUpdate(imageNameToEncode, txt, password):
        encodeGuiMethod(imageNameToEncode, txt, password, path)
        updatePaneDecImages()

    def beforeEncodeGuiMethod(imageNameToEncode):
        # Data to encrypt
        # destroy previous from frame
        for f in paneData.winfo_children():
            f.destroy()

        dataLabel = Label(paneData, text="Enter Data to Encrypt", font='Helvetica 10')
        dataLabel.pack(side=LEFT)
        dataText = Entry(paneData, width=66)
        dataText.pack(side=LEFT)

        for f in panePassword.winfo_children():
            f.destroy()

        # Password Attributes & positioning
        nameLabel = Label(panePassword, text="Enter UNIQUE Password", font='Helvetica 10')
        nameLabel.pack(side=LEFT)
        txtPass = Entry(panePassword, width=30)
        txtPass.config(show="*")
        txtPass.pack(side=LEFT)

        for f in paneSave.winfo_children():
            f.destroy()
        nameLabel = Label(paneSave, text="Enter New Image Name", font='Helvetica 10')
        nameLabel.pack(side=LEFT)
        nameText = Entry(paneSave, width=30)
        nameText.pack(side=LEFT)

        for f in paneFinish.winfo_children():
            f.destroy()

        Button(paneFinish, width=15, text="Finish & Encode!",
                              command=lambda: decodeUpdate(imageNameToEncode, encrypt(dataText.get(), txtPass.get()),
                                                           nameText.get())).pack(side=LEFT, fill=X, padx=5)
        updatePaneDecImages()

    def displayDecryptedData(imagePassword, imageName):
        for f in paneDecData.winfo_children():
            f.destroy()
        lblDecode = Label(paneDecData, text=decrypt(decodeGuiMethod(imageName), imagePassword), font='Helvetica 12')
        lblDecode.pack(side=LEFT)

    def beforeDecodeGuiMethod(imageName):
        for f in panePassDec.winfo_children():
            f.destroy()

        passLabel = Label(panePassDec, text="Enter Your UNIQUE Password", font='Helvetica 10')
        passLabel.pack(side=LEFT)
        passText = Entry(panePassDec, width=30)
        passText.config(show="*")
        passText.pack(side=LEFT)

        Button(panePassDec, width=15, text="Enter & Decrypt!",
                              command=lambda: displayDecryptedData(passText.get(), imageName)).pack(side=LEFT, fill=X, padx=5)

    paneLogo = Frame(window)
    panePassword = Frame(window)
    paneEncrypt = Frame(window)
    paneEncImages = Frame(window)
    paneData = Frame(window)
    paneSave = Frame(window)
    paneFinish = Frame(window)
    paneDecrypt = Frame(window)
    paneDecImages = Frame(window)
    panePassDec = Frame(window)
    paneDecData = Frame(window)

    logo = PhotoImage(file=r"logo-removebg-preview.png", width=187, height=60)
    Button(paneLogo, image=logo, command = lambda: getPath()).pack()

    # Encode Attributes & positioning
    lblEncode = Label(paneEncrypt, text="Choose a photo to encrypt", font='Helvetica 12')
    lblEncode.pack(side = LEFT)

    # Encode Images Attributes & positioning + Image Button definitions
    filelist = os.listdir(path + 'normalImages/')
    for fichier in filelist[:]:  # filelist[:] makes a copy of filelist.
        if not (fichier.endswith(".png")):
            filelist.remove(fichier)

    for i in range(len(filelist)):
        # ima = PIL.Image.open(filelist[i])
        enc["image{0}".format(i+1)] = [PhotoImage(file=filelist[i], width=250, height=140), filelist[i]]
        Button(paneEncImages, image=enc["image"+str(i+1)][0],
                command= lambda i=i: beforeEncodeGuiMethod(enc["image"+str(i+1)][1])).pack(side = LEFT)

    # Decode Attributes & positioning
    filelistDecrypted = os.listdir(path + 'decryptedImages/')
    for fichier in filelistDecrypted[:]:  # filelist[:] makes a copy of filelist.
        if not (fichier.endswith("out.png")):
            filelistDecrypted.remove(fichier)

    for i in range(len(filelistDecrypted)):
        dec["out{0}".format(i + 1)] = [PhotoImage(file=filelistDecrypted[i], width=250, height=140),
                                       filelistDecrypted[i]]
        Button(paneDecImages, image=dec["out" + str(i + 1)][0],
               command=lambda i=i: beforeDecodeGuiMethod(dec["out" + str(i + 1)][1])).pack(side=LEFT)

    lblDecode = Label(paneDecrypt, text="Choose a photo to decrypt", font='Helvetica 12')
    lblDecode.pack(side = LEFT)


    paneLogo.pack(fill = BOTH)
    paneEncrypt.pack(fill = X, pady = 3)
    paneEncImages.pack(fill = X)
    paneData.pack(fill = X)
    panePassword.pack(fill = X)
    paneSave.pack(fill = X)
    paneFinish.pack(fill = X)
    paneDecrypt.pack(fill = X, pady = 3)
    paneDecImages.pack(fill = X)
    panePassDec.pack(fill = X, pady = 3)
    paneDecData.pack(fill = X, pady = 3)


    mainloop()

if __name__ == '__main__':
    mainGUI()
