#import neccessary modules

from tkinter import *
from gtts import gTTS
from playsound import playsound

#initialising window

root = Tk()
root.geometry("350x300")
root.configure(bg='lightblue')
root.title("Speech to text by kizzah")

Label(root, text="KIZZAH'S TEXT TO SPEECH", font="arial 32 bold", bg='pink').pack()
Label(text="Kiiza quark", font='arial 22 bold', bg='pink', width='20').pack(side='bottom')

Msg = StringVar()
Label(root, text="Enter what i should speak", font = 'arial 15 bold', bg='white smoke').place(x=20,y=60)


