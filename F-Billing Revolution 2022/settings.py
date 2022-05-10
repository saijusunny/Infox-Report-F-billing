from ast import pattern
from calendar import c
from cgitb import enable, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD
from urllib.parse import parse_qs
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json


fbilldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="fbillingsintgrtd", port="3306"
)
fbcursor = fbilldb.cursor()

ImageFile.LOAD_TRUNCATED_IMAGES = True

def reset():
  global root
  root.destroy()


# root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
def log():
    global user_name1
    user_name1=username1.get()
    passwd1=password1.get()
    if user_name1=="" or passwd1=="":
        Label(text='Plz enter both username and password',fg='red').place(x=85,y=260)
    else:
        sql='SELECT * FROM users WHERE username=%s AND password=%s'
        val=(user_name1,passwd1,)
        fbcursor.execute(sql,val)
        if fbcursor.fetchone()is not None:
            mainpage()
            if user_name1 != "adminstator":
              tab06.destroy()
            else:
              pass
            root.iconify()
        else:
            messagebox.showinfo('Acess denied','Username Or Password Wrong')

  
sql = "select * from users"
fbcursor.execute(sql)
user_log = fbcursor.fetchall()
if not user_log:
  def lo():
    mainpage()
  root=Tk()
  root.geometry("500x250")
  root.resizable(False, False)
  root.eval('tk::PlaceWindow . center')
  Label(text='Wellocome to F-Billing Revolution 2022',font='arial 13 bold').place(x=100,y=40)
  submitbtn1=Button(text='OPEN NOW', width=20,height=2,command=lo,activeforeground="white",activebackground="black",font='arial 8 bold').place(x=165,y=100)             
