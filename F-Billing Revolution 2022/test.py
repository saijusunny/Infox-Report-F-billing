#Import the required Libraries
import PyPDF2
from tkinter import *
from tkinter import filedialog
#Create an instance of tkinter frame
win= Tk()
#Set the Geometry
win.geometry("750x450")
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


def my_popup(event):
    my_menu.tk_popup(event.x_root, event.y_root)


my_menu= Menu(canvas, tearoff=False)
my_menu.add_command(label="Run Report", command="run")
my_menu.add_separator()
my_menu.add_command(label="Print Report", command="pr")
my_menu.add_command(label="Email Report", command="em")

my_menu.add_separator()
my_menu.add_command(label="Export Report To Excel", command="excel")
my_menu.add_command(label="Export Report To PDF", command="pdf")


canvas.bind("<Button-3>", my_popup)


# #Create a Text Box
# text= Text(win,width= 80,height=100)
# text.pack(pady=20)
# #Define a function to clear the text
# def clear_text():
#    text.delete(1.0, END)
# #Define a function to open the pdf file
# def open_pdf():
#    file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
#    if file:
#       #Open the PDF File
#       pdf_file= PyPDF2.PdfFileReader(file)
#       #Select a Page to read
#       page= pdf_file.getPage(0)
#       #Get the content of the Page
#       content=page.extractText()
#       #Add the content to TextBox
#       text.insert(1.0,content)

# #Define function to Quit the window
# def quit_app():
#    win.destroy()
# #Create a Menu
# my_menu= Menu(win)
# win.config(menu=my_menu)
# #Add dropdown to the Menus
# file_menu=Menu(my_menu,tearoff=False)
# my_menu.add_cascade(label="File",menu= file_menu)
# file_menu.add_command(label="Open",command=open_pdf)
# file_menu.add_command(label="Clear",command=clear_text)
# file_menu.add_command(label="Quit",command=quit_app)
win.mainloop()
