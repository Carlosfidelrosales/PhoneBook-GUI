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