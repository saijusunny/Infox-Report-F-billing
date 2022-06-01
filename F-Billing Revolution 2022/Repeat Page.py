# # Import Required Library
# from tkinter import *
# import win32api
# import win32print
# from tkinter import filedialog
# from pyautogui import alert
# import os
# # Create Tkinter Object
# root = Tk()
  
# # Set Title and geometry
# root.title('Print Hard Copies')
# root.geometry("200x200")
  
# # Print File Function
# def print_file():
#     from reportlab.pdfgen import canvas
#     # from tkdocviewer import *
#     from reportlab.lib import colors
#     from reportlab.pdfbase.ttfonts import TTFont
#     from reportlab.pdfbase import pdfmetrics
#     from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
#     from reportlab.lib.pagesizes import letter, inch


#     documentTitle = 'Document title!'
#     title = 'Invoices List'
#     pdf = canvas.Canvas("mmnn.pdf", pagesize=letter)
#     pdf.setTitle(documentTitle)

    
    
#     pdf.setFont('Helvetica',12)
#     pdf.drawString(30,760, "dsssssssssssssssssssssssssssssssssds")
#     pdf.drawString(30,740, "kjksdfjnhk")
#     pdf.drawString(30,700, "Sales tax reg No:")
#     pdf.drawString(445,760, "Recurring Invoice Report")
#     "Invoice No","Customer","Next Invoice","Recurring Interval","Stop After","Invoice Total"
#     pdf.drawString(460,720,"Invoice Category: All")
#     pdf.drawString(28,695,"__________________________________________________________________________________")
#     pdf.drawString(28,675,"__________________________________________________________________________________")
    
#     pdf.drawString(28,47,"Invoice No          Customer                   Next Invoice    Recurring Interval     Stop After       Invoice Total    ")
#     x=705
   
    
#     pdf.drawString(28,x,"str(i[1])")
                
#     pdf.drawString(115,x,"str(i[18])")
#     pdf.drawString(250,x,"str(i[26])")
#     pdf.drawString(335,x,"str(i[24])")
#     pdf.drawString(430,x,"str(i[27])") 
#     pdf.drawString(505,x,"str(i[8])")
#     pdf.save()        
#     # print("successful1")                
#     # alert(text="Print Successful",title="Success",button='ok',root=root)
# # Make Button
# Button(root, text="Print FIle", command=print_file).pack()
  
# # Execute Tkinter
# root.mainloop()

# # path = filedialog.asksaveasfilename(initialdir=os.getcwd,title="Save File",filetypes=[('Pdf File', '*.pdf',)],
# #     defaultextension=".pdf")

# #     fileName = path
# #     documentTitle = 'Document title!'
# #     title = 'Invoices List'
# #     pdf = canvas.Canvas(fileName, pagesize=letter)
# #     width, height=letter
# #     pdf.setTitle(documentTitle) 

# #     sql_company = "SELECT * from company"
# #     fbcursor.execute(sql_company)
# #     company= fbcursor.fetchone()
    
# #     pdf.setFont('Helvetica',12)
            
# #     pdf.drawString(30,760, company[1])
# #     pdf.drawString(495,760, "Customer List")
            

# #     pdf.drawString(28,750,"__________________________________________________________________________________")
# #     pdf.drawString(28,730,"__________________________________________________________________________________")

            
            
# #     pdf.drawString(28,733,"Billing Information:                                                    Shipping Information:                      ")
# #     rth=cldfilter.get()
            
# #     x=705
# #     if rth=="All Customers ":
                
# #                 count=0
                
# #                 trf='select * from customer '
                    
                            
# #                 fbcursor.execute(trf)
# #                 thg=fbcursor.fetchall()
               
               
                               
# #                 for i in thg:
# #                                     if x==-30:
# #                                         pdf.showPage()
# #                                         x=860
# #                                         pdf.drawString(28,x-100,"__________________________________________________________________________________")
# #                                     else:
                                        
# #                                         pdf.drawString(28,x-10,'Name: '+str(i[4]))
                                    
