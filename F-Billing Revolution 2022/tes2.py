# # Import the required libraries
# from tkinter import *
# from tkHyperLinkManager import HyperlinkManager
# import webbrowser
# from functools import partial

# # Create an instance of tkinter frame
# win = Tk()
# win.geometry("700x350")

# # Define a callback function
# def callback(url):
#    webbrowser.open_new_tab(url)

# # Create a Label to display the link
# text = Text(win)
# text.insert(END,"Hey Folks, Welcome to ")
# text.pack()
# hyperlink= HyperlinkManager(text)

# text.insert(END,
# "TutorialsPoint",hyperlink.add(partial(webbrowser.open,"http://www.tutorialspoint.com")))

# # win.mainloop()
# import hyperlink

# url = hyperlink.parse(u'http://github.com/python-hyper/hyperlink?utm_source=readthedocs')

# better_url = url.replace(scheme=u'https', port=443)
# org_url = better_url.click(u'.')

# print(org_url.to_text())
# # prints: https://github.com/python-hyper/

# print(better_url.get(u'utm_source')[0])
# # prints: readthedocs


# #Import the required libraries
# from tkinter import *
# import webbrowser

# #Create an instance of tkinter frame
# win = Tk()
# win.geometry("750x250")

# #Define a callback function
# def callback(url):
#    webbrowser.open_new_tab(url)

# #Create a Label to display the link
# link = Label(win, text="www.tutorialspoint.com",font=('Helveticabold', 15), fg="blue", cursor="hand2")
# link.pack()
# link.bind("<Button-1>", lambda e:
# callback("http://www.tutorialspoint.com"))

# win.mainloop()

import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
 
c = canvas.Canvas("hello.pdf")
 
# move the origin up and to the left
c.translate(inch,inch)
 
textobject = c.beginText(0, 10)
textobject.setFont("Helvetica-Oblique", 14)
lines = ["ghsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsds,dsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd"]
for line in lines:
    textobject.textLine(line)
 
c.drawText(textobject)
 
c.showPage()
c.save()
 
os.system('hello.pdf')