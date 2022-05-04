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



from tkPDFViewer import tkPDFViewer as pdf# For pdf view
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
reportframe=Frame(tab9, relief=GROOVE, bg="red")
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
mainchartframe =Frame(reportframe,height=1500,width=1500,bg="#f8f8f2")
mainchartframe.place(x=0, y=90)

#report visable a4sheet

mainchartframe1 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
mainchartframe1.place(x=0, y=90)


#Filter by category----------------------------------------------------------------------------
def category():
  # firtst filter-----------------------------------Month to date
  rth=invfilter.get()
  if rth=="Month to date":
        frame = Frame(
        reportframe,
        width=953, 
        height=1000,
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=125)
        canvas=Canvas(
            frame,
            bg='grey',
            width=1400,
            height=1200,
            scrollregion=(0,0,1500, 1500)
            )

        vertibar=Scrollbar(
            frame,
            orient=VERTICAL
            )
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=1300,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text="Invoice Report",fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022     Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')

        # tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7), height = 15, show = "headings")
        # tree.place(x=200, y=350)
        # tree.heading(1)
        # tree.heading(2, text="Invoice#")
        # tree.heading(3, text="Next Invoice")
        # tree.heading(4, text="Recurring Period")
        # tree.heading(5, text="Stop After")
        # tree.heading(6, text="Customer Name")
        # tree.heading(7, text="Invoice Total")  
        # tree.column(1, width = 20)
        # tree.column(2, width = 20)
        # tree.column(3, width = 20)
        # tree.column(4, width = 20)
        # tree.column(5, width = 20) 
        # tree.column(6, width = 20)
        # tree.column(7, width = 20)
  else:
    pass



invfilter = StringVar()# veriable for store category filter
#Drop down Functions----------------------------------------------------------------------------
def maindropmenu(event):
  menuvar=menu1.get()
  if menuvar== "Invoice Report":