else:
    root=Tk()
    root.geometry("500x200")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.title("F-Billing Revolution 2022")
    p1 = PhotoImage(file = 'images/fbicon.png')
    root.iconphoto(False,p1)
    username1=StringVar()
    password1=StringVar()

    Label(text='Login F-Billing Revolution 2022',font='arial 13 bold').place(x=120,y=15)
    
  
    sql = "select username from users"
    fbcursor.execute(sql)
    user_log_name = fbcursor.fetchall()
    uss1=Label(text='Username').place(x=120,y=65)
    ee1 = ttk.Combobox(textvariable=username1)
    ee1.place(x=220,y=65)
    ee1["values"] = user_log_name

    pss1=Label(text='Password').place(x=120,y=105)
    ee2=Entry(textvariable=password1,show='*',width=23).place(x=220,y=105)
    
    submitbtn1=Button(text='Login', width=15,command=log,activeforeground="white",
                   activebackground="black").place(x=250,y=150)
    
  
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
def mainpage():
  root.iconify()
  main = Toplevel()
  main.geometry("1360x730")
  p1 = PhotoImage(file = 'images/fbicon.png')
  main.iconphoto(False, p1)
  main.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
  s = ttk.Style()
  s.theme_use('default')
  s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
  tabControl = ttk.Notebook(main)
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
  
  

  
  # def log():
  #   global user_name1
  #   user_name1=username1.get()
  #   passwd1=password1.get()
  #   if user_name1=="" or passwd1=="":
  #       Label(screen2,text='Plz enter both username and password',fg='red').place(x=85,y=260)
  #   else:
  #       sql='SELECT * FROM users WHERE username=%s AND password=%s'
  #       val=(user_name1,passwd1,)
  #       fbcursor.execute(sql,val)
  #       if fbcursor.fetchone()is not None:
  #           root(user_name1)
  #       else:
  #           messagebox.showinfo('Acess denied','Acess denied')
  
  # sql = "select * from users"
  # fbcursor.execute(sql)
  # user_log = fbcursor.fetchall()
  # if not user_log:
  #   pass
  # else:
  #     screen2=Toplevel()
  #     screen2.title('LOGIN')
  #     screen2.geometry('400x300')
  
  #     username1=StringVar()
  #     password1=StringVar()
  
  #     Label(screen2,text='Login Here').pack()
  #     uss1=Label(screen2,text='Username').place(x=50,y=70)
  #     ee1 = Entry(screen2,textvariable=username1).place(x=140,y=70)
  
  #     pss1=Label(screen2,text='Password').place(x=50,y=110)
  #     ee2=Entry(screen2,textvariable=password1).place(x=140,y=110)
  
  #     submitbtn1=Button(screen2,text='Login', width=20,height=2,command=log).place(x=70,y=200)
  
  def check_empty() :
       if entry.get():
           pass     #your function where you want to jump
       else:
          messagebox.showinfo("Information", "Required entry")
  
  
  ######################## FRONT PAGE OF CUSTOMER SECTION   #######################################################################
  
      
  settingsframe=Frame(tab10, relief=GROOVE, bg="#f8f8f2")
  settingsframe.pack(side="top", fill=BOTH)
  
  settframe=Frame(settingsframe, bg="#f5f3f2", height=60)
  settframe.pack(side="top", fill=X)
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(5, 2))
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  # def upload_filelogo():
  #   global imglogo,filename
  #   f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
  #   filena = filedialog.askopenfilename(filetypes=f_types)
  #   shutil.copyfile(filena, os.getcwd()+'/images/'+filena.split('/')[-1])
  #   print(filena.split('/')[-1])
  #   image = Image.open(filena)
  #   resize_image = image.resize((280, 160))
  #   imglogo = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
  
    # btlogo = Button(secondtab,width=280,height=160,image=imglogo)
    # btlogo.place(x=580,y=280)
  global filename
  filename = ""
  def save_company():
    company_name = comname.get()
    company_address = caddent.get(1.0,END)
    company_mail = comemail.get()
    company_salestax =comsalestax.get()
    currency = comcur.get()
    currencysign = comcursign.get()
    currencysign_placement = comcursignpla.get()
    decimal_sepator = comdecsep.get()
    currency_example = comex.get()
    date_format = comdaf.get()
    example_dateformat = exd.get_date()
    tax = radtax.get()
    tax1name = tax1namee.get()
    tax1rate = tax1ratee.get()
    printtax1 = comptax1.get()
    tax2name = tax2namee.get()
    tax2rate = tax2ratee.get()
    printtax2 = comptax2.get()
    printimage = compimg.get()
    win_menu_colour = win_menu.get()
    radiobut = radema.get()
    cbut1 = checkb1.get()
    cbut2 = checkb2.get()
    cbut3 = checkb3.get()
    cbut4 = checkb4.get()
    cbut5 = checkb5.get()
    cbut6 = checkb6.get()
    child = exctree.get_children()
    var = json.dumps(child)
    sql = "select image from company"
    fbcursor.execute(sql)
    im = fbcursor.fetchone()
    sql = "select * from company"
    fbcursor.execute(sql)
    i = fbcursor.fetchall()
    if not i:
      if filename == "":
        print(12)
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,image,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6)
        fbcursor.execute(sql, val)
        fbilldb.commit()
    else:
      if filename == "":
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,image=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      
      
  
  addcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_add.png"))
  addcustomerLabel = Button(settframe,compound="top", text="Save\nSettings",relief=RAISED,    command=save_company, image=saves, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  addcustomerLabel.pack(side="left", pady=3, ipadx=4)
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  
  editcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_edit.png"))
  editcustomerLabel =  Button(settframe,compound="top", text="Save\nSettings",relief=RAISED,    command='', image=editcustomerIcon, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  addcustomerLabel.pack(side="left", pady=3, ipadx=4)
  editcustomerLabel.pack(side="left")
  
  deletecustomerIcon = ImageTk.PhotoImage(Image.open("images/user_delete.png"))
  deletecustomerLabel = Button(settframe,compound="top", text="Company\nManager",relief=RAISED, command="",  image=deletecustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  deletecustomerLabel.pack(side="left")
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=5)
  
  previewinvoiceIcon = ImageTk.PhotoImage(Image.open("images/priewok.png"))
  previewinvoiceLabel = Button(settframe,compound="top",command="", text="Optimize\nData tables",  relief=RAISED,               image=previewinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black",   height=55, bd=1, width=55)
  previewinvoiceLabel.pack(side="left")
  
  printinvoiceIcon = ImageTk.PhotoImage(Image.open("images/printer.png"))
  printinvoiceLabel = Button(settframe,compound="top", text="Repair\nDatabase",relief=RAISED,  command="",   image=printinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  printinvoiceLabel.pack(side="left")
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=5)
  
  emailinviceIcon = ImageTk.PhotoImage(Image.open("images/gmail.png"))
  emailinviceLabel = Button(settframe,compound="top",command="", text="Backup\nDatabase",  relief=RAISED,               image=emailinviceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55,   bd=1, width=55)
  emailinviceLabel.pack(side="left")
  
  refreshcustomerIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
  refreshcustomerLabel = Button(settframe,compound="top", command="",text="Restore\nDatabase",  relief=RAISED,               image=refreshcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black",   height=55, bd=1, width=55)
  refreshcustomerLabel.pack(side="left")
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=5)
  
  smsIcon = ImageTk.PhotoImage(Image.open("images/text-message.png"))
  smsLabel = Button(settframe,compound="top", text="Serach\nfor Updates",command="", relief=RAISED,   image=smsIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  smsLabel.pack(side="left")
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=5)
  
  importcustomerIcon = ImageTk.PhotoImage(Image.open("images/import.png"))
  importcustomerLabel = Button(settframe,compound="top", text="Enter licence\nKey Code",command="",  relief=RAISED, image=importcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1,   width=55)
  importcustomerLabel.pack(side="left")
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=5)
  
  exportcustomerIcon = ImageTk.PhotoImage(Image.open("images/export.png"))
  exportcustomerLabel = Button(settframe,compound="top", text="Online\nUser Manual",command="",relief=RAISED,   image=exportcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  exportcustomerLabel.pack(side="left")
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=5)
  
  customersearchIcon = ImageTk.PhotoImage(Image.open("images/search-icon.png"))
  customersearchLabel = Button(settframe,compound="top",command="", text="Upgrade to\nPro Now!",  relief=RAISED,               image=customersearchIcon, font=("arial", 8),bg="#f8f8f2", fg="black",   height=55, bd=1, width=55)
  customersearchLabel.pack(side="left")
  
  
  invoi1label = Label(settingsframe, text="Settings", font=("arial", 18), bg="#f8f8f2")
  invoi1label.pack(side="left", padx=(20,0))
  
  global tab06
  m = ttk.Style()
  m.theme_use('default')
  m.configure('one.TNotebook.Tab', background="white", width=20, padding=10)
  tabControl = ttk.Notebook(tab10,style='one.TNotebook.Tab')
  tab01 = ttk.Frame(tabControl)
  tab02 = ttk.Frame(tabControl)
  tab03=  ttk.Frame(tabControl)
  tab04 = ttk.Frame(tabControl)
  tab05 = ttk.Frame(tabControl)
  tab06=  ttk.Frame(tabControl)
  tab07 = ttk.Frame(tabControl)
  tab08 = ttk.Frame(tabControl)
  tab09 =  ttk.Frame(tabControl)
  tab010=  ttk.Frame(tabControl)
  tabControl.add(tab01,image=invoices,compound = LEFT, text ='Miscellaneous',)
  tabControl.add(tab02,image=orders,compound = LEFT, text ='Company settings')
  tabControl.add(tab03,image=estimates,compound = LEFT, text ='Invoiced settings')
  tabControl.add(tab04,image=recurring,compound = LEFT, text ='Order settings')
  tabControl.add(tab05,image=purchase,compound = LEFT, text ='Estimate settings') 
  tabControl.add(tab06,image=expenses,compound = LEFT, text ='Administrator panel')
  tabControl.add(tab07,image=customer,compound = LEFT, text ='Advanced settings')
  tabControl.add(tab08,image=product,compound = LEFT, text ='Email templates')
  tabControl.add(tab09,image=reports,compound = LEFT, text ='Payments')
  tabControl.add(tab010,image=setting,compound = LEFT, text ='Purchase Order')
  tabControl.pack(expand = 1, fill ="both")
  
  ################### tab01 ###################################
  sql = "select * from company"
  fbcursor.execute(sql)
  sectab = fbcursor.fetchone()
  
  firsttab1=Frame(tab01, relief=GROOVE, bg="#f8f8f2")
  firsttab1.pack(side="top", fill=BOTH)
  
  firsttab=Frame(firsttab1, bg="#f5f3f2", height=700)
  firsttab.pack(side="top", fill=BOTH)
  
  messagelbframe=LabelFrame(firsttab,text="Menu and Window Color Style", height=60, width=180)
  messagelbframe.place(x=5, y=15)
  
  win_menu = StringVar()
  winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
  winstyle.place(x=22 ,y=40)
  winstyle['values'] = ('whidbey','windows XP','windows 7','windows 8','windows 10')
  winstyle.current(0)
  fbill = Label(firsttab,text="F-Billing Revolution 2022",font="arial 12 bold").place(x=220,y=20)
  
  dbhost=LabelFrame(firsttab,text="Database Server Hostname", height=60, width=415)
  dbhost.place(x=5, y=85)
  
  db = Label(firsttab, text="DESKTOP-2K")
  db.place(x=15,y=110)
  
  exc=LabelFrame(firsttab,text="Extra cost name", height=180, width=415)
  exc.place(x=5, y=155)
  
  
  
  def insert_valueexc():
    i = varexc.get()
    if i == "":
      pass
    else:
      entryexc.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into extra_cost_name(companyid,extra_cost_name) values(%s,%s)'
        val = (companyid,i)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in exctree.get_children():
          exctree.delete(record)
        sql = 'select * from extra_cost_name'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          immm = str(i[2])
          imn = str.replace(immm," ","_")
          exctree.insert(parent='', index='end', iid=countp, text='hello', values=(imn))
          countp += 1
  # new_value = String
        
        
  
  def edit_valueexc(event):
    selected_item = exctree.selection()[0]
    temp = list(exctree.item(selected_item , 'values'))
    entryexc.delete(0, END)
    entryexc.insert(0, temp)
  
  def save_valueexc():
    i = entryexc.get()
    if i == "":
      pass
    else:
      selected0 = exctree.focus()
      valuz1= exctree.item(selected0)["values"]
      idgettingextracnid=valuz1[0]
      print(i,idgettingextracnid)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update extra_cost_name set extra_cost_name=%s where extra_cost_name=%s'
        val = (i,idgettingextracnid)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        entryexc.delete(0, END)
        for record in exctree.get_children():
            exctree.delete(record)
        fbcursor.execute("select *  from extra_cost_name")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          immm = str(i[2])
          imn = str.replace(immm," ","_")
          exctree.insert('', index='end', iid=countp, text='', values=(imn))
          countp += 1
    
    
  
  def del_valueexc():
    itemid = exctree.item(exctree.focus())["values"][0]
    sql = "delete from extra_cost_name where extra_cost_name = %s"
    val = (itemid, )
    fbcursor.execute(sql, val)
    fbilldb.commit()
    exctree.delete(exctree.selection()[0])
      
      
  
    
    
    
  
  
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  exctree = ttk.Treeview(firsttab, columns=("1"),height=40,selectmode='browse', yscrollcommand=scrollbary.set,   xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=exctree.yview)
  scrollbary.place(x=394,y=200,height=125)
  scrollbarx.config(command=exctree.xview)
  scrollbarx.place(x=15,y=310, width=380)
  exctree.heading('1', text="Extra cost name",)
  # exctree.column('#0', stretch=NO, minwidth=0, width=0)
  exctree.column("#0",width=0,anchor='c', stretch=False)
  exctree.column('1',width=378,anchor='c')
  exctree.place(x=15,y=200,height=115,width=380)
  exctree.bind('<Double-Button-1>' , edit_valueexc)
  sql = 'select * from extra_cost_name'
  fbcursor.execute(sql)
  setexctree = fbcursor.fetchall()
  countp = 0
  for i in setexctree:
      print(i[2])
      immm = str(i[2])
      imn = str.replace(immm," ","_")
      exctree.insert(parent='', index='end', iid=countp, text='', values=(imn))
      countp += 1
  # new_value = StringVar()
  
  # def edit_window_box(val):
      
  #     edit_window = Toplevel(root)
  #     edit_window.title("Edit the value or cancel")
  #     edit_window.geometry("1000x250")
  #     label_edit = Label(edit_window , text='Enter value to edit or press cancel', 
  #     font = ("Times New Roman", 10)).grid(column=0,row=1,padx=0, pady = 2)
  #     #create edit box
  #     edit_box = Entry(edit_window)
  #     edit_box.insert(0,val)
  #     edit_box.grid(column=1,row=1,padx=0,pady=2)
  #     #auto select edit window 
  #     edit_window.focus()
      
  #     def value_assignment(event):
  #         printing = edit_box.get()
  #         new_value.set(printing)
  #         #only destroy will not update the value (perhaps event keeps running in background)
  #         #quit allows event to stop n update value in tree but does not close the window in single click 
  #         #rather on dbl click shuts down entire app 
  #         edit_window.quit()
  #         edit_window.destroy()
      
  #     edit_window.bind('<Return>', value_assignment )
  
  #     B1 = Button(edit_window, text="Okay")
  #     B1.bind('<Button-1>',value_assignment)
  #     B1.grid(column=0,row=10,padx=0, pady = 20)
      
  #     B2 = Button(edit_window, text="Cancel", command = edit_window.destroy).grid(column=1,row=10,padx=10,   pady = 20)
  #     edit_window.mainloop()
      
  # #will explain
  # #variable to hold col value (col clicked)
  # shape1 = IntVar()
  # #tracks both col , row on mouse click
  # def tree_click_handler(event):
  #     cur_item = exctree.item(exctree.focus())
  #     col = exctree.identify_column(event.x)[1:]
  #     rowid = exctree.identify_row(event.y)[1:]
  #     #updates list
  #     shape1.set(col)
  #     try:
  #         x,y,w,h = exctree.bbox('I'+rowid,'#'+col)
  #     except:pass
  #     #tree.tag_configure("highlight", background="yellow")
  #     return(col)
      
  # #code linked to event    
  # exctree.bind('<ButtonRelease-1>', tree_click_handler)
  
  # def edit(event):
  #     try:
  #         selected_item = exctree.selection()[0]
  #         temp = list(exctree.item(selected_item , 'values'))
  #         tree_click_handler
  #         col_selected = int(shape1.get())-1
  #         edit_window_box(temp[col_selected])
  #         #do not run if edit window is open
  #         #use edit_window.mainloop() so value assign after window closes
  #         temp[col_selected] = new_value.get()
  #         exctree.item(selected_item, values= temp)
  #     except: pass
      
      
  # #binding allows to edit on screen double click
  # exctree.bind('<Double-Button-1>' , edit)
  varexc = StringVar()
  entryexc = Entry(firsttab,width=25,textvariable=varexc)
  entryexc.place(x=15,y=173)
  
  btexcadd = Button(firsttab,text="Add new line",command=insert_valueexc)
  btexcadd.place(x=175,y=171)
  
  btexcedit = Button(firsttab,text="Edit line   ",command=save_valueexc)
  btexcedit.place(x=260,y=171)
  btexcadd = Button(firsttab,text=" Delete line  ",command=del_valueexc)
  btexcadd.place(x=330,y=171)
  
  exc=LabelFrame(firsttab,text="Predefined text records for header and footer", height=180, width=415)
  exc.place(x=5, y=350)
  
  def insert_valuepre():
    i = prestr.get()
    if i == "":
      pass
    else:
      entrypre.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into header_and_footer(companyid,headerandfooter) values(%s,%s)'
        val = (companyid,i)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in pretree.get_children():
          pretree.delete(record)
        sql = 'select * from header_and_footer'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          pret = str(i[2])
          pre = str.replace(pret," ","_")
          pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
          countp += 1
  # new_value = String
        
        
  
  def edit_valuepre(event):
    selected_item = pretree.selection()[0]
    temp = list(pretree.item(selected_item , 'values'))
    entrypre.delete(0, END)
    entrypre.insert(0, temp)
  
  def save_valuepre():
    i = prestr.get()
    if i == "":
      pass
    else:
      selected0 = pretree.focus()
      valuz1= pretree.item(selected0)["values"]
      idgettingextracnid=valuz1[0]
      print(i,idgettingextracnid)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update header_and_footer set headerandfooter=%s where headerandfooter=%s'
        val = (i,idgettingextracnid)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        entryexc.delete(0, END)
        for record in pretree.get_children():
            pretree.delete(record)
        fbcursor.execute("select *  from header_and_footer")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          pret = str(i[2])
          pre = str.replace(pret," ","_")
          pretree.insert('', index='end', iid=countp, text='', values=(pre))
          countp += 1
    
    
  
  def del_valuepre():
    itemid = pretree.item(pretree.focus())["values"][0]
    print(itemid)
    sql = "delete from header_and_footer where headerandfooter = %s"
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    for record in pretree.get_children():
      pretree.delete(record)
    fbcursor.execute("select *  from header_and_footer")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      pret = str(i[2])
      pre = str.replace(pret," ","_")
      pretree.insert('', index='end', iid=countp, text='', values=(pre))
      countp += 1
    
      
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  pretree = ttk.Treeview(firsttab, columns=("1"),height=400,     selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=pretree.yview)
  scrollbary.place(x=395,y=400,height=115)
  scrollbarx.config(command=pretree.xview)
  scrollbarx.place(x=15,y=510, width=380)
  pretree.heading('1', text="header and footer",)
  pretree.column('#0', stretch=NO, minwidth=0, width=0)
  pretree.column('1', stretch=NO, width=378)
  pretree.place(x=15,y=400,height=115,width=380)
  pretree.bind('<Double-Button-1>' , edit_valuepre)
  sql = 'select * from header_and_footer'
  fbcursor.execute(sql)
  setexctree = fbcursor.fetchall()
  countp = 0
  for i in setexctree:
    pret = str(i[2])
    pre = str.replace(pret," ","_")
    pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
    countp += 1
  prestr = StringVar()
  entrypre = Entry(firsttab,width=25,textvariable=prestr)
  entrypre.place(x=15,y=370)
  btexcadd = Button(firsttab,text="Add new line",command=insert_valuepre)
  btexcadd.place(x=175,y=370)
  btpredit = Button(firsttab,text="Edit line   ",command=save_valuepre)
  btpredit.place(x=260,y=370)
  btexcadd = Button(firsttab,text=" Delete line   ",command=del_valuepre)
  btexcadd.place(x=330,y=370)
  
  ver = Label(firsttab,text="FREE version.Upgrade PRO version for all features and Ad free invoice")
  ver.place(x=480,y=15)
  
  
  chapass=LabelFrame(firsttab,text="Change Password", height=150, width=500)
  chapass.place(x=480, y=40)
  
  enterold = StringVar()
  lenold = Label(firsttab,text="Enter your old password")
  lenold.place(x=495,y=60)
  enold = Entry(firsttab,textvariable=enterold)
  enold.place(x=640,y=60)
  
  enternew = StringVar()
  ennew = Label(firsttab,text="New password")
  ennew.place(x=495,y=90)
  newpass = Entry(firsttab,textvariable=enternew)
  newpass.place(x=640,y=90)
  
  
  cnewpass = StringVar()
  cnp = Label(firsttab,text="Confirm new password")
  cnp.place(x=495,y=120)
  cnewp = Entry(firsttab,textvariable=cnewpass)
  cnewp.place(x=640,y=120)

  def change_pass():
    old_pass = enterold.get()
    new_pass = enternew.get()
    cnew_pass = cnewpass.get()
    usna = username1.get()
    print(usna)
    sql='SELECT * FROM users WHERE username=%s'
    val=(usna,)
    fbcursor.execute(sql,val)
    chpass = fbcursor.fetchone()
    print(chpass)
    if old_pass == "" or new_pass == "" or cnew_pass == "":
        messagebox.showerror('Password Error','Plz enter password')
    elif old_pass == chpass[4]:
      if new_pass == cnew_pass:
        sqll='UPDATE users SET password=%s,confirm_password=%s WHERE userID=%s'
        vall=(new_pass,cnew_pass,chpass[0])
        fbcursor.execute(sqll,vall,)
        fbilldb.commit()
        messagebox.showinfo('Updated','Password updated successfully')
      else:
        messagebox.showerror('Password Error','password is not match')
    else:
      messagebox.showerror('Password Error','Old Password is Incorrect')
  chabtn = Button(firsttab,text="Change password",command=change_pass)
  chabtn.place(x=840,y=150)
  
  termf=LabelFrame(firsttab,text="Terms of payment", height=150, width=500)
  termf.place(x=480, y=190)


  def insert_valueterm():
    first = entrytopstr.get()
    second = entrydsstr.get()
    if first == "" or second == "":
      pass
    else:
      entrytop.delete(0, END)
      entryds.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into terms_of_payment(companyid,terms_of_payment,Date_shift) values(%s,%s,%s)'
        val = (companyid,first,second)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in termtree.get_children():
          termtree.delete(record)
        sql = 'select * from terms_of_payment'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          
          termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
          countp += 1
  # new_value = String
        
        
  
  def edit_valueterm(event):
    itemid = termtree.item(termtree.focus())["values"][0]
    sql = "select * from terms_of_payment where terms_of_payment = %s"
    val = (itemid,)
    fbcursor.execute(sql,val)
    editterm = fbcursor.fetchone()
    entrytop.delete(0, END)
    entryds.delete(0, END)
    entrytop.insert(0, editterm[2])
    entryds.insert(0, editterm[3])
  
  def save_valueterm():
    first = entrytopstr.get()
    second = entrydsstr.get()
    if first == "" or second == "":
      pass
    else:
      itemid = termtree.item(termtree.focus())["values"][0]
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        pass
      else:
        sql = "select * from terms_of_payment where terms_of_payment=%s"
        val = (itemid,)
        fbcursor.execute(sql,val)
        payt = fbcursor.fetchone()
        sql2 = 'update terms_of_payment set terms_of_payment=%s,Date_shift=%s where terms_of_paymentID=%s'
        val2 = (first,second,payt[0])
        fbcursor.execute(sql2,val2)
        fbilldb.commit()
        entrytop.delete(0, END)
        entryds.delete(0, END)
        for record in termtree.get_children():
          termtree.delete(record)
        fbcursor.execute("select *  from terms_of_payment")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          
          termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
          countp += 1
    
    
  
  def del_valueterm():
    itemid = termtree.item(termtree.focus())["values"][0]
    print(itemid)
    sql = "delete from terms_of_payment where terms_of_payment = %s"
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    for record in termtree.get_children():
        termtree.delete(record)
    fbcursor.execute("select *  from terms_of_payment")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
      countp += 1
  
  
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  termtree = ttk.Treeview(firsttab, columns=("1","2"),height=400,selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=termtree.yview)
  scrollbary.place(x=870,y=228,height=100)
  scrollbarx.config(command=termtree.xview)
  scrollbarx.place(x=495,y=313, width=380)
  termtree.heading('1', text="Terms of payment",)
  termtree.heading('2', text="Date shift (days)",)
  termtree.column('#0', stretch=NO, minwidth=0, width=0)
  termtree.column('1', stretch=NO, minwidth=0, width=250)
  termtree.column('2', stretch=NO, minwidth=0, width=128)
  termtree.place(x=495,y=235,height=80,width=380)
  termtree.bind('<Double-Button-1>' , edit_valueterm)

  sql = 'select * from terms_of_payment'
  fbcursor.execute(sql)
  termt = fbcursor.fetchall()
  countp = 0
  for i in termt:
      termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
      countp += 1
  entrytopstr = StringVar()
  entrytop = Entry(firsttab,width=25,textvariable=entrytopstr)
  entrytop.place(x=495,y=208)
  entrydsstr = StringVar()
  entryds = Entry(firsttab,textvariable=entrydsstr)
  entryds.place(x=670,y=208)
  bttermadd = Button(firsttab,text="Add new line",command=insert_valueterm)
  bttermadd.place(x=800,y=205)
  bttermedit = Button(firsttab,text="     Edit line  ",command=save_valueterm)
  bttermedit.place(x=890,y=205)
  bttermdel = Button(firsttab,text="  Delete line  ",command=del_valueterm)
  bttermdel.place(x=890,y=240)
  
  radem=LabelFrame(firsttab,text="Invoice/Oder/Estimate/P.order Email Attachment file type", height=60,   width=500)
  radem.place(x=480, y=340)
  radema = StringVar()
  radpdf = Radiobutton(firsttab,variable=radema,value="PDF",text='PDF')
  radpdf.place(x= 485, y= 360 )
  radhtml = Radiobutton(firsttab,variable=radema,value="HTML",text='HTML')
  radhtml.place(x= 660, y= 360 )
  if  not sectab:
    pass
  else:
    if sectab[22] == 'PDF':
      radpdf.select()
    else:
      radhtml.select()
  
  checkb1 = IntVar()
  check1 = Checkbutton(firsttab,variable = checkb1, 
                        text="PDF attachment with Embedded Fonts (PDF file size will be larger,but readable on   all devices) ", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  
  check1.place(x=480,y=400)
  if  not sectab:
    pass
  else:
    if sectab[23] == 1:
      check1.select()
    else:
      check1.deselect()
  
  checkb2 = IntVar()
  check2 = Checkbutton(firsttab,variable = checkb2, 
                        text="invoice numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                       )
  
  check2.place(x=480,y=420)
  if  not sectab:
    pass
  else:
    if sectab[24] == 1:
      check2.select()
    else:
      check2.deselect()
  
  checkb3 = IntVar()
  check3 = Checkbutton(firsttab,variable = checkb3, 
                        text="Order numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  
  check3.place(x=480,y=440)
  if  not sectab:
    pass
  else:
    if sectab[25] == 1:
      check3.select()
    else:
      check3.deselect()
  
  checkb4 = IntVar()
  check4 = Checkbutton(firsttab,variable = checkb4, 
                        text="Estimate numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                       )
  
  check4.place(x=480,y=460)
  if  not sectab:
    pass
  else:
    if sectab[26] == 1:
      check4.select()
    else:
      check4.deselect()
  
  checkb5 = IntVar()
  check5 = Checkbutton(firsttab,variable = checkb5, 
                        text="Purchsae order numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  check5.place(x=480,y=480)
  if  not sectab:
    pass
  else:
    if sectab[27] == 1:
      check5.select()
    else:
      check5.deselect()
  
  checkb6 = IntVar()
  check6 = Checkbutton(firsttab,variable = checkb6, 
                        text="Confirmation before closing F-billing Revolution", 
                        onvalue =1 ,
                        offvalue = 0,
                      )
  
  check6.place(x=480,y=500)
  if  not sectab:
    pass
  else:
    if sectab[28] == 1:
      check6.select()
    else:
      check6.deselect()
  
  ################### tab02 ###################################
  sql = "select * from company"
  fbcursor.execute(sql)
  sectab = fbcursor.fetchone()
  print(sectab)
  
  
  secondtab1=Frame(tab02, relief=GROOVE, bg="#f8f8f2")
  secondtab1.pack(side="top", fill=BOTH)
  
  secondtab=Frame(secondtab1, bg="#f5f3f2", height=700)
  secondtab.pack(side="top", fill=BOTH)
  
  comdata=LabelFrame(secondtab,text="Company data", height=200, width=500)
  comdata.place(x=5, y=15)
  cname = Label(secondtab,text="Company name")
  cname.place(x=20, y =35)
  comname = StringVar()
  centry = Entry(secondtab,textvariable=comname)
  if  not sectab:
    pass
  else:
    centry.insert(0, sectab[1])
  centry.place(x=160,y=35,width=280)
  
  
  cadd = Label(secondtab,text="Company Address")
  cadd.place(x=20, y =65)
  caddent = scrolledtext.ScrolledText(secondtab)
  if  not sectab:
    pass
  else:
    caddent.insert('1.0', sectab[2])
  caddent.place(x=160,y=65,height=80,width=280)
  
  cemail = Label(secondtab,text="E-mail Address")
  cemail.place(x=20, y =160)
  comemail = StringVar()
  cemailentry = Entry(secondtab,textvariable=comemail)
  if  not sectab:
    pass
  else:
    cemailentry.insert(0, sectab[3])
  cemailentry.place(x=160,y=160,width=280)
  
  stl = Label(secondtab,text="sales Tax.Reg.No.")
  stl.place(x=20, y =185)
  comsalestax = IntVar()
  ste = Entry(secondtab,textvariable=comsalestax)
  if  not sectab:
    pass
  else:
    ste.insert(0, sectab[4])
  ste.place(x=160,y=185,width=280)
  
  
  curre=LabelFrame(secondtab,text="Currency", height=125, width=500)
  curre.place(x=5, y=220)
  currl = Label(secondtab,text="Currency")
  currl.place(x=20,y= 240)
  comcur = StringVar()
  currbox = ttk.Combobox(secondtab,width=10,textvariable=comcur)
  currbox['values'] =('ALL','AFN','ARS','AWG','AUD','AZN','BSD','BBD','BYN','BZD','BMD','BOB','BAM','BWP',  'BGN','BRL','BND','KHR','CAD','KYD','CLP','CNY','COP','CRC','HRK','CUP','CZK','DKK','DOP','XCD','EGP','SVC',  'EUR','FKP','FJD','GHS','GIP','GTQ','GGP','GYD','HNL','HKD','HUF','ISK','INR','IDR','IRR','IMP','ILS','JMD',  'JPY','JEP','KZT','KPW','KRW','KGS','LAK','LBP','LRD','MKD','MYR','MUR','MXN','MNT','MNT','MZN','NAD','NPR',  'ANG','NZD','NIO','NGN','NOK','OMR','PKR','PAB','PYG','PEN','PHP','PLN','QAR','RON','RUB','SHP','SAR','RSD',  'SCR','SGD','SBD','SOS','KRW','ZAR','LKR','SEK','CHF','SRD','SYP','TWD','THB','TTD','TRY','TVD','UAH','AED',  'GBP','USD','UYU','UZS','VEF','VND','YER','ZWD',)
  if  not sectab:
    pass
  else:
    currbox.insert(0, sectab[5])
  currbox.place(x=80,y=240)
  
  def signpl(event):
    amsgpl = comcursignpla.get()
    currsign = comcursign.get()
    if amsgpl == "before amount":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'8347.26')
    elif amsgpl == "after amount":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26'+currsign)
    elif amsgpl == "before amount with space":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'  8347.26')
    elif amsgpl == "after amount with space":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26  '+currsign)
  
  
  currsignl = Label(secondtab,text="Currency sign")
  currsignl.place(x=180,y=240)
  comcursign = StringVar()
  currsignbox = ttk.Combobox(secondtab,width=10,textvariable=comcursign)
  currsignbox.bind("<<ComboboxSelected>>", signpl)
  currsignbox["values"] = ('Lek','؋','$','ƒ','$','₼','$','$','Br','BZ$','$','$b','KM','P','лв','R$','$','៛',  '$','$','$','¥','$','₡','kn','₱','Kč','kr','RD$','$','£','$','€','£','$','¢','£','Q','£','$','L','$','Ft',  'kr','₹','Rp','﷼','£','₪','J$','¥','£','лв','₩','₩','₭','£','$','ден','RM','₨','$','₮',' د.إ','MT','$','₨',  'ƒ','$','C$','₦','kr','﷼','₨','B/.','Gs','S/.','₱','zł','﷼','lei','₽','£','﷼','Дин.','₨','S','₩','R','₨',  'kr','CHF','£','NT$','฿','TT$','₺','$','₴','د.إ','$U','лв','Bs','₫','﷼','Z$')
  if  not sectab:
    pass
  else:
    currsignbox.insert(0, sectab[6])
  currsignbox.place(x=265,y=240)
  
  cspl = Label(secondtab,text="Currency sign placement")
  cspl.place(x=20,y=270)
  
  def amountsignspace(event):
    amsgpl = comcursignpla.get()
    currsign = comcursign.get()
    if amsgpl == "before amount":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'8347.26')
    elif amsgpl == "after amount":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26'+currsign)
    elif amsgpl == "before amount with space":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'  8347.26')
    elif amsgpl == "after amount with space":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26  '+currsign)
    
      
      
  comcursignpla = StringVar()
  cspe = ttk.Combobox(secondtab,width=24,textvariable=comcursignpla,)
  cspe.bind("<<ComboboxSelected>>", amountsignspace)
  cspe["values"] = ("before amount","after amount",'before amount with space',"after amount with space")
  if  not sectab:
    pass
  else:
    cspe.insert(0, sectab[7])
  cspe.place(x=180,y=270)
  
  def decpl(event):
    dec = comdecsep.get()
    ex = comex.get()
    if dec == ",":
      var = str.replace(ex,".",",")
      exbox.delete(0, END)
      exbox.insert(0, var)
    elif dec == ".":
      var1 = str.replace(ex,",",".")
      exbox.delete(0, END)
      exbox.insert(0, var1)
  dsl = Label(secondtab,text="Decimal separator")
  dsl.place(x=20,y=300)
  comdecsep = StringVar()
  currbox = ttk.Combobox(secondtab,width=5,textvariable=comdecsep)
  currbox.bind("<<ComboboxSelected>>",decpl)
  currbox['values'] = ('.',',')
  if  not sectab:
    pass
  else:
    currbox.insert(0, sectab[8])
  currbox.place(x=130,y=300)
  
  exl = Label(secondtab,text="Example")
  exl.place(x=185,y=300)
  comex = StringVar()
  exbox = Entry(secondtab,width=15,textvariable=comex)
  if  not sectab:
    exbox.insert(0, 84367.26)
  else:
    exbox.insert(0, sectab[9])
  exbox.place(x=245,y=300)
  
  btred = Button(secondtab,text="Restore Default")
  btred.place(x=400,y=270)
  btsc = Button(secondtab,text="SET CURRENCY")
  btsc.place(x=400,y=300)
  
  datef=LabelFrame(secondtab,text="Date format", height=60, width=500)
  datef.place(x=5, y=355)
  
  def daffun(event):
    dafget = daf.get()
    if dafget == "mm-dd-yyyy":
      exd._set_text(exd._date.strftime('%m-%d-%Y'))
    elif dafget == "dd-mm-yyyy":
      exd._set_text(exd._date.strftime('%d-%m-%Y'))
    elif dafget == "yyy.mm.dd":
      exd._set_text(exd._date.strftime('%Y.%m.%d'))
    elif dafget == "mm/dd/yyyy":
      exd._set_text(exd._date.strftime('%m/%d/%Y'))
    elif dafget == "dd/mm/yyy":
      exd._set_text(exd._date.strftime('%d/%m/%Y'))
    elif dafget == "dd.mm.yyyy":
      exd._set_text(exd._date.strftime('%d.%m.%Y'))
    elif dafget == "yyyy/mm/dd":
      exd._set_text(exd._date.strftime('%Y/%m/%d'))
    
  
  comdaf = StringVar()
  daf = ttk.Combobox(secondtab,textvariable=comdaf)
  daf["values"] = ("Default",'mm-dd-yyyy','dd-mm-yyyy','yyy.mm.dd','mm/dd/yyyy','dd/mm/yyy','dd.mm.yyyy','yyyy/  mm/dd')
  daf.bind("<<ComboboxSelected>>",daffun)
  if not sectab:
    pass
  else:
    daf.insert(0, sectab[10])
  daf.place(x=60,y=380)
  
  
  exd = DateEntry(secondtab,)
  exd.place(x=280,y=380)
  if  not sectab:
    pass
  else:
    exd.delete(0, END)
    exd.insert(0, sectab[11])
  
  tnr=LabelFrame(secondtab,text="Tax name and rate", height=200, width=500)
  tnr.place(x=560, y=15)
  
  stt=LabelFrame(secondtab,text="Select tax type", height=120, width=180)
  stt.place(x=580, y=30)
  def rtax1():
    ch = radtax.get()
    if ch == 1:
      tax1namel.place_forget()
      tax1namee.place_forget()
      tax1ratel.place_forget()
      tax1ratee.place_forget()
      tax1ratee.place_forget()
      ptax1.place_forget()
  
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif ch == 2:
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif ch == 3:
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place(x=800, y=110)
      tax2namee.place(x=880,y=110)
      tax2ratel.place(x=800, y=140)
      tax2ratee.place(x=880,y=140)
      ptax2.place(x=580,y=185)
    
  radtax = IntVar()
  rdnotax = Radiobutton(secondtab,text="Do not use TAX",value="1",variable=radtax,command=rtax1)
  rdnotax.place(x=590,y=50)
  
  
  rdtax1 = Radiobutton(secondtab,text="1 level of Tax",value="2",variable=radtax,command=rtax1)
  rdtax1.place(x=590,y=80)
  ptax01 = IntVar()
  tax1namel = Label(secondtab,text="Tax1 name")
  
  
  tax1namee = Entry(secondtab)
  if  not sectab:
    pass
  else:
    tax1namee.insert(0, sectab[15])
  tax1namee.place(x=60,y=380)
  
  
  tax1ratel = Label(secondtab,text="Tax1 rate")
  
  
  tax1ratee = Entry(secondtab)
  if  not sectab:
    pass
  else:
    tax1ratee.insert(0, sectab[16])
  
  comptax1 = BooleanVar()
  ptax1 = Checkbutton(secondtab,text="Print TAX1" ,onvalue =1 ,offvalue = 0,variable=comptax1)
  if  not sectab:
    pass
  elif sectab[17] == 1:
    ptax1.select()
  else:
    ptax1.deselect()
  
  rdtax2 = Radiobutton(secondtab,text="2 level of Tax",value="3",variable=radtax,command=rtax1)
  rdtax2.place(x=590,y=110)
  
  
  tax2namel = Label(secondtab,text="Tax2 name")
  
  
  tax2namee = Entry(secondtab)
  if  not sectab:
    pass
  else:
    tax2namee.insert(0, sectab[18])
  
  tax2ratel = Label(secondtab,text="Tax2 rate")
  
  tax2ratee = Entry(secondtab)
  if  not sectab:
    pass
  else:
    tax2ratee.insert(0, sectab[19])
  
  comptax2 = BooleanVar()
  ptax2 = Checkbutton(secondtab,text="Print TAX2" ,onvalue =1 ,offvalue = 0,variable=comptax2)
  if  not sectab:
    pass
  else:
    if sectab[20] == 1:
      ptax2.select()
    else:
      ptax2.deselect()
  
  if  not sectab:
    pass
  else:
    if sectab[12] == "1":
      rdnotax.select()
      tax1namel.place_forget()
      tax1namee.place_forget()
      tax1ratel.place_forget()
      tax1ratee.place_forget()
      tax1ratee.place_forget()
      ptax1.place_forget()
  
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif sectab[12] == "2":
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
      rdtax1.select()
    elif sectab[12] == "3":
      rdtax2.select()
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place(x=800, y=110)
      tax2namee.place(x=880,y=110)
      tax2ratel.place(x=800, y=140)
      tax2ratee.place(x=880,y=140)
      ptax2.place(x=580,y=185)
    else:
      pass
  
  
  comlo=LabelFrame(secondtab,text="Comapny Logo", height=260, width=320)
  comlo.place(x=560, y=240)
  
  def upload_filelogo():
    global imglogo,filename
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
    image = Image.open(filename)
    resize_image = image.resize((280, 160))
    imglogo = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
  
    btlogo = Button(secondtab,width=280,height=160,image=imglogo)
    btlogo.place(x=580,y=280)
  
  try:
    image = Image.open("images/"+sectab[13])
    resize_image = image.resize((280, 160))
    image = ImageTk.PhotoImage(resize_image)
    btlogo = Button(secondtab,width=280,height=160,image=image)
    btlogo.place(x=580,y=280)
    btlogo.photo = image
  except:
    pass
  
    
  btloadim = Button(secondtab,text="Load logo image",command=upload_filelogo)
  btloadim.place(x=580,y=460)
  
  compimg = IntVar()
  primage = Checkbutton(secondtab,text="Print logo image",variable = compimg,onvalue =1 ,offvalue = 0)
  primage.place(x=740,y=460)
  
  ################### tab06 ###################################
  
  def user():
    display = displaystart.get()
    user_name = usernae.get()
    password = userpase.get()
    conformpassword = usercpase.get()
   
    create_inv = creinvbol.get()
    delete_inv = delinvbol.get()
    void_inv = voinvbol.get()
    mark_inv_as_paid = markinvbol.get()
    
    create_ord = creordbol.get()
    delete_ord = delordbol.get()
    turn_inv_ord = turninvbol.get()
    smsnofi = smsinvbol.get()
    
    create_est = creestimatebol.get()
    delete_est = delestimatebol.get()
    turn_est = turnestiinvbol.get()
  
    create_exp = creexpensebol.get()
    delete_exp = delexpensebol.get()
    rebill_exp = rebillexpebol.get()
    
    create_cus = crecusbol.get()
    delete_cus = delcusbol.get()
    imp_cus = impcusbol.get()
  
    create_pros = creprosbol.get()
    delete_pros = delprosbol.get()
    import_pros = impprosbol.get()
  
    runrep = runrepbol.get()
    gen_rec = genrecinvbol.get()
  
    create_pur = crepurbol.get()
    delete_pur = delpurbol.get()
  
    modify_inv = modifyinvbol.get()
    modify_ord = modifyordbol.get()
    modify_est = modifyestibol.get()
  
    if user_name=="" or password=="":
      messagebox.showerror('',"Please complete the form")
    else:
      sql='SELECT * FROM users WHERE username=%s'# selecting entire table from db,taking username , nd check   the existance
      val=(user_name,)
      fbcursor.execute(sql,val)
      if fbcursor.fetchone()is not None:
        sql='SELECT * FROM users WHERE username=%s'
        val=(user_name,)
        fbcursor.execute(sql,val)
        whuser = fbcursor.fetchone()
        print(whuser[0])
        if password == conformpassword:
        # messagebox.showerror('Warming','User name already exist!!')
          sqll= 'UPDATE users SET displayloginscreen=%s,username=%s,password=%s,confirm_password=%s,create_invoice=%s,delete_invoice=%s,void_invoice=%s,mark_invoice_as_paid=%s,create_order=%s,delete_order=%s,turn_order_into_invoice=%s,send_sms_nofitication=%s,create_estimate=%s,delete_estimate=%s,turn_oestimate_into_invoice=%s,create_expense=%s,delete_expense=%s,rebill_exprense=%s,create_customer=%s,delete_customer=%s,import_customer=%s,	create_product_service=%s,delete_product_service=%s,import_product_service=%s,run_reports=%s,generate_recurring_invoice=%s,create_purchase_order=%s,delete_purchase_order=%s,modify_invoice_settings=%s,modify_order_settings=%s,modify_estimate_settings=%s WHERE userID=%s'
          vall=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est,whuser[0])
          fbcursor.execute(sqll,vall)
          fbilldb.commit()
        else:
          messagebox.showerror('Warming','Password not match!!')
      else:
        if password == conformpassword:
          sql="INSERT INTO users(displayloginscreen,username,password,confirm_password,create_invoice,  delete_invoice,void_invoice,mark_invoice_as_paid,create_order,delete_order,turn_order_into_invoice,  send_sms_nofitication,create_estimate,delete_estimate,turn_oestimate_into_invoice,	create_expense,	  delete_expense,rebill_exprense,create_customer,delete_customer,import_customer,	create_product_service,  delete_product_service,	import_product_service,run_reports,generate_recurring_invoice,  create_purchase_order,delete_purchase_order,modify_invoice_settings,modify_order_settings,  modify_estimate_settings) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
          val=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est)
          fbcursor.execute(sql,val)
          fbilldb.commit()
          for record in uactree.get_children():
            uactree.delete(record)
          sql = "select * from users"
          fbcursor.execute(sql)
          sixuactree = fbcursor.fetchall()
          coutset = 0
          for i in sixuactree:
           uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
           coutset += 1
        else:
          messagebox.showerror('Warming','Password not match!!')
        

   
    
  
  
  
  
    
  
    
  sixtab1=Frame(tab06, relief=GROOVE, bg="#f8f8f2")
  sixtab1.pack(side="top", fill=BOTH)
  
  sixtab=Frame(sixtab1, bg="#f5f3f2", height=700)
  sixtab.pack(side="top", fill=BOTH)
  
  displaystart = BooleanVar()
  displaylocsc = Checkbutton(sixtab,text="Display Login screen startup",onvalue =1 ,offvalue = 0,  variable=displaystart)
  displaylocsc.place(x=20,y=30)
  
  userac=LabelFrame(sixtab,text="User Acounts", height=400, width=260)
  userac.place(x=20, y=55)
  
  
  selper = Label(sixtab,text="Select username to modify permissions")
  selper.place(x=30,y=75)
  
  def focususer(event):
    itemid = uactree.item(uactree.focus())["values"][0]
    sql = "select * from users where username = %s"
    val = (itemid,)
    fbcursor.execute(sql,val)
    sixtabdataback = fbcursor.fetchone()
    print(sixtabdataback)
    usernae.delete(0,END)
    usernae.insert(0,itemid)
    if itemid == "adminstator":
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = DISABLED
        creinv["state"] = DISABLED
        delinv["state"] = DISABLED
        voinv["state"] = DISABLED
        markinv["state"] = DISABLED
        creord["state"] = DISABLED
        delord["state"] = DISABLED
        turninv["state"] = DISABLED
        smsinv["state"] = DISABLED
        creestimate["state"] = DISABLED
        delestimate["state"] = DISABLED
        turnestiinv["state"] = DISABLED
        creexpense["state"] = DISABLED
        delexpense["state"] = DISABLED
        rebillexpe["state"] = DISABLED
        crecus["state"] = DISABLED
        delcus["state"] = DISABLED
        impcus["state"] = DISABLED
        crepros["state"] = DISABLED
        delpros["state"] = DISABLED
        imppros["state"] = DISABLED
        runrep["state"] = DISABLED
        genrecinv["state"] = DISABLED
        crepur["state"] = DISABLED
        delpur["state"] = DISABLED
        modifyinv["state"] = DISABLED
        modifyord["state"] = DISABLED
        modifyesti["state"] = DISABLED
    else:
        userpase.delete(0, END)
        usercpase.delete(0, END)
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = NORMAL
        creinv["state"] = NORMAL
        delinv["state"] = NORMAL
        voinv["state"] = NORMAL
        markinv["state"] = NORMAL
        creord["state"] = NORMAL
        delord["state"] = NORMAL
        turninv["state"] = NORMAL
        smsinv["state"] = NORMAL
        creestimate["state"] = NORMAL
        delestimate["state"] = NORMAL
        turnestiinv["state"] = NORMAL
        creexpense["state"] = NORMAL
        delexpense["state"] = NORMAL
        rebillexpe["state"] = NORMAL
        crecus["state"] = NORMAL
        delcus["state"] = NORMAL
        impcus["state"] = NORMAL
        crepros["state"] = NORMAL
        delpros["state"] = NORMAL
        imppros["state"] = NORMAL
        runrep["state"] = NORMAL
        genrecinv["state"] = NORMAL
        crepur["state"] = NORMAL
        delpur["state"] = NORMAL
        modifyinv["state"] = NORMAL
        modifyord["state"] = NORMAL
        modifyesti["state"] = NORMAL
    if not sixtabdataback:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      creinv.deselect()
      delinv.deselect()
      voinv.deselect()
      markinv.deselect()
      creord.deselect()
      delord.deselect()
      turninv.deselect()
      smsinv.deselect()
      creestimate.deselect()
      delestimate.deselect()
      turnestiinv.deselect()
      creexpense.deselect()
      delexpense.deselect()
      rebillexpe.deselect()
      crecus.deselect()
      delcus.deselect()
      impcus.deselect()
      crepros.deselect()
      delpros.deselect()
      imppros.deselect()
      runrep.deselect()
      genrecinv.deselect()
      crepur.deselect()
      delpur.deselect()
      modifyinv.deselect()
      modifyord.deselect()
      modifyesti.deselect()
      if itemid == "adminstator":
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = DISABLED
        creinv["state"] = DISABLED
        delinv["state"] = DISABLED
        voinv["state"] = DISABLED
        markinv["state"] = DISABLED
        creord["state"] = DISABLED
        delord["state"] = DISABLED
        turninv["state"] = DISABLED
        smsinv["state"] = DISABLED
        creestimate["state"] = DISABLED
        delestimate["state"] = DISABLED
        turnestiinv["state"] = DISABLED
        creexpense["state"] = DISABLED
        delexpense["state"] = DISABLED
        rebillexpe["state"] = DISABLED
        crecus["state"] = DISABLED
        delcus["state"] = DISABLED
        impcus["state"] = DISABLED
        crepros["state"] = DISABLED
        delpros["state"] = DISABLED
        imppros["state"] = DISABLED
        runrep["state"] = DISABLED
        genrecinv["state"] = DISABLED
        crepur["state"] = DISABLED
        delpur["state"] = DISABLED
        modifyinv["state"] = DISABLED
        modifyord["state"] = DISABLED
        modifyesti["state"] = DISABLED
      else:
        userpase.delete(0, END)
        usercpase.delete(0, END)
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = NORMAL
        creinv["state"] = NORMAL
        delinv["state"] = NORMAL
        voinv["state"] = NORMAL
        markinv["state"] = NORMAL
        creord["state"] = NORMAL
        delord["state"] = NORMAL
        turninv["state"] = NORMAL
        smsinv["state"] = NORMAL
        creestimate["state"] = NORMAL
        delestimate["state"] = NORMAL
        turnestiinv["state"] = NORMAL
        creexpense["state"] = NORMAL
        delexpense["state"] = NORMAL
        rebillexpe["state"] = NORMAL
        crecus["state"] = NORMAL
        delcus["state"] = NORMAL
        impcus["state"] = NORMAL
        crepros["state"] = NORMAL
        delpros["state"] = NORMAL
        imppros["state"] = NORMAL
        runrep["state"] = NORMAL
        genrecinv["state"] = NORMAL
        crepur["state"] = NORMAL
        delpur["state"] = NORMAL
        modifyinv["state"] = NORMAL
        modifyord["state"] = NORMAL
        modifyesti["state"] = NORMAL
    else:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      userpase.insert(0, sixtabdataback[4])
      usercpase.insert(0, sixtabdataback[5])
      if sixtabdataback[6] == 1:
        creinv.select()
      else:
        creinv.deselect()
      if sixtabdataback[7] == 1:
        delinv.select()
      else:
        delinv.deselect()
      if sixtabdataback[8] == 1:
        voinv.select()
      else:
        voinv.deselect()
      if sixtabdataback[9] == 1:
        markinv.select()
      else:
        markinv.deselect()
      if sixtabdataback[10] == 1:
        creord.select()
      else:
        creord.deselect()
      if sixtabdataback[11] == 1:
        delord.select()
      else:
        delord.deselect()
      if sixtabdataback[12] == 1:
        turninv.select()
      else:
        turninv.deselect()
      if sixtabdataback[13] == 1:
        smsinv.select()
      else:
        smsinv.deselect()
      if sixtabdataback[14] == 1:
        creestimate.select()
      else:
        creestimate.deselect()
      if sixtabdataback[15] == 1:
        delestimate.select()
      else:
        delestimate.deselect()
      if sixtabdataback[16] == 1:
        turnestiinv.select()
      else:
        turnestiinv.deselect()
      if sixtabdataback[17] == 1:
        creexpense.select()
      else:
        creexpense.deselect()
      if sixtabdataback[18] == 1:
        delexpense.select()
      else:
        delexpense.deselect()
      if sixtabdataback[19] == 1:
        rebillexpe.select()
      else:
        rebillexpe.deselect()
      if sixtabdataback[20] == 1:
        crecus.select()
      else:
        crecus.deselect()
      if sixtabdataback[21] == 1:
        delcus.select()
      else:
        delcus.deselect()
      if sixtabdataback[22] == 1:
        impcus.select()
      else:
        impcus.deselect()
      if sixtabdataback[23] == 1:
        crepros.select()
      else:
        crepros.deselect()
      if sixtabdataback[24] == 1:
        delpros.select()
      else:
        delpros.deselect()
      if sixtabdataback[25] == 1:
        imppros.select()
      else:
        imppros.deselect()
      if sixtabdataback[26] == 1:
        runrep.select()
      else:
        runrep.deselect()
      if sixtabdataback[27] == 1:
        genrecinv.select()
      else:
        genrecinv.deselect()
      if sixtabdataback[28] == 1:
        crepur.select()
      else:
        crepur.deselect()
      if sixtabdataback[29] == 1:
        delpur.select()
      else:
        delpur.deselect()
      if sixtabdataback[30] == 1:
        modifyinv.select()
      else:
        modifyinv.deselect()
      if sixtabdataback[31] == 1:
        modifyord.select()
      else:
        modifyord.deselect()
      if sixtabdataback[32] == 1:
        modifyesti.select()
      else:
        modifyesti.deselect()
         
  
  scrollbarx = Scrollbar(sixtab, orient=HORIZONTAL)
  scrollbary = Scrollbar(sixtab, orient=VERTICAL)
  uactree = ttk.Treeview(sixtab, columns=("1"),height=400,selectmode="extended", yscrollcommand=scrollbary.  set, xscrollcommand=scrollbarx.set)
  scrollbary.config(command=uactree.yview)
  scrollbary.place(x=245,y=100,height=300)
  uactree.heading('1', text="Username",)
  uactree.column('#0', stretch=NO, minwidth=0, width=0)
  uactree.column('1', stretch=NO, minwidth=0, width=218)
  uactree.place(x=30,y=100,height=300,width=220)
  uactree.bind('<Double-Button-1>' , focususer)
  sql = "select * from users"
  fbcursor.execute(sql)
  sixuactree = fbcursor.fetchall()
  coutset = 0
  if not sixuactree:
    uactree.insert('', index='end', text='hello', values=("adminstator"))
  else:
    for i in sixuactree:
      uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
      coutset += 1
  
  def adduser():
    uactree.insert('', index='end', text='hello', values=("Rename User"))
  
  btadd = Button(sixtab,text="Add new User",command=adduser)
  btadd.place(x=30,y=415)
  
  def users():
    itemid = uactree.item(uactree.focus())["values"][0]
    if itemid == "adminstator":
      messagebox.showerror('F-Billing Revolution', 'Cannot delete adminstator user.')
    else:
      delusermess = messagebox.askyesno("Delete user", "Are you sure to delete this user?")
      if delusermess == True:
        sql = "delete from users where username = %s"
        val = (itemid, )
        fbcursor.execute(sql, val)
        fbilldb.commit()
        for record in uactree.get_children():
          uactree.delete(record)
        sql = "select * from users"
        fbcursor.execute(sql)
        sixuactree = fbcursor.fetchall()
        coutset = 0
        for i in sixuactree:
          uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
          coutset += 1
      else:
        pass
        
  
  btdus = Button(sixtab,text="Delete User",command=users)
  btdus.place(x=180,y=415)
  
  userpro=LabelFrame(sixtab,text="User Profile", height=400, width=750)
  userpro.place(x=300, y=55)
  
  
  userna = Label(sixtab,text="Username")
  userna.place(x=340,y=90)
  usernae = Entry(sixtab,)
  usernae.place(x=460,y=90)
  
  userpas = Label(sixtab,text="Password")
  userpas.place(x=340,y=120)
  userpase = Entry(sixtab,)
  userpase.place(x=460,y=120)
  
  usercpas = Label(sixtab,text="Confirm Password")
  usercpas.place(x=340,y=150)
  usercpase = Entry(sixtab,)
  usercpase.place(x=460,y=150)
  
  saveuserprofile = Button(sixtab,text="save user profile",command=user)
  saveuserprofile.place(x=650,y=120)
  
  creinvbol = BooleanVar()
  creinv = Checkbutton(sixtab,text="Create invoice",onvalue= 1 ,offvalue= 0,variable=creinvbol)
  creinv.place(x=340,y=200)
  delinvbol = BooleanVar()
  delinv = Checkbutton(sixtab,text="Delete invoice",onvalue= 1 ,offvalue= 0,variable=delinvbol)
  delinv.place(x=340,y=225)
  voinvbol = BooleanVar()
  voinv = Checkbutton(sixtab,text="Void invoice",onvalue= 1 ,offvalue= 0,variable=voinvbol)
  voinv.place(x=340,y=250)
  markinvbol = BooleanVar()
  markinv = Checkbutton(sixtab,text="Mark invoice as Paid",onvalue= 1 ,offvalue= 0,variable=markinvbol)
  markinv.place(x=340,y=275)
  
  creordbol = BooleanVar()
  creord = Checkbutton(sixtab,text="Create Order",onvalue= 1 ,offvalue= 0,variable=creordbol)
  creord.place(x=500,y=200)
  delordbol = BooleanVar()
  delord = Checkbutton(sixtab,text="Delete Order",onvalue= 1 ,offvalue= 0,variable=delordbol)
  delord.place(x=500,y=225)
  turninvbol = BooleanVar()
  turninv = Checkbutton(sixtab,text="Turn order into invoice",onvalue= 1 ,offvalue= 0,variable=turninvbol)
  turninv.place(x=500,y=250)
  smsinvbol = BooleanVar()
  smsinv = Checkbutton(sixtab,text="Send sms nofitication",onvalue= 1 ,offvalue= 0,variable=smsinvbol)
  smsinv.place(x=500,y=275)
  
  creestimatebol = BooleanVar()
  creestimate = Checkbutton(sixtab,text="Create estimate",onvalue= 1 ,offvalue= 0,variable=creestimatebol)
  creestimate.place(x=680,y=200)
  delestimatebol = BooleanVar()
  delestimate = Checkbutton(sixtab,text="Delete estimate",onvalue= 1 ,offvalue= 0,variable=delestimatebol)
  delestimate.place(x=680,y=225)
  turnestiinvbol = BooleanVar()
  turnestiinv = Checkbutton(sixtab,text="Turn estimates into invoice",onvalue= 1 ,offvalue= 0,  variable=turnestiinvbol)
  turnestiinv.place(x=680,y=250)
  
  creexpensebol = BooleanVar()
  creexpense = Checkbutton(sixtab,text="Create expenses",onvalue= 1 ,offvalue= 0,variable=creexpensebol)
  creexpense.place(x=880,y=200)
  delexpensebol = BooleanVar()
  delexpense = Checkbutton(sixtab,text="Delete expenses",onvalue= 1 ,offvalue= 0,variable=delexpensebol)
  delexpense.place(x=880,y=225)
  rebillexpebol = BooleanVar()
  rebillexpe = Checkbutton(sixtab,text="Rebill expenses",onvalue= 1 ,offvalue= 0,variable=rebillexpebol)
  rebillexpe.place(x=880,y=250)
  
  crecusbol = BooleanVar()
  crecus = Checkbutton(sixtab,text="Create customer",onvalue= 1 ,offvalue= 0,variable=crecusbol)
  crecus.place(x=340,y=320)
  delcusbol = BooleanVar()
  delcus = Checkbutton(sixtab,text="Delete customer",onvalue= 1 ,offvalue= 0,variable=delcusbol)
  delcus.place(x=340,y=340)
  impcusbol = BooleanVar()
  impcus = Checkbutton(sixtab,text="Import customer",onvalue= 1 ,offvalue= 0,variable=impcusbol)
  impcus.place(x=340,y=360)
  
  creprosbol = BooleanVar()
  crepros = Checkbutton(sixtab,text="Create product\services",onvalue= 1 ,offvalue= 0,variable=creprosbol)
  crepros.place(x=500,y=320)
  delprosbol = BooleanVar()
  delpros = Checkbutton(sixtab,text="Delete product\services",onvalue= 1 ,offvalue= 0,variable=delprosbol)
  delpros.place(x=500,y=340)
  impprosbol = BooleanVar()
  imppros = Checkbutton(sixtab,text="Import product\services",onvalue= 1 ,offvalue= 0,variable=impprosbol)
  imppros.place(x=500,y=360)
  
  runrepbol = BooleanVar()
  runrep = Checkbutton(sixtab,text="Run reports",onvalue= 1 ,offvalue= 0,variable=runrepbol)
  runrep.place(x=680,y=320)
  genrecinvbol = BooleanVar()
  genrecinv = Checkbutton(sixtab,text="Generate recurring invoices",onvalue= 1 ,offvalue= 0,  variable=genrecinvbol)
  genrecinv.place(x=680,y=340)
  
  crepurbol = BooleanVar()
  crepur = Checkbutton(sixtab,text="Create Purchase order",onvalue =1 ,offvalue = 0,variable=crepurbol)
  crepur.place(x=880,y=320)
  delpurbol = BooleanVar()
  delpur = Checkbutton(sixtab,text="Delete Purchase order",onvalue =1 ,offvalue = 0,variable=delpurbol)
  delpur.place(x=880,y=340)
  
  undersetlab = Label(sixtab,text="Under Settings menu tab")
  undersetlab.place(x=340,y=400)
  
  modifyinvbol = BooleanVar()
  modifyinv = Checkbutton(sixtab,text="Modify invoice settings",onvalue =1 ,offvalue = 0,variable=modifyinvbol)
  modifyinv.place(x=340,y=425)
  
  modifyordbol = BooleanVar()
  modifyord = Checkbutton(sixtab,text="Modify order settings",onvalue =1 ,offvalue = 0,variable=modifyordbol)
  modifyord.place(x=500,y=425)
  
  modifyestibol = BooleanVar()
  modifyesti = Checkbutton(sixtab,text="Modify estimate settings",onvalue =1 ,offvalue = 0,  variable=modifyestibol)
  modifyesti.place(x=680,y=425)
root.mainloop()

