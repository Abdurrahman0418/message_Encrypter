from tkinter import *
from tkinter import messagebox
import base64
import os

#decryptFunction
def decrypt():
    #get the code from the text box
    password=code.get()

    if password=="1234":
        #backgroundToAnotherScreenForWatchTheEncryptText
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        #ASCII Converter
        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        #showTheEncryptedTextOnScreen2
        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        #insertTheENDAndDecryptInToText2
        text2.insert(END,decrypt)

    #showAlertWhenCodeTextboxIsEmpty
    elif password=="":
        messagebox.showerror("encryption","Input Password")

    #showAlertWhenCodeIsWrong
    elif password!="1234":
        messagebox.showerror("encryption","Invalid Password")

#encryptFunction
def encrypt():
    #get the code from the text box
    password=code.get()

    if password=="1234":
        #backgroundToAnotherScreenForWatchTheEncryptText
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        #ASCII Converter
        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        #showTheEncryptedTextOnScreen1
        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        #insertTheENDAndEncryptInToText2
        text2.insert(END,encrypt)

    #showAlertWhenCodeTextboxIsEmpty
    elif password=="":
        messagebox.showerror("encryption","Input Password")

    #showAlertWhenCodeIsWrong
    elif password!="1234":
        messagebox.showerror("encryption","Invalid Password")



#GUI Screen Edit
def main_screen():

    global screen
    global code
    global text1

    #screenBackgroundDisplay
    screen=Tk()
    screen.geometry("375x398")

    #icon
    image_icon=PhotoImage(file="keys.png")
    screen.iconphoto(False,image_icon)
    screen.title("PctApp")

    #resetFunction
    def reset():
        code.set("")
        text1.delete(1.0,END)

    #Lable
    Label(text="Enter text for encryption and decryption",fg="black",font=("calibri",13)).place(x=10,y=10)
    #TextboxForText
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    #Lable
    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calibri",13)).place(x=10,y=170)

    #TextboxForKey
    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    #buttonForEncrypt
    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    #buttonForDecrypt
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    #buttonForReset
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)


    screen.mainloop()

main_screen()