#frame for display data to a a4 sheet

    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55, command=category)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  


    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)
    
    iruw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    iruw1.place(x=415,y=9)
    iruw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    iruw2.place(x=530,y=9)
    lbl_ir =Label(midFrame, text="From:" , bg="#f8f8f2")
    lbl_ir.place(x=676,y=10)

    exir=DateEntry(midFrame)
    exir.place(x=721,y=10)

    lbl_ir =Label(midFrame, text="To:", bg="#f8f8f2")
    lbl_ir.place(x=690,y=50)

    exir=DateEntry(midFrame)
    exir.place(x=721,y=50)

    lbl_ir = Label(midFrame, text="Category:", bg="#f8f8f2")
    lbl_ir.place(x=470,y=10)

    menuir = StringVar()
    drop1ir=ttk.Combobox(midFrame, textvariable=menuir)
    drop1ir.place(x=530,y=10)
    drop1ir["values"]=("Java","Php", "POP")
    drop1ir.current(0)

    
    rpdrop2_ir=ttk.Combobox(midFrame, textvariable=invfilter)
    rpdrop2_ir["values"]=("Month to date","Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_ir.place(x=530,y=50)
    rpdrop2_ir.current(0)



    #--------------------------------check box-------------------------------------
    rpcheckvar1_ir = IntVar()
    rpchkbtn1_ir= Checkbutton(midFrame, text = "Paid", variable = rpcheckvar1_ir, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1_ir.place(x=815,y=2)

    rpcheckvar2_ir = IntVar()
    rpchkbtn1_ir = Checkbutton(midFrame, text = "Void", variable = rpcheckvar2_ir, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1_ir.place(x=815,y=40)

    rpcheckvar3_ir = IntVar()
    rpchkbtn1_ir= Checkbutton(midFrame, text = "Unpaid", variable = rpcheckvar3_ir, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:paidgraph()")
    rpchkbtn1_ir.place(x=883,y=2)

    mainchartframe2 =Frame(reportframe,height=1500, width=200)
    mainchartframe2.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)


    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')
    #----------------------------------------------------------------------------------------------------
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

    irwcuw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    irwcuw1.place(x=415,y=9)
    irwcuw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    irwcuw2.place(x=530,y=9)
    lbl_irwc =Label(midFrame, text="From:" , bg="#f8f8f2")
    lbl_irwc.place(x=676,y=10)

    exirwc=DateEntry(midFrame)
    exirwc.place(x=721,y=10)

    lbl_irwc =Label(midFrame, text="To:", bg="#f8f8f2")
    lbl_irwc.place(x=690,y=50)

    exirwc=DateEntry(midFrame)
    exirwc.place(x=721,y=50)

    lbl_irwc = Label(midFrame, text="Category:", bg="#f8f8f2")
    lbl_irwc.place(x=470,y=10)

    menuirwc = StringVar()
    drop1irwc=ttk.Combobox(midFrame, textvariable=menuirwc)
    drop1irwc.place(x=530,y=10)
    drop1irwc["values"]=("Java","Php", "POP")
    drop1irwc.current(0)

    rpmenu2_irwc = StringVar()
    rpdrop2_irwc=ttk.Combobox(midFrame, textvariable=rpmenu2_irwc,)
    rpdrop2_irwc["values"]=("Month to date,""Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_irwc.place(x=530,y=50)
    rpdrop2_irwc.current(0)



    #--------------------------------check box-------------------------------------
    rpcheckvar1_irwc = IntVar()
    rpchkbtn1_irwc= Checkbutton(midFrame, text = "Paid", variable = rpcheckvar1_irwc, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1_irwc.place(x=815,y=2)

    rpcheckvar2_irwc = IntVar()
    rpchkbtn1_irwc = Checkbutton(midFrame, text = "Void", variable = rpcheckvar2_irwc, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1_irwc.place(x=815,y=40)

    rpcheckvar3_irwc = IntVar()
    rpchkbtn1_irwc = Checkbutton(midFrame, text = "Unpaid", variable = rpcheckvar3_irwc, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:paidgraph()")
    rpchkbtn1_irwc.place(x=883,y=2)

    mainchartframe3 =Frame(reportframe,height=1500, width=200)
    mainchartframe3.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)

    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')

    #----------------------------------------------------------------------------------------------------
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
    
    oruw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    oruw1.place(x=415,y=9)
    oruw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    oruw2.place(x=530,y=9)

    lbl_or =Label(midFrame, text="From:" , bg="#f8f8f2")
    lbl_or.place(x=676,y=10)

    exor=DateEntry(midFrame)
    exor.place(x=721,y=10)

    lbl_or =Label(midFrame, text="To:", bg="#f8f8f2")
    lbl_or.place(x=690,y=50)

    exor=DateEntry(midFrame)
    exor.place(x=721,y=50)

    lbl_or = Label(midFrame, text="Category:", bg="#f8f8f2")
    lbl_or.place(x=470,y=10)

    menuor = StringVar()
    drop1or=ttk.Combobox(midFrame, textvariable=menuor)
    drop1or.place(x=530,y=10)
    drop1or["values"]=("Java","Php", "POP")
    drop1or.current(0)

    rpmenu2_or = StringVar()
    rpdrop2_or=ttk.Combobox(midFrame, textvariable=rpmenu2_or,)
    rpdrop2_or["values"]=("Month to date,""Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_or.place(x=530,y=50)
    rpdrop2_or.current(0)
    
    mainchartframe4 =Frame(reportframe,height=1500, width=200)
    mainchartframe4.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)

#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')
  
      #----------------------------------------------------------------------------------------------------
  elif menuvar=="Recurring Invoice Report":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    
    pruw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    pruw1.place(x=415,y=9)
    pruw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    pruw2.place(x=530,y=9)

    mainchartframe5 =Frame(reportframe,height=1500, width=200)
    mainchartframe5.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)

#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')

      #----------------------------------------------------------------------------------------------------
  elif menuvar=="Past Due Invoices":

    rprefreshlebelpdi = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebelpdi.place(x=22,y=12)


    rpprintlabelpdi = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabelpdi.place(x=95,y=12)
  

    rpsaveLabelpdi = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabelpdi.place(x=168,y=12)

    rpcopyLabelpdi = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabelpdi.place(x=240,y=12)
    
    pdiuw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    pdiuw1.place(x=415,y=9)
    pdiuw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    pdiuw2.place(x=530,y=9)


    lbl_pdi = Label(midFrame, text="Category:", bg="#f8f8f2")
    lbl_pdi.place(x=530,y=9)
    
    menupdi = StringVar()
    drop1pdi=ttk.Combobox(midFrame, textvariable=menupdi, width=30)
    drop1pdi.place(x=530,y=50)
    drop1pdi["values"]=("Java","Php", "POP")
    drop1pdi.current(0)

    mainchartframe6 =Frame(reportframe,height=1500, width=200)
    mainchartframe6.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)

#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')
    #----------------------------------------------------------------------------------------------------
  
  elif menuvar=="Customers List":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)


    pdiuw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    pdiuw1.place(x=415,y=9)

    cluw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    cluw2.place(x=530,y=9)


    lbl_cl = Label(midFrame, text=" Select Customer Category:", bg="#f8f8f2")
    lbl_cl.place(x=530,y=9)
    
    menucl = StringVar()
    drop1cl=ttk.Combobox(midFrame, textvariable=menucl, width=30)
    drop1cl.place(x=530,y=50)
    drop1cl["values"]=("All Customers ","Default")
    drop1cl.current(0)

    rpcheckvar1_cl = IntVar()
    rpchkbtn1_cl = Checkbutton(midFrame, text = "Active", variable = rpcheckvar1_cl, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1_cl.place(x=725,y=2)

    rpcheckvar2_cl = IntVar()
    rpchkbtn1_cl = Checkbutton(midFrame, text = "Inactive", variable = rpcheckvar2_cl, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1_cl.place(x=730,y=40)
    
    mainchartframe7 =Frame(reportframe,height=1500, width=200)
    mainchartframe7.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)

#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')
    #----------------------------------------------------------------------------------------------------
  
  elif menuvar=="Customers List(Detailed)":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    cluw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    cluw2.place(x=530,y=9)


    lbl_cl = Label(midFrame, text=" Select Customer Category:", bg="#f8f8f2")
    lbl_cl.place(x=530,y=9)
    
    menucl = StringVar()
    drop1cl=ttk.Combobox(midFrame, textvariable=menucl, width=30)
    drop1cl.place(x=530,y=50)
    drop1cl["values"]=("All Customers ","Default")
    drop1cl.current(0)

    rpcheckvar1_cl = IntVar()
    rpchkbtn1_cl = Checkbutton(midFrame, text = "Active", variable = rpcheckvar1_cl, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1_cl.place(x=725,y=2)

    rpcheckvar2_cl = IntVar()
    rpchkbtn1_cl = Checkbutton(midFrame, text = "Inactive", variable = rpcheckvar2_cl, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1_cl.place(x=730,y=40)

    mainchartframe8 =Frame(reportframe,height=1500, width=200)
    mainchartframe8.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)
#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')
    #----------------------------------------------------------------------------------------------------
  
  elif menuvar=="Product/Service List":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12) 

    psluw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    psluw1.place(x=415,y=9)

    psluw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    psluw2.place(x=530,y=9)


    lbl_psl = Label(midFrame, text=" Select Product Category:", bg="#f8f8f2")
    lbl_psl.place(x=530,y=9)
    
    menupsl = StringVar()
    drop1psl=ttk.Combobox(midFrame, textvariable=menupsl, width=30)
    drop1psl.place(x=530,y=50)
    drop1psl["values"]=("All product and Services ", "All products", "All Service","Default")
    drop1psl.current(0)

    rpcheckvar1_psl = IntVar()
    rpchkbtn1_psl = Checkbutton(midFrame, text = "Active", variable = rpcheckvar1_psl, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1_psl.place(x=725,y=2)

    rpcheckvar2_psl = IntVar()
    rpchkbtn1_psl = Checkbutton(midFrame, text = "Inactive", variable = rpcheckvar2_psl, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1_psl.place(x=730,y=40)

    mainchartframe9 =Frame(reportframe,height=1500, width=200)
    mainchartframe9.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)
#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')

      #----------------------------------------------------------------------------------------------------

  elif menuvar=="Price List":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    pluw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    pluw1.place(x=415,y=9)

    pluw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    pluw2.place(x=530,y=9)


    lbl_pl = Label(midFrame, text=" Select Product Category:", bg="#f8f8f2")
    lbl_pl.place(x=530,y=9)
    
    menupl = StringVar()
    drop1pl=ttk.Combobox(midFrame, textvariable=menupl, width=30)
    drop1pl.place(x=530,y=50)
    drop1pl["values"]=("All product and Services ", "All products", "All Service","Default")
    drop1pl.current(0)

    rpcheckvar1_pl = IntVar()
    rpchkbtn1_pl = Checkbutton(midFrame, text = "Active", variable = rpcheckvar1_pl, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1_pl.place(x=725,y=2)

    rpcheckvar2_pl = IntVar()
    rpchkbtn1_pl = Checkbutton(midFrame, text = "Inactive", variable = rpcheckvar2_pl, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1_pl.place(x=730,y=40)


    mainchartframe10 =Frame(reportframe,height=1500, width=200)
    mainchartframe10.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview ", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)

#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')
    #----------------------------------------------------------------------------------------------------
  
  elif menuvar=="Products Low Stock Report":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    plruw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    plruw1.place(x=415,y=9)

    plruw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    plruw2.place(x=530,y=9)


    rpcheckvar1_plr = IntVar()
    rpchkbtn1_plr = Checkbutton(midFrame, text = "Active", variable = rpcheckvar1_plr, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1_plr.place(x=530,y=2)

    rpcheckvar2_plr = IntVar()
    rpchkbtn1_plr = Checkbutton(midFrame, text = "Inactive", variable = rpcheckvar2_plr, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1_plr.place(x=535,y=40)
    
    mainchartframe11 =Frame(reportframe,height=1500, width=200)
    mainchartframe11.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)
#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')
   
    #----------------------------------------------------------------------------------------------------
  elif menuvar=="Tax Report(Invoices)":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    triuw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    triuw1.place(x=415,y=9)

    triuw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    triuw2.place(x=530,y=9)

    lbl_tri =Label(midFrame, text="From:" , bg="#f8f8f2")
    lbl_tri.place(x=676,y=10)

    extri=DateEntry(midFrame)
    extri.place(x=721,y=10)

    lbl_tri =Label(midFrame, text="To:", bg="#f8f8f2")
    lbl_tri.place(x=690,y=50)

    extri=DateEntry(midFrame)
    extri.place(x=721,y=50)

    lbl_tri = Label(midFrame, text="Category:", bg="#f8f8f2")
    lbl_tri.place(x=470,y=10)

    menutri = StringVar()
    drop1tri=ttk.Combobox(midFrame, textvariable=menutri)
    drop1tri.place(x=530,y=10)
    drop1tri["values"]=("Java","Php", "POP")
    drop1tri.current(0)

    rpmenu2_tri = StringVar()
    rpdrop2_tri=ttk.Combobox(midFrame, textvariable=rpmenu2_tri,)
    rpdrop2_tri["values"]=("Month to date,""Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_tri.place(x=530,y=50)
    rpdrop2_tri.current(0)
      

    rpcheckvar1_tri = IntVar()
    rpchkbtn1_tri= Checkbutton(midFrame, text = "Paid", variable = rpcheckvar1_tri, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1_tri.place(x=815,y=2)

    rpcheckvar2_tri = IntVar()
    rpchkbtn1_tri = Checkbutton(midFrame, text = "Void", variable = rpcheckvar2_tri, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1_tri.place(x=815,y=40)

    rpcheckvar3_tri = IntVar()
    rpchkbtn1_tri = Checkbutton(midFrame, text = "Unpaid", variable = rpcheckvar3_tri, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:paidgraph()")
    rpchkbtn1_tri.place(x=883,y=2)
    
    mainchartframe12 =Frame(reportframe,height=1500, width=200)
    mainchartframe12.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)

#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')

    #----------------------------------------------------------------------------------------------------
  elif menuvar=="Tax Report(Orders)":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)


    trouw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    trouw1.place(x=415,y=9)

    trouw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    trouw2.place(x=530,y=9)

    lbl_tro =Label(midFrame, text="From:" , bg="#f8f8f2")
    lbl_tro.place(x=676,y=10)

    extro=DateEntry(midFrame)
    extro.place(x=721,y=10)

    lbl_tro =Label(midFrame, text="To:", bg="#f8f8f2")
    lbl_tro.place(x=690,y=50)

    extro=DateEntry(midFrame)
    extro.place(x=721,y=50)

    lbl_tro = Label(midFrame, text="Category:", bg="#f8f8f2")
    lbl_tro.place(x=470,y=10)

    menutro = StringVar()
    drop1tro=ttk.Combobox(midFrame, textvariable=menutro)
    drop1tro.place(x=530,y=10)
    drop1tro["values"]=("Java","Php", "POP")
    drop1tro.current(0)

    rpmenu2_tro = StringVar()
    rpdrop2_tro=ttk.Combobox(midFrame, textvariable=rpmenu2_tro,)
    rpdrop2_tro["values"]=("Month to date,""Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_tro.place(x=530,y=50)
    rpdrop2_tro.current(0)
    
    mainchartframe13 =Frame(reportframe,height=1500, width=200)
    mainchartframe13.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)

#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')
    #----------------------------------------------------------------------------------------------------
  
  elif menuvar=="Sales Report(group by date)":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    sruw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    sruw1.place(x=415,y=9)

    sruw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    sruw2.place(x=530,y=9)

    lbl_sr =Label(midFrame, text="From:" , bg="#f8f8f2")
    lbl_sr.place(x=728,y=10)

    exsr=DateEntry(midFrame)
    exsr.place(x=773,y=10)

    lbl_sr =Label(midFrame, text="To:", bg="#f8f8f2")
    lbl_sr.place(x=743,y=50)

    exsr=DateEntry(midFrame)
    exsr.place(x=773,y=50)

    lbl_sr = Label(midFrame, text="Category:", bg="#f8f8f2")
    lbl_sr.place(x=470,y=10)

    menusr = StringVar()
    drop1sr=ttk.Combobox(midFrame, textvariable=menu, width=30)
    drop1sr.place(x=530,y=10)
    drop1sr["values"]=("Java","Php", "POP")
    drop1sr.current(0)

    rpmenu2_sr = StringVar()
    rpdrop2_sr=ttk.Combobox(midFrame, textvariable=rpmenu2_sr,width=30)
    rpdrop2_sr["values"]=("Month to date,""Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_sr.place(x=530,y=50)
    rpdrop2_sr.current(0)


    mainchartframe14 =Frame(reportframe,height=1500, width=200)
    mainchartframe14.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)
#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')

      #----------------------------------------------------------------------------------------------------
  elif menuvar=="Invoice Report(Detailed)":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)
    plruw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    plruw1.place(x=415,y=9)

    irduw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    irduw2.place(x=530,y=9)

    lbl_ird =Label(midFrame, text="From:" , bg="#f8f8f2")
    lbl_ird.place(x=728,y=10)

    exird=DateEntry(midFrame)
    exird.place(x=773,y=10)

    lbl_ird =Label(midFrame, text="To:", bg="#f8f8f2")
    lbl_ird.place(x=743,y=50)

    exird=DateEntry(midFrame)
    exird.place(x=773,y=50)

    lbl_ird = Label(midFrame, text="Category:", bg="#f8f8f2")
    lbl_ird.place(x=470,y=10)

    menuird = StringVar()
    drop1ird=ttk.Combobox(midFrame, textvariable=menuird, width=30)
    drop1ird.place(x=530,y=10)
    drop1ird["values"]=("Java","Php", "POP")
    drop1ird.current(0) 

    rpmenu2_ird = StringVar()
    rpdrop2_ird=ttk.Combobox(midFrame, textvariable=rpmenu2_ird,width=30)
    rpdrop2_ird["values"]=("Month to date,""Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_ird.place(x=530,y=50)
    rpdrop2_ird.current(0)


    
    mainchartframe15 =Frame(reportframe,height=1500, width=200)
    mainchartframe15.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2")
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)
#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')

    #----------------------------------------------------------------------------------------------------
  elif menuvar=="Daily Invoices Report":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)\

    diruw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    diruw1.place(x=415,y=9)

    diruw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    diruw2.place(x=530,y=9)


    lbl_dir = Label(midFrame, text=" Day:", bg="#f8f8f2")
    lbl_dir.place(x=526,y=9)
    
    exidir=DateEntry(midFrame)
    exidir.place(x=530,y=50)

   
    mainchartframe16 =Frame(reportframe,height=1500, width=200)
    mainchartframe16.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2") 
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)
#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')
    #----------------------------------------------------------------------------------------------------  
  elif menuvar=="Purchase orders Report":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    poruw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    poruw1.place(x=415,y=9)

    poruw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    poruw2.place(x=530,y=9)

    lbl_por =Label(midFrame, text="From:" , bg="#f8f8f2")
    lbl_por.place(x=676,y=10)

    expor=DateEntry(midFrame)
    expor.place(x=721,y=10)

    lbl_por =Label(midFrame, text="To:", bg="#f8f8f2")
    lbl_por.place(x=690,y=50)

    expor=DateEntry(midFrame)
    expor.place(x=721,y=50)

    lbl_por = Label(midFrame, text="Category:", bg="#f8f8f2")
    lbl_por.place(x=470,y=10)

    menupor = StringVar()
    drop1por=ttk.Combobox(midFrame, textvariable=menupor)
    drop1por.place(x=530,y=10)
    drop1por["values"]=("Java","Php", "POP")
    drop1por.current(0)

    rpmenu2_por = StringVar()
    rpdrop2_por=ttk.Combobox(midFrame, textvariable=rpmenu2_por,)
    rpdrop2_por["values"]=("Month to date,""Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_por.place(x=530,y=50)
    rpdrop2_por.current(0)
      

    rpcheckvar1_por = IntVar()
    rpchkbtn1_por= Checkbutton(midFrame, text = "Complete", variable = rpcheckvar1_por, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1_por.place(x=815,y=2)

    rpcheckvar2_por = IntVar()
    rpchkbtn1_por = Checkbutton(midFrame, text = "Draft", variable = rpcheckvar2_por, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1_por.place(x=815,y=40)


    mainchartframe17 =Frame(reportframe,height=1500, width=200)
    mainchartframe17.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2") 
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)
#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')

    #----------------------------------------------------------------------------------------------------
  elif menuvar=="Expenses Report":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)


    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)
    sruw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    sruw1.place(x=415,y=9)

    sruw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    sruw2.place(x=530,y=9)

    lbl_er =Label(midFrame, text="From:" , bg="#f8f8f2")
    lbl_er.place(x=728,y=10)

    exer=DateEntry(midFrame)
    exer.place(x=773,y=10)

    lbl_er =Label(midFrame, text="To:", bg="#f8f8f2")
    lbl_er.place(x=743,y=50)

    exer=DateEntry(midFrame)
    exer.place(x=773,y=50)

    lbl_er = Label(midFrame, text="Category:", bg="#f8f8f2")
    lbl_er.place(x=470,y=10)

    menuer = StringVar()
    drop1er=ttk.Combobox(midFrame, textvariable=menuer, width=30)
    drop1er.place(x=530,y=10)
    drop1er["values"]=("Java","Php", "POP")
    drop1er.current(0)

    rpmenu2_er = StringVar()
    rpdrop2_er=ttk.Combobox(midFrame, textvariable=rpmenu2_er,width=30)
    rpdrop2_er["values"]=("Month to date,""Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_er.place(x=530,y=50)
    rpdrop2_er.current(0)

    rpcheckvar1_er = IntVar()
    rpchkbtn1_er= Checkbutton(midFrame, text = "Invoiced", variable = rpcheckvar1_er, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
    rpchkbtn1_er.place(x=868,y=2)

    rpcheckvar2_er = IntVar()
    rpchkbtn1_er = Checkbutton(midFrame, text = "Rebilable", variable = rpcheckvar2_er, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
    rpchkbtn1_er.place(x=868,y=40)


    mainchartframe19 =Frame(reportframe,height=1500, width=200)
    mainchartframe19.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2") 
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)
#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')

    #----------------------------------------------------------------------------------------------------
  elif menuvar=="Payment Reports":
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
    rprefreshlebel.place(x=22,y=12)
 

    rpprintlabel = Button(midFrame,compound="top", text="Print Chart",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="create")
    rpprintlabel.place(x=95,y=12)
  

    rpsaveLabel = Button(midFrame,compound="top", text="Export Report\n to Excel",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="dele")
    rpsaveLabel.place(x=168,y=12)

    rpcopyLabel = Button(midFrame,compound="top", text="Export Report\n to PDF",relief=RAISED, image=copy,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="convert")
    rpcopyLabel.place(x=240,y=12)

    pruw1 = Label(midFrame,text="                                    ", bg="#f8f8f2")
    pruw1.place(x=415,y=9)
    pruw2 = Label(midFrame,text="                                                                                                             \n                                                                                                                                                  \n                                                              \n                                                            ", bg="#f8f8f2")
    pruw2.place(x=530,y=9)


    lbl_pr = Label(midFrame, text="Category:", bg="#f8f8f2")
    lbl_pr.place(x=530,y=9)
    
    menupr = StringVar()
    drop1pr=ttk.Combobox(midFrame, textvariable=menupr, width=30)
    drop1pr.place(x=530,y=50)
    drop1pr["values"]=("Java","Php", "POP")
    drop1pr.current(0)

    lbl_pr =Label(midFrame, text="From:" , bg="#f8f8f2")
    lbl_pr.place(x=725,y=10)

    expr=DateEntry(midFrame)
    expr.place(x=770,y=10)

    lbl_pr =Label(midFrame, text="To:", bg="#f8f8f2")
    lbl_pr.place(x=740,y=50)

    expr=DateEntry(midFrame)
    expr.place(x=770,y=50)


    mainchartframe18 =Frame(reportframe,height=1500, width=200)
    mainchartframe18.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2") 
    irwcuw1.place(x=2,y=95)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="#f8f8f2" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=100)

#Pdf page
    frame = Frame(
        reportframe,
        width=953,
        height=1000,
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=125)
    canvas=Canvas(
        frame,
        bg='grey',
        width=1400,
        height=1200,
        scrollregion=(0,0,1500, 1500)
        )

    vertibar=Scrollbar(
        frame,
        orient=VERTICAL
        )
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1300,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')


  

  
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




irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f8f8f2") 
irwcuw1.place(x=2,y=95)


lbl_invdtt2 =Label(reportframe, text="Screen Charts", bg="#f8f8f2" , font=("arial", 16))
lbl_invdtt2.place(x=2, y=100)

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

# MF1 = Frame(mainchartframe )
# MF1.grid(row=2, column=1, pady=5, padx=(5, 0))

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