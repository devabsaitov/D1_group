from tkinter import *
from PIL import Image , ImageTk

def load_img(img_name, w , h , rotate):
    img = Image.open(img_name)
    img = img.resize((w,h))
    img = img.rotate(rotate)
    img = ImageTk.PhotoImage(image = img)
    return img

def scrollbar(root):
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    return second_frame


def change_img1(e):
    global productga_joy , product_green2
    print(e)
    e.state.delete('all')
    productga_joy.create_image(350, 350 , image = product_green2)
def change_img2(e):
    global productga_joy , product_green1
    print(e)
    e.state.delete('all')
    e.state.create_image(350, 350 , image = product_green1)


def main_win():
    global productga_joy , product_green2 , product_green1
    win = Tk()
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    win.geometry("%dx%d" % (width, height))
    scroll_win = scrollbar(win)

    # -------------- image ----------------------

    body_1 = load_img('image/body_1.png', width, 900, 0)
    product_green1 = load_img('image/product_green1.png', 400, 400, 0)
    product_green2 = load_img('image/product_green2.png', 400, 400, 0)



    # ---------------- header ---------------------
    header = Frame(scroll_win , width = width , height=150, bg='yellow')
    header.pack()

    # ----------------- body -------------------

    body = Frame(scroll_win, width=width, height=3000, bg='green')


    Label(body , image = body_1 ).pack()

    b1 = Button(body , text = 'Show Now', font = ('aakar', 16 , 'bold'))
    b1.place(relx = 0.2 , rely = 0.6)

    title = Label(body , text = 'Our Products' , font = ('aakar', 20 , 'bold'))
    title.pack(pady = 40)

    productga_joy = Canvas(body , width = width , height = 700 , bg = 'blue')
    productga_joy.pack()
    productga_joy.create_image(350, 350 , image=product_green1)
    productga_joy.bind('<Motion>', change_img1)
    productga_joy.bind('<Leave>', change_img2)


    body.pack()


    # ------------------ footer -------------------

    footer = Frame(scroll_win, width=width, height=300, bg='red')
    footer.pack()

    # ---------------------------------------

    win.mainloop()

main_win()
