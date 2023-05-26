"""
TKINTER

widget:
    Label
    Entry
    Button
    ListBox
    CheckBox
    RadioButton
    ComboBox
    Frame

"""

from tkinter import *

win = Tk()
# win.geometry("1000x2040")
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))

canvas = Canvas(win, height = height , width = width , bg = "red")
canvas.pack()

# canvas.create_line(10 , 100 , width, 100 , 400, 400 , 1000 , 500  , width = 10 , fill = "yellow")

# ==================================================================
def show_rectangle(event):
    print(event.keysym)
    # if event.char == 'a':
    #     canvas.create_rectangle(0, 0, width, height, width=10, fill="orange")
    # elif event.char == 'b':
    #     canvas.create_rectangle(0, 0, width, height, width=10, fill="green")

win.bind("<Key>" , show_rectangle)

# ==================================================================

# canvas.create_oval(20 , 20 , 500 , 500 , fill = "yellow" , width = 20)
# canvas.create_arc(600 , 600 , 1000 , 1000 ,start =0  , extent = 180 ,  fill = "yellow" , width = 20)
# canvas.create_text(300 , 300 , text = "D1 Junior" , font = ("aakar", 100 , "bold"))



win.mainloop()
