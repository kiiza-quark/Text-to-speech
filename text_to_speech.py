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

entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)

#function that does the real conversion
def speak():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('audio.mp3')
    playsound('audio.mp3')

def exit():
    root.destroy()

def reset():
    Msg.set("")

##buttons

Button(root, font='arial 16 bold', text = "SPEAK", command=speak, width='10').place(x=10,y=140)
Button(root, font='arial 16 bold', text="EXIT", width='4', command=exit, bg='Orangered1').place(x=145,y=140)
Button(root, font='arial 16 bold', text="RESET", width='10', command=reset).place(x=205,y=140)

root.mainloop()
