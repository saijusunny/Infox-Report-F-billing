from cProfile import label
from cgitb import text
from enum import auto

from itertools import count
from pydoc import describe
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import width
from PIL import ImageTk, Image
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
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

#==============================================++++++++++++++++++++++++++++++++++++++ Saiju
reportframe=Frame(tab9, relief=GROOVE, bg="#f8f8f2")
reportframe.pack(side="top", fill=BOTH)

midFrame=Frame(reportframe, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

refreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command="create")
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
lbl_invdtt = Label(lbframe, text="Report Type:  ", bg="#f8f8f2")
lbl_invdtt.grid(row=1, column=0)

menu1 = StringVar()
drop=ttk.Combobox(lbframe, textvariable=menu1, width=30)
drop.grid(row=2, column=0, pady=5, padx=(5, 0))
drop["values"]=("Screen Charts","Invoice Report","Invoice Report(With Customer)", "Order Report", "Recurring Invoice Report", "Past Due Invoices", "Payment Reports", "Customers List","Customers List(Detailed)","Product/Service List", "Price List", "Products Low Stock Report", "Tax Report(Invoices)", "Tax Report(Orders)", "Sales Report(group by date)", "Invoice Report(Detailed)", "Daily Invoices Report", "Purchase orders Report", "Expenses Report"
)
drop.current(0)

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
chkbtn1 = Checkbutton(lbframe, text = "Invoice", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
chkbtn1.grid(row=0, column=6, rowspan=2, padx=(0,3))

checkvar2 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Outstanding", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
chkbtn1.grid(row=2, column=6,rowspan=2,padx=(25,0))

checkvar3 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Paid", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
chkbtn1.grid(row=1, column=7)


# first graph
mainchartframe = LabelFrame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe.pack(side="left", padx=0, pady=0)

lbl_invdtt =Label(mainchartframe, text="Screen Charts", bg="#f8f8f2" , font=("arial", 16))
lbl_invdtt.grid(row=0, column=1, pady=5, padx=(5, 0))

  
root.mainloop()