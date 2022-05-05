from tkinter import*

from django.forms import IntegerField
Win = Tk()
Win.geometry('400x400')
Win['background']='#000000'
Win.title('Calculator')

def one():
    C= 1
    print(C)
    val.set(C)

def two():
    C= 2
    print(C)
    val.set(C)

def three():
    C= 3
    print(C)
    val.set(C)

def four():
    C= 4
    print(C)
    val.set(C)

def five():
    C= 5
    print(C)
    val.set(C)

def six():
    C= 6
    print(C)
    val.set(C)

def seven():
    C= 7
    print(C)
    val.set(C)

def eight():
    C= 8
    print(C)
    val.set(C)

def nine():
    C= 9
    print(C)
    val.set(C)

def zero():
    C= 0
    print(C)
    val.set(C)

val = StringVar()
clr = StringVar()

entry=Entry(Win, textvariable=val, width=50, fg='white', bg='blue').place(y=30,x=50)
btn1=Button(Win, text='1', width=9, fg='white', bg='red', command=one).place(y=70,x=52)
btn1=Button(Win, text='2', width=9, fg='white', bg='red', command=two).place(y=70,x=127)
btn1=Button(Win, text='3', width=9, fg='white', bg='red', command=three).place(y=70,x=202)
btn1=Button(Win, text='+',width=9, fg='white', bg='blue', command=one).place(y=70,x=277)


btn1=Button(Win, text='4', width=9, fg='white', bg='red', command=four).place(y=100,x=52)
btn1=Button(Win, text='5', width=9, fg='white', bg='red', command=five).place(y=100,x=127)
btn1=Button(Win, text='6', width=9, fg='white', bg='red', command=six).place(y=100,x=202)
btn1=Button(Win, text='-', width=9, fg='white', bg='blue', command=one).place(y=100,x=277)

btn1=Button(Win, text='7', width=9, fg='white', bg='red', command=seven).place(y=130,x=52)
btn1=Button(Win, text='8', width=9, fg='white', bg='red', command=eight).place(y=130,x=127)
btn1=Button(Win, text='9', width=9, fg='white', bg='red', command=nine).place(y=130,x=202)
btn1=Button(Win, text='*', width=9, fg='white', bg='blue', command=one).place(y=130,x=277)

btn1=Button(Win, text='0', width=9, fg='white', bg='red', command=zero).place(y=160,x=52)
btn1=Button(Win, text='.', width=9, fg='white', bg='blue', command=one).place(y=160,x=127)
btn1=Button(Win, text='=', width=9, fg='white', bg='blue', command=one).place(y=160,x=202)
btn1=Button(Win, text='/', width=9, fg='white', bg='blue', command=one).place(y=160,x=277)

btn3=Button(Win, text='Clear', width=9, fg='black', bg='white', command=one).place(y=190,x=160)



Win.mainloop()
