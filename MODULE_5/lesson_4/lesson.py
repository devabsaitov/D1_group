# web site

from tkinter import *

win = Tk()
win.geometry('500x500')
win.config(bg= 'yellow')

box = StringVar()
i = Button(win , text = 'create account' ,
           font = ('aakar', 15 , 'bold') ,
           bg = 'yellow',
           highlightbackground = "yellow",
           borderwidth = 0,
           activebackground = "yellow"
           )
i.pack()

win.mainloop()




