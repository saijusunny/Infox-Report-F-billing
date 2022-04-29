from cProfile import label
from cgitb import text
from enum import auto

from itertools import count
from pydoc import describe
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import clear, width
from PIL import ImageTk, Image
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from setuptools import Command
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io

def reset():
  global root
  root.destroy()

root=Tk()
root.geometry("1360x730")

root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
root.iconphoto(False, p1)


s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 =  ttk.Frame(tabControl)
tab10=  ttk.Frame(tabControl)
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
tabControl.pack(expand = 1, fill ="both")


selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")

right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")


photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")
photo11 = PhotoImage(file = "images/export excel.png")

#==============================================++++++++++++++++++++++++++++++++++++++ Saiju
reportframe=Frame(tab9, relief=GROOVE, bg="#f8f8f2")
reportframe.pack(side="top", fill=BOTH)

midFrame=Frame(reportframe, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

midFrame2=Frame(reportframe, bg="#f5f3f2", height=60)
midFrame2.pack(side="top", fill=X)

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

refreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
refreshlebel.pack(side="left")
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))

printlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
printlabel.pack(side="left")
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))


saveLabel = Button(midFrame,compound="top", text="Save Chart\nimage",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
saveLabel.pack(side="left",)
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

copyLabel = Button(midFrame,compound="top", text="Copy Chart\n to Clipboard",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
copyLabel.pack(side="left")
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))
#***********************************************************************************************
#right side of menu bar

lbframe = LabelFrame(midFrame, height=60, width=1500, bg="#f8f8f2")
lbframe.pack(side="left", padx=10, pady=0)


# first graph frame
mainchartframe =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe.pack(side="left", padx=0, pady=0)

#report visable a4sheet

mainchartframe1 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe1.pack(side="top", padx=0, pady=0)

mainchartframe2 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe2.pack(side="left", padx=0, pady=0)

mainchartframe3 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe3.pack(side="left", padx=0, pady=0)

mainchartframe4 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe4.pack(side="left", padx=0, pady=0)

mainchartframe5 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe5.pack(side="left", padx=0, pady=0)

mainchartframe6 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe6.pack(side="left", padx=0, pady=0)

mainchartframe7 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe7.pack(side="left", padx=0, pady=0)

mainchartframe8 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe8.pack(side="left", padx=0, pady=0)

mainchartframe9 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe9.pack(side="left", padx=0, pady=0)

mainchartframe10 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe10.pack(side="left", padx=0, pady=0)

mainchartframe11 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe11.pack(side="left", padx=0, pady=0)

mainchartframe12 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe12.pack(side="left", padx=0, pady=0)

mainchartframe13 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe13.pack(side="left", padx=0, pady=0)

mainchartframe14 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe14.pack(side="left", padx=0, pady=0)

mainchartframe15 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe15.pack(side="left", padx=0, pady=0)

mainchartframe16 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe16.pack(side="left", padx=0, pady=0)

mainchartframe17 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe17.pack(side="left", padx=0, pady=0)

mainchartframe18 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe18.pack(side="left", padx=0, pady=0)

mainchartframe19 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe19.pack(side="left", padx=0, pady=0)

mainchartframe20 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe20.pack(side="left", padx=0, pady=0)



#Drop down Functions----------------------------------------------------------------------------
def maindropmenu(event):
  menuvar=menu1.get()
  if menuvar== "Screen Charts":
    lbl_invdtt1 =Label(mainchartframe, text="Screen Charts", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))

   
  elif menuvar== "Invoice Report":
