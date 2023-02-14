from tkinter import *
import csv
from tkinter import messagebox
import tkinter.font

dataContact = Tk()
dataContact.title("Contact Book")
dataContact.geometry("1300x375")
dataContact.resizable(False, False)

FRAME = Frame(dataContact, bg="blue", height=100, width=300)
imageFile = PhotoImage(file = "PhoneBook-GUI/phonebook.png")
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
    display_Selection
    print(contactList)

def EditCSVFile(contactList):
    with open('StudentData.csv','w', newline='') as csv_file:
        writecsv = csv.writer(csv_file,delimiter=',')
        writecsv.writerow(header)
        for row in contactList:
            writecsv.writerow(row)

def IncludeDetail():
    if FirstName.get()!="" and LastName.get()!="" and ContactNumb.get()!="" and Email.get()!="":
        contactList.append([FirstName.get() +' '+ LastName.get(),ContactNumb.get(), Email.get()])
        print(contactList)
        EditCSVFile(contactList)
        display_Selection()
        ResetData()
        messagebox.showinfo("SUCCESS!", "Contact Added!")
    else:
        messagebox.showerror("ERROR!", "Please fill the correct information needed!")

def ModifyDetail():
    if FirstName.get() and LastName.get() and ContactNumb.get() and Email.get():
        contactList[SelectedData()] = [ FirstName.get()+' '+ LastName.get(), ContactNumb.get(), Email.get()]
        EditCSVFile(contactList)
        messagebox.showinfo("SUCCESS!", "Contact Updated Successfully!")
        ResetData()
        display_Selection()
    elif not(FirstName.get()) and not(LastName.get()) and not(ContactNumb.get()) and not(Email.get()) and not(len(select.curselection())==0):
        messagebox.showerror("ERROR!", "Please Fill the Correct Information Needed!")
    else:
        if len(select.curselection())==0:
            messagebox.showerror("ERROR!", "Please Select the Name and Press Search Button")
        else:
            messagebox.showerror("ERROR!", "To Load all Information of Selected Row of your Choice, Press Search Button.")

def ResetData():
    FirstName_var.set('')
    LastName_var.set('')
    ContactNumb_var.set('')
    Email_var.set('')

def RemoveData():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('CONFIRMATION!','Do You Wish to Permanently Delete Contact?')
        if result==True:
            del contactList[SelectedData()]
            EditCSVFile(contactList)
            display_Selection()
    else:
        messagebox.showerror("ERROR!", 'Please Select the Contact')

def SearchData():
    name, phone, email = contactList[SelectedData()]
    print(name.split(' '))
    FirstName_var.set(name.split()[0])
    LastName_var.set(name.split()[1])
    ContactNumb_var.set(phone)
    Email_var.set(email)

def display_Selection():
    contactList.sort(key=lambda record: record[1])
    select.delete(0, END)
    i=0
    for name, phone, email in contactList:
        i+=1
        select.insert(END, f"{i} / {name} / {phone} / {email}")

def SelectedData():
    print("",len(select.curselection()))
    if len(select.curselection())==0:
        messagebox.showerror("ERROR!", "Please Select the Name you want to find.")
    else:
        return int(select.curselection()[0])

Desired_font = tkinter.font.Font(family="Times New Roman", size=15)
Desired_font2 = tkinter.font.Font(family="OCR A Extended", size=30, weight="bold")

#1ST FRAME
Frame1 = LabelFrame(dataContact,text="")
Frame1.grid(padx=50,pady=15, row=1, column=1, sticky=N)

#innerframe
innerFrame_1 = Frame(Frame1)
innerFrame_1.grid(row=0,column=3,padx=15,pady=0)

#titlesection
title_page = Label(innerFrame_1,text="PHONEBOOK GUI", font= Desired_font2)
title_page.grid(row=0,column=0,columnspan=2,padx=5,pady=5)
title_page_var = StringVar()

#firstnamelabel
Label_FirstName = Label(innerFrame_1,text="First Name", font= Desired_font)
Label_FirstName.grid(row=1,column=0,padx=5,pady=20)
FirstName_var = StringVar()
FirstName = Entry(innerFrame_1,width=50, textvariable=FirstName_var, background="#144272", foreground="#ffffff")
FirstName.grid(row=1,column=1,padx=5,pady=20)

#lastnamelabel
Label_LastName= Label(innerFrame_1,text="Last Name", font= Desired_font)
Label_LastName.grid(row=2,column=0,padx=5,pady=20)
LastName_var= StringVar()
LastName = Entry(innerFrame_1,width=50,textvariable=LastName_var, background="#144272", foreground="#ffffff")
LastName.grid(row=2,column=1,padx=5,pady=20)

#contactnumlabel
Label_ContactNumb= Label(innerFrame_1,text="Contact Number", font= Desired_font)
Label_ContactNumb.grid(row=3,column=0,padx=5,pady=20)
ContactNumb_var = StringVar()
ContactNumb = Entry(innerFrame_1,width=50,textvariable=ContactNumb_var, background="#144272", foreground="#ffffff")
ContactNumb.grid(row=3,column=1,padx=5,pady=20)

#emaillabel
Label_Email= Label(innerFrame_1,text="Email Address", font= Desired_font)
Label_Email.grid(row=4,column=0,padx=5,pady=20)
Email_var = StringVar()
Email = Entry(innerFrame_1,width=50,textvariable=Email_var, background="#144272", foreground="#ffffff")
Email.grid(row=4,column=1,padx=5,pady=20)

#2ND FRAME
Frame2 = Frame(dataContact)
Frame2.grid(row=1,column=3,padx=5,pady=20,sticky=N)

#addbutton
Include_DataButton = Button(Frame2,text="Add",width=20,height=3,bg="#F94A29",fg="#FFFFFF",command=IncludeDetail)
Include_DataButton.grid(row=0,column=0,padx=0,pady=3)

#modifybutton
Modify_DataButton = Button(Frame2,text="Update",width=20,height=3,bg="#F94A29",fg="#FFFFFF",command=ModifyDetail)
Modify_DataButton.grid(row=1,column=0,padx=5,pady=3)

#resetbutton
Reset_DataButton = Button(Frame2,text="Reset",width=20,height=3,bg="#F94A29",fg="#FFFFFF",command = ResetData)
Reset_DataButton.grid(row=2,column=0,padx=5,pady=3)

#This will display the DETAILS of the contacts.
Data_Display = Frame(dataContact)
Data_Display.grid(row=1,column=2,padx=15,pady=10, sticky=N,rowspan=3)
# scroll = Scrollbar(Data_Display, orient=VERTICAL)
select = Listbox(Data_Display,font=("Cascadia Code",10),bg="#000000",fg="#FFBF00",width=50,height=19,borderwidth=5,relief="groove")
# scroll.config(command=select.yview)
select.grid(row=0,column=1)
# scroll.grid(row=0,column=1)

#FUNCTION FRAME
FunctionFrame = Frame(dataContact)
FunctionFrame.grid(row=1,column=3,padx=75,pady= 205,sticky=S + N)

#searchbutton
Searchbutton = Button(FunctionFrame,text="Search",width=20, height = 4, bg="#F94A29",fg="#FFFFFF",command=SearchData)
Searchbutton.grid(row=0,column=0,padx=5,pady=3)

#deletebutton
Delete_button = Button(FunctionFrame,text="Delete",width=20,height=4,bg="#820000",fg="#FFFFFF",command=RemoveData)
Delete_button.grid(row=1,column=0,padx=5,pady=3)


InterpetCSVFile()

dataContact.mainloop()