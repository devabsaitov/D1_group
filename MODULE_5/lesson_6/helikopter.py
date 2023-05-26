from tkinter import *
from PIL import Image, ImageTk

win = Tk()


def load_image(image_name, w, h, r):
    img = Image.open(f'image/{image_name}')
    img = img.resize((w, h))
    img = img.rotate(r)
    img = ImageTk.PhotoImage(image=img)
    return img


game_polya = Canvas(win, width=600, height=600, bg='blue')
game_polya.pack()

helikoptor_img = load_image('helikaptor.png', 150, 120, 0)
galichka_img = load_image('galichka.png', 80, 50, 0)
player = game_polya.create_image(100, 500, image=helikoptor_img)
H = game_polya.create_rectangle(370, 450, 470, 480, fill='gray')
H_2 = game_polya.create_rectangle(100, 180, 200, 210, fill='gray')


def move_helicaptor(event):
    print(event.keysym)
    if event.keysym == 'Left':
        game_polya.move(player, -20, 0)
    if event.keysym == 'Right':
        game_polya.move(player, 20, 0)
    if event.keysym == 'Up':
        game_polya.move(player, 0, -20)


def gravitation_function():
    player_pos = game_polya.coords(player)
    H_pos = game_polya.coords(H)
    H_pos_2 = game_polya.coords(H_2)
    print(H_pos)
    if H_pos[0] - 60 < player_pos[0] and player_pos[1] > H_pos[1] - 40 and H_pos[2] + 80 > player_pos[0] + 60:
        game_polya.create_image(520 , 470 , image = galichka_img)

    elif H_pos_2[0] - 60 < player_pos[0] and \
            player_pos[1] > H_pos_2[1] - 40 and \
            H_pos_2[2] + 80 > player_pos[0] + 60 and \
            H_pos_2[3] > player_pos[1] - 10:

        game_polya.create_image(230, 200, image=galichka_img)

    elif player_pos[1] < 501:
        game_polya.move(player, 0, 3)
    game_polya.after(50, gravitation_function)


gravitation_function()
win.bind('<Key>', move_helicaptor)
win.mainloop()
