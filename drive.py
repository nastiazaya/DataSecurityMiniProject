from Steganography import *
from tkinter import *
import os

def mainGUI():
    ## Initialize
    window = Tk()
    window.title("Welcome to KGB Decryption system")
    window.geometry('500x200')

    # must be here before decleration of the labels
    def retrieveTextInputFromEncodeLabel(textLabele):
        imageNameE = textLabele.get()
        encodeGuiMethod(imageNameE)

    ## must be here before decleration of the labels
    def retrieveTextInputFromDecodeLabel(textLabeld):
        imageNameD = textLabeld.get()
        print(decodeGuiMethod(imageNameD))

    # Encode Attributes & positioning
    lblEncode = Label(window)
    lblEncode.configure(text="Enter Image name to encode")
    lblEncode.grid(column=1, row=0)
    txtEncode = Entry(window, width=30)
    txtEncode.grid(column=2, row=0)
    buttonCommit = Button(window, text="Encode Image", command=lambda: retrieveTextInputFromEncodeLabel(txtEncode))
    buttonCommit.grid(column=3, row=0)

    # Decode Attributes & positioning
    lblDecode = Label(window)
    lblDecode.configure(text="Enter Image name to decode")
    lblDecode.grid(column=1, row=1)
    txtDecode = Entry(window, width=30)
    txtDecode.grid(column=2, row=1)
    buttonCommit = Button(window, text="Decode Image", command=lambda: retrieveTextInputFromDecodeLabel(txtDecode))
    buttonCommit.grid(column=3, row=1)

    window.mainloop() # DONT TOUCH OR REMOVE THAT LINE, this is the last line of the GUI

if __name__ == '__main__':

    mainGUI()