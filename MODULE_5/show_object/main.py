from tkinter import *
from PIL import Image , ImageTk

def load_image(image_name, w, h):
    img = Image.open(f'image/{image_name}')
    img = img.resize((w , h))
    img = ImageTk.PhotoImage(image = img)
    return img

def product1_motion(e):
    product1_canvas.delete('all')
    product1_canvas.create_image(200 , 200 , image= product1_2)
def product1_leave(e):
    product1_canvas.delete('all')
    product1_canvas.create_image(200 , 200 , image= product1_1)

def show_obj():
    global product1_canvas , product1_2 , product1_1
    win = Tk()
    win.geometry('1500x500')

    product1_1 = load_image('product1_1.png', 400, 400)
    product1_2 = load_image('product1_2.png', 400, 400)
    product1_canvas = Canvas(win , width = 400 , height=400)
    product1_canvas.place(relx = 0.1 , rely = 0.2)
    product1_canvas.create_image(200 , 200, image = product1_1)
    product1_canvas.bind('<Motion>' , product1_motion)
    product1_canvas.bind('<Leave>' , product1_leave)



    win.mainloop()
show_obj()
