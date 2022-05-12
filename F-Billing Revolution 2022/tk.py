from datetime import date, datetime
from tkinter import *
from matplotlib.pyplot import text

from tkcalendar import DateEntry

root = Tk()
root.geometry("750x450")

import datetime
import calendar

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)
    
def tak(event):
   d1=expdt3.get_date()
   d2=date.today()
   d3=d1-d2
   print(d3)

   expdt2=DateEntry(root, textvariable=d3)
   print(type(expdt2))
   expdt2.pack()
    




expdt3=DateEntry(root)
# print(type(expdt3))
expdt3.bind("<<DateEntrySelected>>",tak)
expdt3.pack()

root.mainloop()
