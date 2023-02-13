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

def InterpetCSVFile():
    global header
    with open('StudentData.csv') as csvfile:
        csv_reader = csv.reader(csvfile,delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            contactList.append(row)	
    print(contactList)

def EditCSVFile(contactList):
    with open('StudentData.csv','w', newline='') as csv_file:
        writecsv = csv.writer(csv_file,delimiter=',')
        writecsv.writerow(header)
        for row in contactList:
            writecsv.writerow(row)

Desired_font = tkinter.font.Font(family="Times New Roman", size=15)
Desired_font2 = tkinter.font.Font(family="Verdana", size=20, weight="bold")

#1ST FRAME
Frame1 = LabelFrame(dataContact,text="")
Frame1.grid(padx=50,pady=15, row=1, column=1, sticky=N)

#innerframe
innerFrame_1 = Frame(Frame1)
innerFrame_1.grid(row=0,column=3,padx=15,pady=0)

#titlesection
title_page = Label(innerFrame_1,text="PHONE BOOK", font= Desired_font2)
title_page.grid(row=0,column=0,columnspan=2,padx=5,pady=5)
title_page_var = StringVar()