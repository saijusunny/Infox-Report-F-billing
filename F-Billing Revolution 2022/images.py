
import tkinter as tk
from textwrap import wrap

root = tk.Tk()

canvas_width = 600
canvas_height = 400
w = canvas_width // 2
h = canvas_height // 2
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

r1 = canvas.create_rectangle(w, h, w + 40, h + 10)
t = canvas.create_text(w + 20, h + 5, text="Hello")


def keypress(event):
    """The 4 key press"""
    x, y = 0, 0
    if event.char == "a":
        x = -10
    if event.char == "d":
        x = 10
    if event.char == "w":
        y = -10
    if event.char == "s":
        y = 10
    canvas.move(r1, x, y)
    canvas.move(t, x, y)


root.bind("<Key>", keypress)
root.mainloop()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
import tkinter as tk
 
root = tk.Tk()
 
canvas_width = 600
canvas_height = 400
w = canvas_width // 2
h = canvas_height // 2
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
 
r1 = canvas.create_rectangle(w, h, w + 40, h + 10)
text="Hellodfjhsgfjhgfjhgdjhgfjhdsgfjhgsdjhgfdjshgfjshgjdhfgjhgsfjdhudhfiughfuisdgbuidifid"
wraped_text="\n".join(wrap(text,40))
t = canvas.create_text(w + 20, h + 5, text=wraped_text)
 
 
def keypress(event):
    """The 4 key press"""
    x, y = 0, 0
    if event.char == "a":
        x = -10
    if event.char == "d":
        x = 10
    if event.char == "w":
        y = -10
    if event.char == "s":
        y = 10
    canvas.move(r1, x, y)
    canvas.move(t, x, y)
 
 
root.bind("<Key>", keypress)
root.mainloop()