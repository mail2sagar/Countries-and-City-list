from tkinter import *
import random

window = Tk()
window.title("Lucky Friend Wheel")
window.geometry("500x500")

text_box1 = Entry(window)
text_box2 = Entry(window)

btn1 = Button(window,text="Display Country And City Name")
btn2 = Button(window,text="Display Country And City Name Randomly")

lb1 = Label(window)
lb2 = Label(window)
lb3 = Label(window)
lb4 = Label(window)

list1 = []
list2 = []

def add_country():
    country_name = text_box1.get()
    list1.append(country_name)
    lb1["text"] = "Country Name: " + str(list1)

    city_name = text_box1.get()
    list1.append(city_name)
    lb2["text"] = "City Name: " + str(list2)

def random_cc():
    length = len(list1)
    random_number = random.randint(0,length-1)

    lb2["text"] = "Country Name: "+str(list1)
    lb3["text"] = "City Name: "+str(list2)

    length = len(list2)
    random_number = random.randint(0,length-1)

    lb3["text"] = "Random Country: "+str(list1)
    lb4["text"] = "Random City: "+str(list2)


text_box1.place(relx=0.5,rely=0.1,anchor=CENTER)
text_box2.place(relx=0.5,rely=0.2,anchor=CENTER)

btn1.place(relx=0.5,rely=0.3,anchor=CENTER)

lb1.place(relx=0.5,rely=0.4,anchor=CENTER)
lb2.place(relx=0.5,rely=0.5,anchor=CENTER)

btn2.place(relx=0.5,rely=0.6,anchor=CENTER)

lb3.place(relx=0.5,rely=0.7,anchor=CENTER)
lb4.place(relx=0.5,rely=0.8,anchor=CENTER)


window.mainloop()