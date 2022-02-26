import string
import random
from tkinter import *
# first install pyperclip with "pip install pyperclip"
import pyperclip as pc

win = Tk()
win.geometry("200x200")
win.resizable(False, False)



pas = StringVar()

# ======== Backend =============

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def geneartor():
    the_len = int(e1.get())



    password = []

    random.shuffle(characters)

    for item in range(the_len):
        password.append(random.choice(characters))

    random.shuffle(password)

    pas.set(password)


def cop():
    string_pass = str(e2.get())
    pc.copy(string_pass)
# ============= Frant ===========

la = Label(win, text='len :')
la.place(relx=0.0, rely=0.0, anchor=NW)

e1 = Entry(win)
e1.place(relx=0.2, rely=0.0, anchor=NW)


# === creat ===

b1 = Button(win, text='Creat', width=10, command=geneartor)
b1.place(relx=0.3, rely=0.1, anchor=NW)


# === Entry_password ===

e2 = Entry(win, textvariable=pas)
e2.place(relx=0.2, rely=0.3, anchor=NW)

# === Copy ===
b2 = Button(win, text='Copy', width=10, command=cop)
b2.place(relx=0.3, rely=0.4, anchor=NW)





# geneartor()


mainloop()


