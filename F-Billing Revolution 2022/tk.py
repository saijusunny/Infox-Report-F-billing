# Import Required Library
from tkinter import *
import win32api
from tkinter import filedialog
from pyautogui import alert
import os
# Create Tkinter Object
root = Tk()
  
# Set Title and geometry
root.title('Print Hard Copies')
root.geometry("200x200")
  
# Print File Function
def print_file():
    from reportlab.pdfgen import canvas
    # from tkdocviewer import *
    from reportlab.lib import colors
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase import pdfmetrics
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
    from reportlab.lib.pagesizes import letter, inch


    documentTitle = 'Document title!'
    title = 'Invoices List'
    pdf = canvas.Canvas("mmnn.pdf", pagesize=letter)
    pdf.setTitle(documentTitle)

    
    
    pdf.setFont('Helvetica',12)
    pdf.drawString(30,760, "dssds")
    pdf.drawString(30,740, "kjksdfjnhk")
    pdf.drawString(30,700, "Sales tax reg No:")
    pdf.drawString(445,760, "Recurring Invoice Report")
    "Invoice No","Customer","Next Invoice","Recurring Interval","Stop After","Invoice Total"
    pdf.drawString(460,720,"Invoice Category: All")
    pdf.drawString(28,695,"__________________________________________________________________________________")
    pdf.drawString(28,675,"__________________________________________________________________________________")
    
    pdf.drawString(28,678,"Invoice No          Customer                   Next Invoice    Recurring Interval     Stop After       Invoice Total    ")
    x=705
   
    
    pdf.drawString(28,x,"str(i[1])")
                
    pdf.drawString(115,x,"str(i[18])")
    pdf.drawString(250,x,"str(i[26])")
    pdf.drawString(335,x,"str(i[24])")
    pdf.drawString(430,x,"str(i[27])") 
    pdf.drawString(505,x,"str(i[8])")
    pdf.save()
    win32api.ShellExecute(0,"print","mmnn.pdf",None,".",0)        
    print("successful1")                
    alert(text="Print Successful",title="Success",button='ok',root=root)
# Make Button
Button(root, text="Print FIle", command=print_file).pack()
  
# Execute Tkinter
root.mainloop()