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

#firstnamelabel
Label_FirstName = Label(innerFrame_1,text="First Name", font= Desired_font)
Label_FirstName.grid(row=1,column=0,padx=5,pady=20)
FirstName_var = StringVar()
FirstName = Entry(innerFrame_1,width=50, textvariable=FirstName_var, background="yellow")
FirstName.grid(row=1,column=1,padx=5,pady=20)

#lastnamelabel
Label_LastName= Label(innerFrame_1,text="Last Name", font= Desired_font)
Label_LastName.grid(row=2,column=0,padx=5,pady=20)
LastName_var= StringVar()
LastName = Entry(innerFrame_1,width=50,textvariable=LastName_var, background="yellow")
LastName.grid(row=2,column=1,padx=5,pady=20)

#contactnumlabel
Label_ContactNumb= Label(innerFrame_1,text="Contact Number", font= Desired_font)
Label_ContactNumb.grid(row=3,column=0,padx=5,pady=20)
ContactNumb_var = StringVar()
ContactNumb = Entry(innerFrame_1,width=50,textvariable=ContactNumb_var, background="yellow")
ContactNumb.grid(row=3,column=1,padx=5,pady=20)

#emaillabel
Label_Email= Label(innerFrame_1,text="Email Address", font= Desired_font)
Label_Email.grid(row=4,column=0,padx=5,pady=20)
Email_var = StringVar()
Email = Entry(innerFrame_1,width=50,textvariable=Email_var, background="yellow")
Email.grid(row=4,column=1,padx=5,pady=20)

#2ND FRAME
Frame2 = Frame(dataContact)
Frame2.grid(row=1,column=3,padx=5,pady=20,sticky=N)

#addbutton
Include_DataButton = Button(Frame2,text="Add",width=20,height=3,bg="#6B69D6",fg="#FFFFFF",command="")
Include_DataButton.grid(row=0,column=0,padx=0,pady=3)

#modifybutton
Modify_DataButton = Button(Frame2,text="Update",width=20,height=3,bg="#6B69D6",fg="#FFFFFF",command="")
Modify_DataButton.grid(row=1,column=0,padx=5,pady=3)

#resetbutton
Reset_DataButton = Button(Frame2,text="Reset",width=20,height=3,bg="#6B69D6",fg="#FFFFFF",command="")
Reset_DataButton.grid(row=2,column=0,padx=5,pady=3)