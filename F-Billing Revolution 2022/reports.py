from cProfile import label
from cgitb import text
from enum import auto

from itertools import count
from pydoc import describe
from sqlite3 import Cursor
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from turtle import clear, color, width
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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime as dt


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
reportframe=Frame(tab9, relief=GROOVE, bg="#f5f3f2")
reportframe.pack(side="top", fill=BOTH)

midFrame=Frame(reportframe, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

# midFrame2=Frame(reportframe, bg="red", height=60)
# midFrame2.pack(side="top", fill=X)

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


#report visable a4sheet

# mainchartframe1 =Frame(reportframe,height=1500, width=1500, bg="#f8f8f2")
# mainchartframe1.pack()
# dte = dt.datetime.now()
# print({date:%a, %b,%d,%y})
#Filter by category----------------------------------------------------------------------------
def category():
  # firtst filter-----------------------------------Month to date
    rth=invfilter.get()
    if rth=="Month to date":

        frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=115)
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
        canvas.config(width=1310,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text=menu1.get(),fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022      Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        # Create an instance of Style widget
        style=ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        # Add a Treeview widget
        tree=ttk.Treeview(canvas, column=("c1", "c2"), show='headings', height=8, style='mystyle.Treeview')
        tree.column("# 1", anchor=E, stretch=NO, width=100)
        tree.heading("# 1", text="Index")
        tree.column("# 2", anchor=E, stretch=NO)
        tree.heading("# 2", text="Programming Language")

        # Insert the data in Treeview widget
        tree.insert('', 'end',text="1",values=('1','C++'))
        tree.insert('', 'end',text="2",values=('2', 'Java'))
        tree.insert('', 'end',text="3",values=('3', 'Python'))
        tree.insert('', 'end',text="4",values=('4', 'Golang'))
        tree.insert('', 'end',text="5",values=('5', 'JavaScript'))
        tree.insert('', 'end',text="6",values=('6', 'C# '))
        tree.insert('', 'end',text="7",values=('6', 'Rust'))
        tree.insert('', 'end',text="8",values=('6', 'SQL'))

        tree.place(x=10,y=200)
    #--------------------------------------------------------------------------------------------------------------
    elif rth=="Year To Date":
        frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=115)
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
        canvas.config(width=1310,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text=menu1.get(),fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022     Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')

        
        def emailrp():
            rpmailDetail=Toplevel()
            rpmailDetail.title("E-Mail")
            p2 = PhotoImage(file = "images/fbicon.png")
            rpmailDetail.iconphoto(False, p2)
            rpmailDetail.geometry("1030x550+150+120")
            
            def myrp_SMTP():
                if True:
                    em_ser_conbtn.destroy()
                    mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
                    mysmtpservercon.place(x=610, y=110)
                    lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
                    hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
                    lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
                    portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
                    lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
                    unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
                    lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
                    pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
                    ssl_chkvar=IntVar()
                    ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
                    ssl_chkbtn.place(x=50, y=110)
                    em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
                else:
                    pass
            
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", padding=5)
            email_Notebook = ttk.Notebook(rpmailDetail)
            email_Frame = Frame(email_Notebook, height=500, width=1080)
            account_Frame = Frame(email_Notebook, height=550, width=1080)
            email_Notebook.add(email_Frame, text="E-mail")
            email_Notebook.add(account_Frame, text="Account")
            email_Notebook.place(x=0, y=0)
            messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
            messagelbframe.place(x=5, y=5)
            lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
            emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
            sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
            lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
            carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
            stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
            lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
            subent=Entry(messagelbframe, width=50).place(x=120, y=59)

            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
            mess_Notebook = ttk.Notebook(messagelbframe)
            emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
            htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
            mess_Notebook.add(emailmessage_Frame, text="E-mail message")
            mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
            mess_Notebook.place(x=5, y=90)

            btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
            btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
            btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
            btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
            btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
            btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
            btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
            btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
            btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
            btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
            btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

            dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
            dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
            mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
            btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
            attachlbframe.place(x=740, y=5)
            htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
            lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
            btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
            btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
            lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
            lbl_tt_info.place(x=740, y=370)

            ready_frame=Frame(rpmailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
            
            sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
            sendatalbframe.place(x=5, y=5)
            lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
            sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
            lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
            nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
            lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
            replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
            lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
            signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
            confirm_chkvar=IntVar()
            confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
            confirm_chkbtn.place(x=200, y=215)
            btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

            sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
            sendatalbframe.place(x=610, y=5)
            servar=IntVar()
            SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
            SMTP_rbtn.place(x=10, y=10)
            MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=myrp_SMTP)
            MySMTP_rbtn.place(x=10, y=40)
            em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
            em_ser_conbtn.place(x=710, y=110)
        
        def my_popup(event):
            my_menu.tk_popup(event.x_root, event.y_root)
            
        my_menu= Menu(canvas, tearoff=False)
        my_menu.add_command(label="Run Report", command="run")
        my_menu.add_separator()
        my_menu.add_command(label="Print Report", command="pr")
        my_menu.add_command(label="Email Report", command=emailrp)

        my_menu.add_separator()
        my_menu.add_command(label="Export Report To Excel", command="excel")
        my_menu.add_command(label="Export Report To PDF", command="pdf")


        canvas.bind("<Button-3>", my_popup)
        #===============================================================================================
    elif rth=="Current year":
        frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=115)
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
        canvas.config(width=1310,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text=menu1.get(),fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022     Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')

        
        def emailrp():
            rpmailDetail=Toplevel()
            rpmailDetail.title("E-Mail")
            p2 = PhotoImage(file = "images/fbicon.png")
            rpmailDetail.iconphoto(False, p2)
            rpmailDetail.geometry("1030x550+150+120")
            
            def myrp_SMTP():
                if True:
                    em_ser_conbtn.destroy()
                    mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
                    mysmtpservercon.place(x=610, y=110)
                    lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
                    hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
                    lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
                    portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
                    lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
                    unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
                    lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
                    pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
                    ssl_chkvar=IntVar()
                    ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
                    ssl_chkbtn.place(x=50, y=110)
                    em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
                else:
                    pass
            
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", padding=5)
            email_Notebook = ttk.Notebook(rpmailDetail)
            email_Frame = Frame(email_Notebook, height=500, width=1080)
            account_Frame = Frame(email_Notebook, height=550, width=1080)
            email_Notebook.add(email_Frame, text="E-mail")
            email_Notebook.add(account_Frame, text="Account")
            email_Notebook.place(x=0, y=0)
            messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
            messagelbframe.place(x=5, y=5)
            lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
            emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
            sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
            lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
            carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
            stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
            lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
            subent=Entry(messagelbframe, width=50).place(x=120, y=59)

            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
            mess_Notebook = ttk.Notebook(messagelbframe)
            emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
            htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
            mess_Notebook.add(emailmessage_Frame, text="E-mail message")
            mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
            mess_Notebook.place(x=5, y=90)

            btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
            btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
            btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
            btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
            btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
            btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
            btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
            btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
            btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
            btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
            btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

            dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
            dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
            mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
            btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
            attachlbframe.place(x=740, y=5)
            htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
            lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
            btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
            btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
            lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
            lbl_tt_info.place(x=740, y=370)

            ready_frame=Frame(rpmailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
            
            sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
            sendatalbframe.place(x=5, y=5)
            lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
            sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
            lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
            nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
            lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
            replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
            lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
            signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
            confirm_chkvar=IntVar()
            confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
            confirm_chkbtn.place(x=200, y=215)
            btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

            sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
            sendatalbframe.place(x=610, y=5)
            servar=IntVar()
            SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
            SMTP_rbtn.place(x=10, y=10)
            MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=myrp_SMTP)
            MySMTP_rbtn.place(x=10, y=40)
            em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
            em_ser_conbtn.place(x=710, y=110)
        
        def my_popup(event):
            my_menu.tk_popup(event.x_root, event.y_root)
            
        my_menu= Menu(canvas, tearoff=False)
        my_menu.add_command(label="Run Report", command="run")
        my_menu.add_separator()
        my_menu.add_command(label="Print Report", command="pr")
        my_menu.add_command(label="Email Report", command=emailrp)

        my_menu.add_separator()
        my_menu.add_command(label="Export Report To Excel", command="excel")
        my_menu.add_command(label="Export Report To PDF", command="pdf")


        canvas.bind("<Button-3>", my_popup)
    #==============================================================================================================
    elif rth=="Current month":
        frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=115)
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
        canvas.config(width=1310,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text=menu1.get(),fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022     Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')

        
        def emailrp():
            rpmailDetail=Toplevel()
            rpmailDetail.title("E-Mail")
            p2 = PhotoImage(file = "images/fbicon.png")
            rpmailDetail.iconphoto(False, p2)
            rpmailDetail.geometry("1030x550+150+120")
            
            def myrp_SMTP():
                if True:
                    em_ser_conbtn.destroy()
                    mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
                    mysmtpservercon.place(x=610, y=110)
                    lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
                    hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
                    lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
                    portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
                    lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
                    unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
                    lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
                    pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
                    ssl_chkvar=IntVar()
                    ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
                    ssl_chkbtn.place(x=50, y=110)
                    em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
                else:
                    pass
            
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", padding=5)
            email_Notebook = ttk.Notebook(rpmailDetail)
            email_Frame = Frame(email_Notebook, height=500, width=1080)
            account_Frame = Frame(email_Notebook, height=550, width=1080)
            email_Notebook.add(email_Frame, text="E-mail")
            email_Notebook.add(account_Frame, text="Account")
            email_Notebook.place(x=0, y=0)
            messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
            messagelbframe.place(x=5, y=5)
            lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
            emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
            sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
            lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
            carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
            stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
            lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
            subent=Entry(messagelbframe, width=50).place(x=120, y=59)

            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
            mess_Notebook = ttk.Notebook(messagelbframe)
            emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
            htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
            mess_Notebook.add(emailmessage_Frame, text="E-mail message")
            mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
            mess_Notebook.place(x=5, y=90)

            btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
            btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
            btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
            btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
            btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
            btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
            btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
            btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
            btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
            btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
            btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

            dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
            dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
            mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
            btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
            attachlbframe.place(x=740, y=5)
            htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
            lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
            btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
            btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
            lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
            lbl_tt_info.place(x=740, y=370)

            ready_frame=Frame(rpmailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
            
            sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
            sendatalbframe.place(x=5, y=5)
            lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
            sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
            lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
            nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
            lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
            replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
            lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
            signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
            confirm_chkvar=IntVar()
            confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
            confirm_chkbtn.place(x=200, y=215)
            btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

            sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
            sendatalbframe.place(x=610, y=5)
            servar=IntVar()
            SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
            SMTP_rbtn.place(x=10, y=10)
            MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=myrp_SMTP)
            MySMTP_rbtn.place(x=10, y=40)
            em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
            em_ser_conbtn.place(x=710, y=110)
        
        def my_popup(event):
            my_menu.tk_popup(event.x_root, event.y_root)
            
        my_menu= Menu(canvas, tearoff=False)
        my_menu.add_command(label="Run Report", command="run")
        my_menu.add_separator()
        my_menu.add_command(label="Print Report", command="pr")
        my_menu.add_command(label="Email Report", command=emailrp)

        my_menu.add_separator()
        my_menu.add_command(label="Export Report To Excel", command="excel")
        my_menu.add_command(label="Export Report To PDF", command="pdf")


        canvas.bind("<Button-3>", my_popup)
        #=====================================================================================================
    elif rth=="Current days":
        frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=115)
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
        canvas.config(width=1310,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text=menu1.get(),fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022     Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')

        
        def emailrp():
            rpmailDetail=Toplevel()
            rpmailDetail.title("E-Mail")
            p2 = PhotoImage(file = "images/fbicon.png")
            rpmailDetail.iconphoto(False, p2)
            rpmailDetail.geometry("1030x550+150+120")
            
            def myrp_SMTP():
                if True:
                    em_ser_conbtn.destroy()
                    mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
                    mysmtpservercon.place(x=610, y=110)
                    lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
                    hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
                    lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
                    portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
                    lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
                    unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
                    lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
                    pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
                    ssl_chkvar=IntVar()
                    ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
                    ssl_chkbtn.place(x=50, y=110)
                    em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
                else:
                    pass
            
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", padding=5)
            email_Notebook = ttk.Notebook(rpmailDetail)
            email_Frame = Frame(email_Notebook, height=500, width=1080)
            account_Frame = Frame(email_Notebook, height=550, width=1080)
            email_Notebook.add(email_Frame, text="E-mail")
            email_Notebook.add(account_Frame, text="Account")
            email_Notebook.place(x=0, y=0)
            messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
            messagelbframe.place(x=5, y=5)
            lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
            emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
            sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
            lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
            carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
            stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
            lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
            subent=Entry(messagelbframe, width=50).place(x=120, y=59)

            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
            mess_Notebook = ttk.Notebook(messagelbframe)
            emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
            htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
            mess_Notebook.add(emailmessage_Frame, text="E-mail message")
            mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
            mess_Notebook.place(x=5, y=90)

            btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
            btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
            btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
            btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
            btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
            btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
            btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
            btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
            btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
            btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
            btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

            dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
            dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
            mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
            btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
            attachlbframe.place(x=740, y=5)
            htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
            lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
            btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
            btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
            lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
            lbl_tt_info.place(x=740, y=370)

            ready_frame=Frame(rpmailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
            
            sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
            sendatalbframe.place(x=5, y=5)
            lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
            sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
            lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
            nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
            lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
            replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
            lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
            signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
            confirm_chkvar=IntVar()
            confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
            confirm_chkbtn.place(x=200, y=215)
            btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

            sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
            sendatalbframe.place(x=610, y=5)
            servar=IntVar()
            SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
            SMTP_rbtn.place(x=10, y=10)
            MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=myrp_SMTP)
            MySMTP_rbtn.place(x=10, y=40)
            em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
            em_ser_conbtn.place(x=710, y=110)
        
        def my_popup(event):
            my_menu.tk_popup(event.x_root, event.y_root)
            
        my_menu= Menu(canvas, tearoff=False)
        my_menu.add_command(label="Run Report", command="run")
        my_menu.add_separator()
        my_menu.add_command(label="Print Report", command="pr")
        my_menu.add_command(label="Email Report", command=emailrp)

        my_menu.add_separator()
        my_menu.add_command(label="Export Report To Excel", command="excel")
        my_menu.add_command(label="Export Report To PDF", command="pdf")


        canvas.bind("<Button-3>", my_popup)
        #=================================================================================================
    elif rth=="Last 30 days":
        frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=115)
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
        canvas.config(width=1310,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text=menu1.get(),fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022     Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')

        
        def emailrp():
            rpmailDetail=Toplevel()
            rpmailDetail.title("E-Mail")
            p2 = PhotoImage(file = "images/fbicon.png")
            rpmailDetail.iconphoto(False, p2)
            rpmailDetail.geometry("1030x550+150+120")
            
            def myrp_SMTP():
                if True:
                    em_ser_conbtn.destroy()
                    mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
                    mysmtpservercon.place(x=610, y=110)
                    lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
                    hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
                    lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
                    portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
                    lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
                    unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
                    lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
                    pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
                    ssl_chkvar=IntVar()
                    ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
                    ssl_chkbtn.place(x=50, y=110)
                    em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
                else:
                    pass
            
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", padding=5)
            email_Notebook = ttk.Notebook(rpmailDetail)
            email_Frame = Frame(email_Notebook, height=500, width=1080)
            account_Frame = Frame(email_Notebook, height=550, width=1080)
            email_Notebook.add(email_Frame, text="E-mail")
            email_Notebook.add(account_Frame, text="Account")
            email_Notebook.place(x=0, y=0)
            messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
            messagelbframe.place(x=5, y=5)
            lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
            emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
            sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
            lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
            carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
            stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
            lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
            subent=Entry(messagelbframe, width=50).place(x=120, y=59)

            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
            mess_Notebook = ttk.Notebook(messagelbframe)
            emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
            htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
            mess_Notebook.add(emailmessage_Frame, text="E-mail message")
            mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
            mess_Notebook.place(x=5, y=90)

            btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
            btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
            btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
            btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
            btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
            btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
            btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
            btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
            btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
            btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
            btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

            dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
            dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
            mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
            btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
            attachlbframe.place(x=740, y=5)
            htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
            lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
            btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
            btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
            lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
            lbl_tt_info.place(x=740, y=370)

            ready_frame=Frame(rpmailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
            
            sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
            sendatalbframe.place(x=5, y=5)
            lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
            sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
            lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
            nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
            lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
            replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
            lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
            signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
            confirm_chkvar=IntVar()
            confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
            confirm_chkbtn.place(x=200, y=215)
            btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

            sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
            sendatalbframe.place(x=610, y=5)
            servar=IntVar()
            SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
            SMTP_rbtn.place(x=10, y=10)
            MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=myrp_SMTP)
            MySMTP_rbtn.place(x=10, y=40)
            em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
            em_ser_conbtn.place(x=710, y=110)
        
        def my_popup(event):
            my_menu.tk_popup(event.x_root, event.y_root)
            
        my_menu= Menu(canvas, tearoff=False)
        my_menu.add_command(label="Run Report", command="run")
        my_menu.add_separator()
        my_menu.add_command(label="Print Report", command="pr")
        my_menu.add_command(label="Email Report", command=emailrp)

        my_menu.add_separator()
        my_menu.add_command(label="Export Report To Excel", command="excel")
        my_menu.add_command(label="Export Report To PDF", command="pdf")


        canvas.bind("<Button-3>", my_popup)
    
    #=====================================================================================================
    elif rth=="Last 60 days":
        frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=115)
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
        canvas.config(width=1310,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text=menu1.get(),fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022     Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')

        
        def emailrp():
            rpmailDetail=Toplevel()
            rpmailDetail.title("E-Mail")
            p2 = PhotoImage(file = "images/fbicon.png")
            rpmailDetail.iconphoto(False, p2)
            rpmailDetail.geometry("1030x550+150+120")
            
            def myrp_SMTP():
                if True:
                    em_ser_conbtn.destroy()
                    mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
                    mysmtpservercon.place(x=610, y=110)
                    lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
                    hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
                    lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
                    portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
                    lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
                    unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
                    lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
                    pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
                    ssl_chkvar=IntVar()
                    ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
                    ssl_chkbtn.place(x=50, y=110)
                    em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
                else:
                    pass
            
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", padding=5)
            email_Notebook = ttk.Notebook(rpmailDetail)
            email_Frame = Frame(email_Notebook, height=500, width=1080)
            account_Frame = Frame(email_Notebook, height=550, width=1080)
            email_Notebook.add(email_Frame, text="E-mail")
            email_Notebook.add(account_Frame, text="Account")
            email_Notebook.place(x=0, y=0)
            messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
            messagelbframe.place(x=5, y=5)
            lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
            emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
            sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
            lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
            carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
            stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
            lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
            subent=Entry(messagelbframe, width=50).place(x=120, y=59)

            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
            mess_Notebook = ttk.Notebook(messagelbframe)
            emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
            htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
            mess_Notebook.add(emailmessage_Frame, text="E-mail message")
            mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
            mess_Notebook.place(x=5, y=90)

            btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
            btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
            btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
            btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
            btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
            btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
            btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
            btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
            btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
            btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
            btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

            dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
            dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
            mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
            btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
            attachlbframe.place(x=740, y=5)
            htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
            lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
            btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
            btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
            lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
            lbl_tt_info.place(x=740, y=370)

            ready_frame=Frame(rpmailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
            
            sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
            sendatalbframe.place(x=5, y=5)
            lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
            sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
            lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
            nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
            lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
            replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
            lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
            signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
            confirm_chkvar=IntVar()
            confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
            confirm_chkbtn.place(x=200, y=215)
            btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

            sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
            sendatalbframe.place(x=610, y=5)
            servar=IntVar()
            SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
            SMTP_rbtn.place(x=10, y=10)
            MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=myrp_SMTP)
            MySMTP_rbtn.place(x=10, y=40)
            em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
            em_ser_conbtn.place(x=710, y=110)
        
        def my_popup(event):
            my_menu.tk_popup(event.x_root, event.y_root)
            
        my_menu= Menu(canvas, tearoff=False)
        my_menu.add_command(label="Run Report", command="run")
        my_menu.add_separator()
        my_menu.add_command(label="Print Report", command="pr")
        my_menu.add_command(label="Email Report", command=emailrp)

        my_menu.add_separator()
        my_menu.add_command(label="Export Report To Excel", command="excel")
        my_menu.add_command(label="Export Report To PDF", command="pdf")


        canvas.bind("<Button-3>", my_popup)
    #========================================================================================================
    elif rth=="Last 60 days":
        frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=115)
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
        canvas.config(width=1310,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text=menu1.get(),fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022     Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')

        
        def emailrp():
            rpmailDetail=Toplevel()
            rpmailDetail.title("E-Mail")
            p2 = PhotoImage(file = "images/fbicon.png")
            rpmailDetail.iconphoto(False, p2)
            rpmailDetail.geometry("1030x550+150+120")
            
            def myrp_SMTP():
                if True:
                    em_ser_conbtn.destroy()
                    mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
                    mysmtpservercon.place(x=610, y=110)
                    lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
                    hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
                    lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
                    portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
                    lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
                    unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
                    lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
                    pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
                    ssl_chkvar=IntVar()
                    ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
                    ssl_chkbtn.place(x=50, y=110)
                    em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
                else:
                    pass
            
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", padding=5)
            email_Notebook = ttk.Notebook(rpmailDetail)
            email_Frame = Frame(email_Notebook, height=500, width=1080)
            account_Frame = Frame(email_Notebook, height=550, width=1080)
            email_Notebook.add(email_Frame, text="E-mail")
            email_Notebook.add(account_Frame, text="Account")
            email_Notebook.place(x=0, y=0)
            messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
            messagelbframe.place(x=5, y=5)
            lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
            emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
            sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
            lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
            carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
            stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
            lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
            subent=Entry(messagelbframe, width=50).place(x=120, y=59)

            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
            mess_Notebook = ttk.Notebook(messagelbframe)
            emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
            htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
            mess_Notebook.add(emailmessage_Frame, text="E-mail message")
            mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
            mess_Notebook.place(x=5, y=90)

            btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
            btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
            btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
            btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
            btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
            btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
            btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
            btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
            btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
            btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
            btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

            dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
            dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
            mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
            btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
            attachlbframe.place(x=740, y=5)
            htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
            lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
            btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
            btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
            lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
            lbl_tt_info.place(x=740, y=370)

            ready_frame=Frame(rpmailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
            
            sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
            sendatalbframe.place(x=5, y=5)
            lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
            sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
            lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
            nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
            lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
            replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
            lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
            signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
            confirm_chkvar=IntVar()
            confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
            confirm_chkbtn.place(x=200, y=215)
            btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

            sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
            sendatalbframe.place(x=610, y=5)
            servar=IntVar()
            SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
            SMTP_rbtn.place(x=10, y=10)
            MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=myrp_SMTP)
            MySMTP_rbtn.place(x=10, y=40)
            em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
            em_ser_conbtn.place(x=710, y=110)
        
        def my_popup(event):
            my_menu.tk_popup(event.x_root, event.y_root)
            
        my_menu= Menu(canvas, tearoff=False)
        my_menu.add_command(label="Run Report", command="run")
        my_menu.add_separator()
        my_menu.add_command(label="Print Report", command="pr")
        my_menu.add_command(label="Email Report", command=emailrp)

        my_menu.add_separator()
        my_menu.add_command(label="Export Report To Excel", command="excel")
        my_menu.add_command(label="Export Report To PDF", command="pdf")


        canvas.bind("<Button-3>", my_popup)
#================================================================================================================
    elif rth=="Last 90 days":
        frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=115)
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
        canvas.config(width=1310,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text=menu1.get(),fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022     Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')

        
        def emailrp():
            rpmailDetail=Toplevel()
            rpmailDetail.title("E-Mail")
            p2 = PhotoImage(file = "images/fbicon.png")
            rpmailDetail.iconphoto(False, p2)
            rpmailDetail.geometry("1030x550+150+120")
            
            def myrp_SMTP():
                if True:
                    em_ser_conbtn.destroy()
                    mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
                    mysmtpservercon.place(x=610, y=110)
                    lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
                    hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
                    lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
                    portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
                    lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
                    unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
                    lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
                    pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
                    ssl_chkvar=IntVar()
                    ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
                    ssl_chkbtn.place(x=50, y=110)
                    em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
                else:
                    pass
            
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", padding=5)
            email_Notebook = ttk.Notebook(rpmailDetail)
            email_Frame = Frame(email_Notebook, height=500, width=1080)
            account_Frame = Frame(email_Notebook, height=550, width=1080)
            email_Notebook.add(email_Frame, text="E-mail")
            email_Notebook.add(account_Frame, text="Account")
            email_Notebook.place(x=0, y=0)
            messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
            messagelbframe.place(x=5, y=5)
            lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
            emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
            sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
            lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
            carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
            stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
            lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
            subent=Entry(messagelbframe, width=50).place(x=120, y=59)

            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
            mess_Notebook = ttk.Notebook(messagelbframe)
            emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
            htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
            mess_Notebook.add(emailmessage_Frame, text="E-mail message")
            mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
            mess_Notebook.place(x=5, y=90)

            btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
            btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
            btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
            btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
            btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
            btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
            btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
            btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
            btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
            btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
            btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

            dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
            dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
            mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
            btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
            attachlbframe.place(x=740, y=5)
            htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
            lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
            btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
            btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
            lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
            lbl_tt_info.place(x=740, y=370)

            ready_frame=Frame(rpmailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
            
            sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
            sendatalbframe.place(x=5, y=5)
            lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
            sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
            lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
            nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
            lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
            replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
            lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
            signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
            confirm_chkvar=IntVar()
            confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
            confirm_chkbtn.place(x=200, y=215)
            btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

            sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
            sendatalbframe.place(x=610, y=5)
            servar=IntVar()
            SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
            SMTP_rbtn.place(x=10, y=10)
            MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=myrp_SMTP)
            MySMTP_rbtn.place(x=10, y=40)
            em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
            em_ser_conbtn.place(x=710, y=110)
        
        def my_popup(event):
            my_menu.tk_popup(event.x_root, event.y_root)
            
        my_menu= Menu(canvas, tearoff=False)
        my_menu.add_command(label="Run Report", command="run")
        my_menu.add_separator()
        my_menu.add_command(label="Print Report", command="pr")
        my_menu.add_command(label="Email Report", command=emailrp)

        my_menu.add_separator()
        my_menu.add_command(label="Export Report To Excel", command="excel")
        my_menu.add_command(label="Export Report To PDF", command="pdf")


        canvas.bind("<Button-3>", my_popup)
        #====================================================================================================
    elif rth=="Previous month":
        frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=115)
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
        canvas.config(width=1310,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text=menu1.get(),fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022     Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')

        
        def emailrp():
            rpmailDetail=Toplevel()
            rpmailDetail.title("E-Mail")
            p2 = PhotoImage(file = "images/fbicon.png")
            rpmailDetail.iconphoto(False, p2)
            rpmailDetail.geometry("1030x550+150+120")
            
            def myrp_SMTP():
                if True:
                    em_ser_conbtn.destroy()
                    mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
                    mysmtpservercon.place(x=610, y=110)
                    lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
                    hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
                    lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
                    portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
                    lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
                    unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
                    lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
                    pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
                    ssl_chkvar=IntVar()
                    ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
                    ssl_chkbtn.place(x=50, y=110)
                    em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
                else:
                    pass
            
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", padding=5)
            email_Notebook = ttk.Notebook(rpmailDetail)
            email_Frame = Frame(email_Notebook, height=500, width=1080)
            account_Frame = Frame(email_Notebook, height=550, width=1080)
            email_Notebook.add(email_Frame, text="E-mail")
            email_Notebook.add(account_Frame, text="Account")
            email_Notebook.place(x=0, y=0)
            messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
            messagelbframe.place(x=5, y=5)
            lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
            emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
            sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
            lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
            carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
            stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
            lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
            subent=Entry(messagelbframe, width=50).place(x=120, y=59)

            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
            mess_Notebook = ttk.Notebook(messagelbframe)
            emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
            htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
            mess_Notebook.add(emailmessage_Frame, text="E-mail message")
            mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
            mess_Notebook.place(x=5, y=90)

            btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
            btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
            btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
            btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
            btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
            btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
            btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
            btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
            btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
            btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
            btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

            dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
            dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
            mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
            btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
            attachlbframe.place(x=740, y=5)
            htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
            lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
            btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
            btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
            lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
            lbl_tt_info.place(x=740, y=370)

            ready_frame=Frame(rpmailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
            
            sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
            sendatalbframe.place(x=5, y=5)
            lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
            sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
            lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
            nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
            lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
            replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
            lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
            signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
            confirm_chkvar=IntVar()
            confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
            confirm_chkbtn.place(x=200, y=215)
            btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

            sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
            sendatalbframe.place(x=610, y=5)
            servar=IntVar()
            SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
            SMTP_rbtn.place(x=10, y=10)
            MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=myrp_SMTP)
            MySMTP_rbtn.place(x=10, y=40)
            em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
            em_ser_conbtn.place(x=710, y=110)
        
        def my_popup(event):
            my_menu.tk_popup(event.x_root, event.y_root)
            
        my_menu= Menu(canvas, tearoff=False)
        my_menu.add_command(label="Run Report", command="run")
        my_menu.add_separator()
        my_menu.add_command(label="Print Report", command="pr")
        my_menu.add_command(label="Email Report", command=emailrp)

        my_menu.add_separator()
        my_menu.add_command(label="Export Report To Excel", command="excel")
        my_menu.add_command(label="Export Report To PDF", command="pdf")


        canvas.bind("<Button-3>", my_popup)
        #===========================================================================================================
    elif rth=="Previous year":
        frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
        frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
        frame.place(x=20,y=115)
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
        canvas.config(width=1310,height=600)

        canvas.config(
            yscrollcommand=vertibar.set
            )
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
        canvas.create_text(375,100,text="Your Company Name",fill='black',font=("Helvetica", 12), justify='center')

        canvas.create_text(350,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
        canvas.create_text(900,100,text=menu1.get(),fill='black',font=("Helvetica", 16), justify='right')
        canvas.create_text(855,145,text="Date From:01-04-2022     Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

        canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')

        
        def emailrp():
            rpmailDetail=Toplevel()
            rpmailDetail.title("E-Mail")
            p2 = PhotoImage(file = "images/fbicon.png")
            rpmailDetail.iconphoto(False, p2)
            rpmailDetail.geometry("1030x550+150+120")
            
            def myrp_SMTP():
                if True:
                    em_ser_conbtn.destroy()
                    mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
                    mysmtpservercon.place(x=610, y=110)
                    lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
                    hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
                    lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
                    portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
                    lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
                    unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
                    lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
                    pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
                    ssl_chkvar=IntVar()
                    ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
                    ssl_chkbtn.place(x=50, y=110)
                    em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
                else:
                    pass
            
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", padding=5)
            email_Notebook = ttk.Notebook(rpmailDetail)
            email_Frame = Frame(email_Notebook, height=500, width=1080)
            account_Frame = Frame(email_Notebook, height=550, width=1080)
            email_Notebook.add(email_Frame, text="E-mail")
            email_Notebook.add(account_Frame, text="Account")
            email_Notebook.place(x=0, y=0)
            messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
            messagelbframe.place(x=5, y=5)
            lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
            emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
            sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
            lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
            carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
            stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
            lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
            subent=Entry(messagelbframe, width=50).place(x=120, y=59)

            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
            mess_Notebook = ttk.Notebook(messagelbframe)
            emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
            htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
            mess_Notebook.add(emailmessage_Frame, text="E-mail message")
            mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
            mess_Notebook.place(x=5, y=90)

            btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
            btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
            btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
            btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
            btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
            btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
            btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
            btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
            btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
            btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
            btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

            dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
            dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
            mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
            btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
            btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
            btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
            mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
            mframe.place(x=0, y=28)
            attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
            attachlbframe.place(x=740, y=5)
            htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
            lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
            btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
            btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
            lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
            lbl_tt_info.place(x=740, y=370)

            ready_frame=Frame(rpmailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
            
            sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
            sendatalbframe.place(x=5, y=5)
            lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
            sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
            lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
            nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
            lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
            replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
            lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
            signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
            confirm_chkvar=IntVar()
            confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
            confirm_chkbtn.place(x=200, y=215)
            btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

            sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
            sendatalbframe.place(x=610, y=5)
            servar=IntVar()
            SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
            SMTP_rbtn.place(x=10, y=10)
            MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=myrp_SMTP)
            MySMTP_rbtn.place(x=10, y=40)
            em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
            em_ser_conbtn.place(x=710, y=110)
        
        def my_popup(event):
            my_menu.tk_popup(event.x_root, event.y_root)
            
        my_menu= Menu(canvas, tearoff=False)
        my_menu.add_command(label="Run Report", command="run")
        my_menu.add_separator()
        my_menu.add_command(label="Print Report", command="pr")
        my_menu.add_command(label="Email Report", command=emailrp)

        my_menu.add_separator()
        my_menu.add_command(label="Export Report To Excel", command="excel")
        my_menu.add_command(label="Export Report To PDF", command="pdf")


        canvas.bind("<Button-3>", my_popup)

        #============================================================================================
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

    canvas.config(
        yscrollcommand=vertibar.set
        )
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(235,25,1025,1430,  outline='yellow',fill='white')
    
    canvas.create_text(620,300,text="No Data To Display",fill='black',font=("arial", 14), justify='center')

    canvas.create_text(625,350,text="Please sdelect the report type from the list above\nAfter you can set the date period or other parameters",fill='blue',font=("arial", 12), justify='center')

    canvas.create_text(620,400,text="Click on 'Run Report' button for the report result",fill='blue',font=("arial", 12), justify='center')

    # midFrame2=LabelFrame(frame, bg="red", width=100, height=60)
    # midFrame2.place(x=20, y=100)
    #----------------------------------------------------------------------------------------------------
  elif menuvar=="Invoice Report(With Customer)":

    #frame for display data to a a4 sheet

    rprefreshlebel_cst = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    
    rpdrop2_irwc=ttk.Combobox(midFrame, textvariable=invfilter,)
    rpdrop2_irwc["values"]=("Month to date","Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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


    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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


    rpdrop2_or=ttk.Combobox(midFrame, textvariable=invfilter,)
    rpdrop2_or["values"]=("Month to date","Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_or.place(x=530,y=50)
    rpdrop2_or.current(0)
    
    mainchartframe4 =Frame(reportframe,height=1500, width=200)
    mainchartframe4.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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

    rprefreshlebelpdi = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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


    rpdrop2_tri=ttk.Combobox(midFrame, textvariable=invfilter,)
    rpdrop2_tri["values"]=("Month to date","Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

 
    rpdrop2_tro=ttk.Combobox(midFrame, textvariable=invfilter,)
    rpdrop2_tro["values"]=("Month to date","Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_tro.place(x=530,y=50)
    rpdrop2_tro.current(0)
    
    mainchartframe13 =Frame(reportframe,height=1500, width=200)
    mainchartframe13.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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
    drop1sr=ttk.Combobox(midFrame, textvariable=menusr, width=30)
    drop1sr.place(x=530,y=10)
    drop1sr["values"]=("Java","Php", "POP")
    drop1sr.current(0)

    rpdrop2_sr=ttk.Combobox(midFrame, textvariable=invfilter,width=30)
    rpdrop2_sr["values"]=("Month to date","Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_sr.place(x=530,y=50)
    rpdrop2_sr.current(0)


    mainchartframe14 =Frame(reportframe,height=1500, width=200)
    mainchartframe14.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    rpdrop2_ird=ttk.Combobox(midFrame, textvariable=invfilter,width=30)
    rpdrop2_ird["values"]=("Month to date","Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
    rpdrop2_ird.place(x=530,y=50)
    rpdrop2_ird.current(0)


    
    mainchartframe15 =Frame(reportframe,height=1500, width=200)
    mainchartframe15.pack(side="top", padx=0, pady=0)

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    rpdrop2_por=ttk.Combobox(midFrame, textvariable=invfilter,)
    rpdrop2_por["values"]=("Month to date","Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    rpdrop2_er=ttk.Combobox(midFrame, textvariable=invfilter,width=30)
    rpdrop2_er["values"]=("Month to date","Year To Date","Current year","Current month","Current days", "Last 30 days", "Last 60 days", "Last 90 days","Previous month", "Previous year", "Custom Range")
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
    rprefreshlebel = Button(midFrame,compound="top", text="Refresh",relief=RAISED, image=photo8,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=category)
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

    irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="white")
    irwcuw1.place(x=2,y=90)


    lbl_invdtt2 =Label(reportframe, text="Report Result Preview", bg="white" , font=("arial", 16))
    lbl_invdtt2.place(x=2, y=87)
    irwcuw1 = Label(reportframe,text="                                                                                               ", bg="white")
    irwcuw1.place(x=1135, y=97)
    lbl_invdtt2 =Label(reportframe, text="Right Click on Preview For More Options", bg="white" , font=("arial",8 ))
    lbl_invdtt2.place(x=1140, y=97)

    frame = Frame(
        reportframe,
        width=1500,
        height=1000,
        bg="red"
        )
    frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
    frame.place(x=20,y=115)
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
    canvas.config(width=1310,height=600)

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
chkbtn1 = Checkbutton(lbframe, text = "Invoice", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2",command="lambda:invoicegraph()")
chkbtn1.grid(row=0, column=6, rowspan=2, padx=(0,3))

checkvar2 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Outstanding", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:outstandinggraph()")
chkbtn1.grid(row=2, column=6,rowspan=2,padx=(25,0))

checkvar3 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Paid", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command="lambda:paidgraph()")
chkbtn1.grid(row=1, column=7)








#labels




#first graph

import matplotlib.pyplot as plt
from pylab import plot, show, xlabel, ylabel
from matplotlib.widgets import Cursor

invoice=StringVar()
outstanding=StringVar()
paid=StringVar()

x=0
invoice=1200
outstanding=22
paid=14

#------------------------------------with cursor----------------
# y=float(invoice)
# x+=1
# fig, ax =plt.subplots()
# plt.bar(x,y, label="Invoice", color="orange")
# plt.legend()
# plt.xlabel("x-axis")
# plt.ylabel("y-label")
# axes=plt.gca()
# axes.yaxis.grid()
# cursor=Cursor(ax, horizOn=True, vertOn=True, color='r', linewidth=1)
# plt.show()
#-------------------------------------------------------------------------------

frame = Frame(
        reportframe,
        width=1380,
        height=1000,
        bg='red',
        )
frame.pack(expand=True, fill=BOTH,  padx=0, pady=0)
    
frame.pack()




y=float(invoice)
x+=1
figfirst = plt.figure(figsize=(17, 3.58), dpi=80)
plt.bar(x,y, label="Invoice", color="orange")
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-label")
axes=plt.gca()
axes.yaxis.grid()

# cursor=Cursor(ax, horizOn=True, vertOn=True, useblit=True, color='r', linewidth=1)

x=1
y=float(outstanding)
x+=1
plt.bar(x,y, label="Outstanding", color="blue")
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-label")
axes=plt.gca()
axes.yaxis.grid()
# cursor=Cursor(ax, horizOn=True, vertOn=True, useblit=True, color='r', linewidth=1)


x=100
y=float(paid)
x+=1
plt.bar(x,y, label="Paid", color="green") 
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-label")
axes=plt.gca()
axes.yaxis.grid()
# cursor=Cursor(ax, horizOn=True, vertOn=True, useblit=True, color='r', linewidth=1)

#used to display chart in our frame
canvasbar = FigureCanvasTkAgg(figfirst, master=frame)
canvasbar.draw()
canvasbar.get_tk_widget().place(x=0, y=0) # show the barchart on the ouput window

#second graph

figsecond = plt.figure(figsize=(9, 4), dpi=80)

x=2
y=float(paid)
x+=1
plt.barh(x,y, label="Paid", color="orange") 
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-label")
axes=plt.gca()
axes.xaxis.grid()


canvasbar = FigureCanvasTkAgg(figsecond, master=reportframe)
canvasbar.draw()
canvasbar.get_tk_widget().place(x=0, y=370)

# #second graph

figlast = plt.figure(figsize=(9, 4), dpi=80)

x=2
y=float(paid)
x+=1
plt.barh(x,y, label="Paid", color="blue") 
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-label")
axes=plt.gca()
axes.xaxis.grid()
 

canvasbar = FigureCanvasTkAgg(figlast, master=reportframe)
canvasbar.draw()
canvasbar.get_tk_widget().place(x=650, y=370)



# irwcuw1 = Label(reportframe,text="                                                                                                                                                               \n", bg="#f5f3f2") 
# irwcuw1.place(x=2,y=95)


lbl_invdtt2 =Label(reportframe, text="Screen Charts", bg="white" , font=("arial", 16))
lbl_invdtt2.place(x=2, y=85)
  
root.mainloop()