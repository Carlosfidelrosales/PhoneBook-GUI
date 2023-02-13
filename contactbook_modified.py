from tkinter import *
import csv
from tkinter import messagebox
import tkinter.font

dataContact = Tk()
dataContact.title("Contact Book")
dataContact.geometry("1300x375")
dataContact.resizable(False, False)

FRAME = Frame(dataContact, bg="blue", height=100, width=300)
imageFile = PhotoImage(file = "phonebook.png")
background_label = Label(dataContact, image=imageFile, anchor="center")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

contactList = []