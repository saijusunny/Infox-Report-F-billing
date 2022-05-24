# #Import the required Libraries
# from tkinter import font
# import PyPDF2
# from tkinter import *
# from tkinter import filedialog
# from tkinter import ttk
# #Create an instance of tkinter frame
# win= Tk()
# #Set the Geometry
# # win.geometry("750x450")


# import os
# import subprocess
# import tkinter as tk

# class App(object):
#     def __init__(self, root):
#         self.line_start = None
#         self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
#         self.canvas.bind("<Button-1>", lambda e: self.draw(e.x, e.y))
#         self.button = tk.Button(root, text="Generate PDF", command=self.generate_pdf)
#         self.canvas.pack()
#         self.button.pack(pady=10)

#     def draw(self, x, y):
#         if self.line_start:
#             x_origin, y_origin = self.line_start
#             self.canvas.create_line(x_origin, y_origin, x, y)
#             self.line_start = None
#         else:
#             self.line_start = (x, y)

#     def generate_pdf(self):
#         self.canvas.postscript(file="tmp.ps", colormode="color")
#         process = subprocess.Popen(["ps2pdf", "tmp.ps", "result.pdf"], shell=True)
#         process.wait()
#         os.remove("tmp.ps")

# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title("Canvas2PDF")
#     app = App(root)
#     root.mainloop()


frame = Frame(
    win,
    width=953,
    height=1000,
    )
frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
frame.place(x=247,y=90)





canvas=Canvas(
    frame,
    bg='grey',
    width=953,
    height=1000,
    scrollregion=(0,0,1500, 1500)
    )

vertibar=Scrollbar(
    frame,
    orient=VERTICAL
    )
vertibar.pack(side=RIGHT,fill=Y)
vertibar.config(command=canvas.yview)
canvas.config(width=953,height=1000)

canvas.config(
    yscrollcommand=vertibar.set
    )
canvas.pack(expand=True,side=LEFT,fill=BOTH)
canvas.create_rectangle(25,25,935,1120,  outline='yellow',fill='white')
# # canvas.create_text(345,165,text="Address line1\nAddress line2\nAddress line3\nAddress line3\nAddress line4\nPhone 555-5555",fill='black',font=("Helvetica", 10), justify='left')

# # canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        
# # canvas.create_text(900,100,text="menu1.get()",fill='black',font=("Helvetica", 16), justify='right')
# # canvas.create_text(855,145,text="Date From:01-04-2022      Date From:01-04-2022\n Invoice Category: All",fill='black',font=("Helvetica", 8), justify='right')

# # canvas.create_text(345,228,text="Sales tax reg No.",fill='black',font=("Helvetica", 8), justify='left')
        


# #         # Add a Treeview widget


# # tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5", "c6", "c7", "c8"), show='headings', height=8, style='mystyle.Treeview')
# # style=ttk.Style()
# # style.configure('mystyle.Treeview', font('Arial Bold', 10))
# # tree.column("# 1", anchor=E, stretch=NO, width=100)
# # tree.heading("# 1", text="No")
# # tree.column("# 2", anchor=E, stretch=NO, width=100)
# # tree.heading("# 2", text="Date")
# # tree.column("# 3", anchor=E, stretch=NO, width=100)
# # tree.heading("# 3", text="Due Date")
# # tree.column("# 4", anchor=E, stretch=NO, width=100)
# # tree.heading("# 4", text="Terms")
# # tree.column("# 5", anchor=E, stretch=NO, width=100)
# # tree.heading("# 5", text="Status")
# # tree.column("# 6", anchor=E, stretch=NO, width=100)
# # tree.heading("# 6", text="Invoice Total")
# # tree.column("# 7", anchor=E, stretch=NO, width=100)
# # tree.heading("# 7", text="Invoice Paid")
# # tree.column("# 8", anchor=E, stretch=NO, width=100)
# # tree.heading("# 8", text="Balance")
# # # Insert the data in Treeview widget
# # tree.insert('', 'end',text="1",values=('','','','','','Invoice Total','Total Paid','Balance'))

# # window = canvas.create_window(85, 290, anchor="nw", window=tree)

# # win.mainloop()



from reportlab.pdfgen import canvas


c=canvas.Canvas("invoiuce.pdf")
c.drawString(200, 700, "hello World")
c.save()
print("Pdf generate")