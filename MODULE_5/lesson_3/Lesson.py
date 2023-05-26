from tkinter import *


win = Tk()
win.geometry('800x800')
win.config(bg= 'red')

def change_bg(e):
    if e.char == 'a':
        win.config(bg='yellow')
    if e.char =='b':
        win.config(bg='black')
def mouse_show(e):
    Button(win, text='test').pack()
win.bind("<Button-4>", mouse_show)
win.mainloop()