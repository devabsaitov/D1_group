# txt = "Python"
# print(len(txt))
#
# list_ = [1,2,3,4]
# print(len(list_))

from tkinter import *

win = Tk()
win.geometry("500x500")
canvas = Canvas(win , width=500, height=500)

canvas.pack()
class Shape:
    def draw(self):
        pass
    def elase(self):
        pass

class Restangle(Shape):
    def draw(self):
        canvas.create_rectangle(20, 20, 300, 300, fill = "blue")
class Circle(Shape):
    def draw(self):
        canvas.create_oval(300,300, 350, 350, fill = "red")
Restangle().draw()
Circle().draw()
win.mainloop()
