from tkinter import *
from PIL import Image , ImageTk

def load_image(img_name , width, height):
    img = Image.open(f"image/{img_name}")
    img = img.resize((width, height))
    img = ImageTk.PhotoImage(image = img)
    return img

# dict , tuple ,int , str , list , set


config ={
    1:4,
    2:5,
    3:6,
    4:1,
    5:2,
    6:3
}

def src_function(btn):
    global src_active , language

    language[src_active].config(borderwidth=0, highlightbackground="#D8D8D8")
    for k , v in language.items():
        if btn == v:
            src_active = k
            v.config(borderwidth=1, highlightbackground="blue")



def dest_function(btn):
    global dest_active , language
    print(dest_active)
    language[dest_active].config(borderwidth=0, highlightbackground="#D8D8D8")
    for k, v in language.items():
        if btn == v:
            dest_active = k
            v.config(borderwidth=1, highlightbackground="blue")



def replace_function():
    global src_active , dest_active
    for k , v in language.items():
        if v == src_active:
            dest_active = config[k]
        if v == dest_active:
            src_active = config[k]




win = Tk()
win.geometry("1500x1000")
win.title("Google Translate")
google_img = load_image("google_img.png", 900 , 500)
replace_img = load_image("replace_img.png", 50 , 50)
ptichka_img = load_image("ptichka_img.png", 50 , 50)


google_canvas = Canvas(win , width = 900 , height = 350)
google_canvas.pack()
google_canvas.create_image(450 , 250 , image = google_img)

# ----------------------- src buttons ---------------------------------------------------
russian_src = Button(win , text = "Russian",
                     font = ('aakar', 20 , 'bold'),
                     borderwidth = 0,
                     activebackground = "#D8D8D8",
                     command = lambda : src_function(russian_src)
                     )
russian_src.place(relx = 0.1 , rely = 0.4)

english_src = Button(win, text="English",
                     font=('aakar', 20, 'bold'),
                     borderwidth=1,
                     activebackground="#D8D8D8",
                     highlightbackground = 'blue',
                     command=lambda: src_function(english_src)

                     )
english_src.place(relx=0.2, rely=0.4)

uzbek_src = Button(win, text="Uzbek",
                   font=('aakar', 20, 'bold'),
                   borderwidth=0,
                   activebackground="#D8D8D8",
                    command=lambda: src_function(uzbek_src)
                   )
uzbek_src.place(relx=0.3, rely=0.4)


text_src = Text(win , width = 70 , height = 20)
text_src.place(relx = 0.1 , rely = 0.5)

# ----------------------replace button ---------------------------------------
replace_btn = Button(win ,
                     image = replace_img,
                     borderwidth=0,
                     activebackground="#D8D8D8",
                     command = lambda : replace_function()
                     )
replace_btn.place(relx = 0.465 , rely = 0.4)

# ---------------------- dest buttons ---------------------------------------
russian_dest = Button(win, text="Russian",
                      font=('aakar', 20, 'bold'),
                      borderwidth=0,
                      activebackground="#D8D8D8",
                      command=lambda: dest_function(russian_dest)

                      )
russian_dest.place(relx=0.6, rely=0.4)

english_dest = Button(win, text="English",
                      font=('aakar', 20, 'bold'),
                      borderwidth=0,
                      activebackground="#D8D8D8",
                      command=lambda: dest_function(english_dest)
                      )
english_dest.place(relx=0.7, rely=0.4)

uzbek_dest = Button(win, text="Uzbek",
                    font=('aakar', 20, 'bold'),
                    borderwidth=1,
                    activebackground="#D8D8D8",
                    highlightbackground='blue',
                    command = lambda: dest_function(uzbek_dest)
                    )
uzbek_dest.place(relx=0.8, rely=0.4)

text_src = Text(win, width=70, height=20)
text_src.place(relx=0.49, rely=0.5)

# ----------------------------- Ptichka button ----------------------------------
ptichka_button = Button(win ,
                        image = ptichka_img,
                        borderwidth=0,
                        activebackground="#D8D8D8"
                        )
ptichka_button.place(relx = 0.465 , rely = 0.85)

src_active = english_src
dest_active = uzbek_dest

language = {
    1: russian_src,
    2: english_src,
    3: uzbek_src,

    4: russian_dest,
    5: english_dest,
    6: uzbek_dest
}

win.mainloop()