#frame for display data to a a4 sheet

    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  


    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)
        #--------------------------------check box-------------------------------------
    rpcheckvar1 = IntVar()
    rpchkbtn1 = Checkbutton(lbframe, text = "Paid", variable = rpcheckvar1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1.place(x=483,y=2)

    rpcheckvar2 = IntVar()
    rpchkbtn1 = Checkbutton(lbframe, text = "Void", variable = rpcheckvar2, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1.place(x=483,y=40, )

    rpcheckvar3 = IntVar()
    rpchkbtn1 = Checkbutton(lbframe, text = "Unpaid", variable = rpcheckvar3, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:paidgraph()")
    rpchkbtn1.place(x=570,y=2)

    #------------------------------------------Date---------------------
    rpmenu2 = StringVar()
    rpdrop2=ttk.Combobox(lbframe, textvariable=rpmenu2)
    rpdrop2["values"]=("Month to date","Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2.current(0)
    rpdrop2.place(x=212,y=48)



    lbl_invdtt2 =Label(mainchartframe, text="Invoice Report", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  elif menuvar=="Invoice Report(With Customer)":

    #frame for display data to a a4 sheet

    rprefreshlebel_cst = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel_cst.place(x=22,y=12)


    rpprintlabel_cst = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel_cst.place(x=95,y=12)
  
    rpsaveLabel_cst = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel_cst.place(x=168,y=12)

    rpcopyLabel_cst = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel_cst.place(x=240,y=12)

    #--------------------------------check box-------------------------------------
    rpcheckvar1_cst = IntVar()
    rpchkbtn1_cst = Checkbutton(lbframe, text = "Paid", variable = rpcheckvar1_cst, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1_cst.place(x=483,y=2)

    rpcheckvar2_cst = IntVar()
    rpchkbtn1_cst = Checkbutton(lbframe, text = "Void", variable = rpcheckvar2_cst, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1_cst.place(x=483,y=40)

    rpcheckvar3_cst = IntVar()
    rpchkbtn1_cst = Checkbutton(lbframe, text = "Unpaid", variable = rpcheckvar3_cst, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:paidgraph()")
    rpchkbtn1_cst.place(x=570,y=2)

    #----------------------------------------date----------------------
    rpmenu2_cst = StringVar()
    rpdrop2_cst=ttk.Combobox(lbframe, textvariable=rpmenu2_cst,)
    rpdrop2_cst.grid(row=2, column=3, pady=5, padx=(5, 0))
    rpdrop2_cst["values"]=("Month to date,""Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_cst.place(x=212,y=48)
    rpdrop2_cst.current(0)


    lbl_invdtt3 =Label(mainchartframe2, text="Invoice Report(With Customer)", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt3.grid(row=0, column=1, pady=5, padx=(5, 0))

  elif menuvar=="Order Report":
    #frame for display data to a a4 sheet


    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    w = Canvas(midFrame, width=170, height=75, bg="#f8f8f2")
    w.place(x=820,y=2)


    lbl_invdtt1 =Label(mainchartframe3, text="Order Report", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  elif menuvar=="Recurring Invoice Report":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    lbl_invdtt1 =Label(mainchartframe4, text="Recurring Invoice Report", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
    
    recuw1 = Canvas(midFrame, width=450, height=75, bg="#f8f8f2")
    recuw1.place(x=530,y=2)
    
    recuw2 = Canvas(midFrame, width=100, height=20, bg="#f8f8f2")
    recuw2.place(x=450,y=5 ) 
  
  elif menuvar=="Past Due Invoices":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)
    
    lbl_invdtt1 =Label(mainchartframe5, text="Past Due Invoices", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  

  
  elif menuvar=="Customers List":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)
    lbl_invdtt1 =Label(mainchartframe6, text="Customers List", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  elif menuvar=="Customers List(Detailed)":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)
    lbl_invdtt1 =Label(mainchartframe7, text="Customers List(Detailed)", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  elif menuvar=="Product/Service List":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12) 
    lbl_invdtt1 =Label(mainchartframe8, text="Product/Service List", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  elif menuvar=="Price List":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    lbl_invdtt1 =Label(mainchartframe9, text="Price List", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  elif menuvar=="Products Low Stock Report":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    lbl_invdtt1 =Label(mainchartframe10, text="Products Low Stock Report", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  elif menuvar=="Tax Report(Invoices)":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    lbl_invdtt1 =Label(mainchartframe11, text="Tax Report(Invoices)", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  elif menuvar=="Tax Report(Orders)":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    lbl_invdtt1 =Label(mainchartframe12, text="Tax Report(Orders)", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  elif menuvar=="Sales Report(group by date)":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    lbl_invdtt1 =Label(mainchartframe13, text="Sales Report(group by date)", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  
  elif menuvar=="Invoice Report(Detailed)":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    lbl_invdtt1 =Label(mainchartframe14, text="Invoice Report(Detailed)", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  elif menuvar=="Daily Invoices Report":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    lbl_invdtt1 =Label(mainchartframe15, text="Daily Invoices Report", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  
  elif menuvar=="Purchase orders Report":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    lbl_invdtt1 =Label(mainchartframe16, text="Purchase orders Report", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))

  elif menuvar=="Expenses Report":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    lbl_invdtt1 =Label(mainchartframe17, text="Expenses Report", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
    
  elif menuvar=="Payment Reports":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    lbl_invdtt1 =Label(mainchartframe18, text="Payment Reports", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt1.grid(row=0, column=1, pady=5, padx=(5, 0))
  

  
  else:
    pass

lbl_invdtt = Label(lbframe, text="Report Type:  ", bg="#f8f8f2")
lbl_invdtt.place(x=8, y=10)
menu1 = StringVar()
drop=ttk.Combobox(lbframe, textvariable=menu1, width=30)
drop.grid(row=2, column=0, pady=5, padx=(5, 0))
drop["values"]=("Screen Charts","Invoice Report","Invoice Report(With Customer)", "Order Report", "Recurring Invoice Report", "Past Due Invoices", "Payment Reports", "Customers List","Customers List(Detailed)","Product/Service List", "Price List", "Products Low Stock Report", "Tax Report(Invoices)", "Tax Report(Orders)", "Sales Report(group by date)", "Invoice Report(Detailed)", "Daily Invoices Report", "Purchase orders Report", "Expenses Report"
)
drop.current(0)
drop.bind("<<ComboboxSelected>>",maindropmenu)



lbl_invdtt = Label(lbframe, text="Category:", bg="#f8f8f2")
lbl_invdtt.grid(row=1, column=0, pady=5, padx=(150, 0))

menu = StringVar()
drop1=ttk.Combobox(lbframe, textvariable=menu)
drop1.grid(row=1, column=3, pady=5, padx=(5, 0))
drop1["values"]=("Java","Php", "POP")
drop1.current(0)

menu2 = StringVar()
drop2=ttk.Combobox(lbframe, textvariable=menu2,)
drop2.grid(row=2, column=3, pady=5, padx=(5, 0))
drop2["values"]=("Year To Date","Current year","Last 3 Month","Last 6 Month", "Last 12 Month", "Last 18 Month", "Last 24 Month","Previous Year", "Before Previous Year", "Custom Range")
drop2.current(0)

  
lbl_invdtt =Label(lbframe, text="From:" , bg="#f8f8f2")
lbl_invdtt.grid(row=1, column=4, pady=5, padx=(5, 0))

expdt=DateEntry(lbframe)
expdt.grid(row=1, column=5)

lbl_invdtt =Label(lbframe, text="To:", bg="#f8f8f2")
lbl_invdtt.grid(row=2, column=4, pady=5, padx=(5, 0))

expdt=DateEntry(lbframe)
expdt.grid(row=2, column=5)

checkvar1 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Invoice", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command=lambda:invoicegraph())
chkbtn1.grid(row=0, column=6, rowspan=2, padx=(0,3))

checkvar2 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Outstanding", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command=lambda:outstandinggraph())
chkbtn1.grid(row=2, column=6,rowspan=2,padx=(25,0))

checkvar3 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Paid", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command=lambda:paidgraph())
chkbtn1.grid(row=1, column=7)




#labels




#first graph

import matplotlib.pyplot as plt
from pylab import plot, show, xlabel, ylabel

invoice=StringVar()
outstanding=StringVar()
paid=StringVar()

x=0
invoice=1200
outstanding=22
paid=14

MF1 = Frame(mainchartframe )
MF1.grid(row=2, column=1, pady=5, padx=(5, 0))

#graph function

#invoice Grpah
def invoicegraph():

  global invoice
  global x
  y=float(invoice)
  x+=1
  plt.bar(x,y, label="Invoice", color="orange")
  plt.legend()
  plt.xlabel("x-axis")
  plt.ylabel("y-label")
  plt.show()
  # chart1= label(mainchartframe,plt.show())
  # chart1.grid(row=2, column=1)

  

#Out standing graph
def outstandinggraph():
  global outstanding
  global x
  y=float(outstanding)
  x+=1
  plt.bar(x,y, label="Outstanding", color="blue")
  plt.legend()
  plt.xlabel("x-axis")
  plt.ylabel("y-label")
  plt.show()

#paid graph
def paidgraph():
  global paid
  global x
  y=float(paid)
  x+=1
  plt.bar(x,y, label="Paid", color="green")
  plt.legend()
  plt.xlabel("x-axis")
  plt.ylabel("y-label")
  plt.show()



#secon graph


  
root.mainloop()