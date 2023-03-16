from tkinter import *
import random

window = Tk()

window.title("Lucky Friend Wheel")
window.geometry("500x500")

list = ["Evie","Lily","Chloe","Eilidh","May-Belle","Zoe","Anaya","Amelia","Eva","Harper","ϻοκshἰthα❤"]

def lucky():
    random_no = random.randint(0,10)
    print(list[random_no])

button = Button(window,text="Who is my Lucky Friend?",command=lucky)
button.place(relx=0.5,rely=0.5,anchor=CENTER)

window.mainloop()