# #                                         pdf.drawString(300,x-10,'Name:'+str(i[6]))
# #                                         pdf.drawString(28,x-25,"Customer Id:"+str(i[0]))
# #                                         pdf.drawString(300,x-25,"Tax exempt No.:"+str(i[17]))
# #                                         pdf.drawString(28,x-40,'Address: '+str(i[5]))
# #                                         pdf.drawString(300,x-40,'Address:'+str(i[7]))
# #                                         pdf.drawString(28,x-55,'Contact Person: '+str(i[8])) 
# #                                         pdf.drawString(300,x-55,'Contact Person:'+str(i[13]))
# #                                         pdf.drawString(28,x-70,'Tel:'+str(i[10]))
# #                                         pdf.drawString(300,x-70,'Tel:'+str(i[15]))
# #                                         pdf.drawString(150,x-70,'Fax: '+str(i[11])) 
# #                                         pdf.drawString(430,x-70,'Fax: '+str(i[16]))
# #                                         pdf.drawString(28,x-85,'Email: '+str(i[9]))
# #                                         pdf.drawString(300,x-85,'Email: '+str(i[14]))
# #                                         pdf.drawString(28,x-100,"__________________________________________________________________________________")
                                    
                            
# #                                     x-=105
# #                                     count += 1
  
# #                 pdf.save()
    
# #     else:
# #         pass

# #----------------------



for i in range(50):
    if i==40 or i==42:
        print("haii")
    else:
        print(i)

# def  cn_pr(canvas):
#     print(str(canvas))
#     filename=tempfile.mktemp(".txt")
#     open(filename,'w').write(str(canvas))
#     os.startfile(filename,"print")

# def show(event):
#     os.startfile(file, "print")
    # ltx=txt.itemcget(id_inv, 'text')
    # temp_file=tempfile.mktemp('.xlsx')
    # open(temp_file, 'w').write(ltx)
    # os.startfile(temp_file,'print')
    # pass
# def print_inr():
    
#     from reportlab.pdfgen import canvas
#     # from tkdocviewer import *
#     from reportlab.lib import colors
#     from reportlab.pdfbase.ttfonts import TTFont
#     from reportlab.pdfbase import pdfmetrics
#     from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
#     from reportlab.lib.pagesizes import letter, inch

#     # path = filedialog.asksaveasfilename(initialdir=os.getcwd,title="Save File",filetypes=[('Pdf File', '*.pdf',)],
#     # defaultextension=".pdf")
     
#     # fileName = path
#     documentTitle = 'Document title!'
#     title = 'Invoices List'
#     pdf = canvas.Canvas("Reports.pdf", pagesize=letter)
#     pdf.setTitle(documentTitle)

#     sql_company = "SELECT * from company"
#     fbcursor.execute(sql_company)
#     company= fbcursor.fetchone()
    
#     pdf.setFont('Helvetica',12)
#     pdf.drawString(30,760, company[1])
#     pdf.drawString(30,740, company[2])
#     pdf.drawString(30,700, "Sales tax reg No:"+company[4])
#     pdf.drawString(445,760, "Recurring Invoice Report")
#     "Invoice No","Customer","Next Invoice","Recurring Interval","Stop After","Invoice Total"
#     pdf.drawString(460,720,"Invoice Category: All")
#     pdf.drawString(28,695,"__________________________________________________________________________________")
#     pdf.drawString(28,675,"__________________________________________________________________________________")
    
#     pdf.drawString(28,678,"Invoice No          Customer                   Next Invoice    Recurring Interval     Stop After       Invoice Total    ")
    
#     count=0
#     sql_inv_dt='SELECT * FROM invoice'
 
#     fbcursor.execute(sql_inv_dt)
#     tre=fbcursor.fetchall()
#     x=655
#     for i in tre:
#                 pdf.drawString(28,x,str(i[1]))
                
#                 pdf.drawString(115,x,str(i[18]))
#                 pdf.drawString(250,x,str(i[26]))
#                 pdf.drawString(335,x,str(i[24]))
#                 pdf.drawString(430,x,str(i[27])) 
#                 pdf.drawString(505,x,str(i[8]))
               
#                 count += 1
#                 x-=15
 
#     pdf.save()
#     p = win32print.OpenPrinter (printer_name)
#     job = win32print.StartDocPrinter (p, 1, ("test of raw data", None, "RAW")) 
#     win32print.StartPagePrinter (p) 
#     win32print.WritePrinter (p, "Reports.pdf") 
#     win32print.EndPagePrinter (p)  

#     print("successful1")                
#     alert(text="Print Successful",title="Success",button='ok')
    