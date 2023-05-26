from tkinter import *
from PIL import Image , ImageTk

WIDTH = 900
HEIGHT = 900
win = Tk()
win.geometry(f"{WIDTH}x{HEIGHT}")
win.title("Move player")


def load_img(img_name, w , h , rotate):
    img = Image.open(img_name)
    img = img.resize((w,h))
    img = img.rotate(rotate)
    img = ImageTk.PhotoImage(image = img)
    return img

player1_img1 = load_img("player1.png" , 100 , 100 , 0)
player1_img2 = load_img("player1.png" , 100 , 100 , 90)
player1_img3 = load_img("player1.png" , 100 , 100 , -90)
player1_img4 = load_img("player1.png" , 100 , 100 , -180)

player2_img1 = load_img("player2.png" , 100 , 100 , 0)
player2_img2 = load_img("player2.png" , 100 , 100 , 90)
player2_img3 = load_img("player2.png" , 100 , 100 , -90)
player2_img4 = load_img("player2.png" , 100 , 100 , -180)



canvas = Canvas(win, width = WIDTH, height = HEIGHT, bg = "green")
canvas.pack()

player1_x1 = WIDTH / 2
player1_y1 = HEIGHT / 2

player2_x1 = WIDTH / 3
player2_y1 = HEIGHT / 3

player1 = canvas.create_image
player1(player1_x1 , player1_y1 , image=player1_img1)

player2 = canvas.create_image
player2(player2_x1 , player2_y1 , image=player2_img1)

position_player1_img = player1_img1
position_player2_img = player2_img1


def draw_player():
    canvas.delete('all')
    player1(player1_x1 , player1_y1 , image=position_player1_img)

    player2(player2_x1 , player2_y1 , image=position_player2_img)



def move_function(event):
    global player1_y1 , player1_x1 , player2_y1 , player2_x1 , position_player1_img , position_player2_img
    print(event.keysym)
    if event.char == 'w':
        player1_y1 -= 10
        draw_player()
        position_player1_img = player1_img1


    if event.char == 'a':
        player1_x1 -= 10
        draw_player()
        position_player1_img = player1_img2

    if event.char == 's':
        player1_y1 += 10
        draw_player()
        position_player1_img = player1_img4

    if event.char == 'd':
        player1_x1 += 10
        draw_player()
        position_player1_img = player1_img3


    if event.keysym == 'Up':
        player2_y1 -= 10
        draw_player()
        position_player2_img = player2_img1
    if event.keysym == 'Left':
        player2_x1 -= 10
        draw_player()
        position_player2_img = player2_img2

    if event.keysym == 'Right':
        player2_x1 += 10
        draw_player()
        position_player2_img = player2_img3
    if event.keysym == 'Down':
        player2_y1 += 10
        draw_player()
        position_player2_img = player2_img4



win.bind('<KeyPress>', move_function)



win.mainloop()