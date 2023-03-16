from tkinter import *
import random

window = Tk()
window.title("Lucky Friend Wheel")
window.geometry("400x400")

text_box = Entry(window)

label_1 = Label(window)
label_2 = Label(window)
label_3 = Label(window)

list = []

def add_name():
    friend_name = text_box.get()
    list.append(friend_name)
    label_1["text"] = "Your Friend List: " + str(list)


def luck():
    length = len(list)
    random_number = random.randint(0,length-1)

    label_2["text"] = random_number
    label_3["text"] = "Your Lucky Friend Is: "+str(list[random_number])


button_1 = Button(window,text="Add to the Friend List",command=add_name)
button_2 = Button(window,text="Who is your Lucky Friend?",command=luck)

text_box.place(relx=0.5,rely=0.2,anchor=CENTER)

button_1.place(relx=0.5,rely=0.3,anchor=CENTER)

label_1.place(relx=0.5,rely=0.4,anchor=CENTER)

button_2.place(relx=0.5,rely=0.5,anchor=CENTER)

label_2.place(relx=0.5,rely=0.6,anchor=CENTER)

label_3.place(relx=0.5,rely=0.7,anchor=CENTER)

window.mainloop()