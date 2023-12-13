# Puzzle #

import random
from tkinter import messagebox
from turtle import Turtle, Screen

ROWCOUNT = 4
COLCOUNT = 4
PENSIZE = 3
ZAOBLENI = 4

BTNWIDTH = 100
BTNHEIGHT = 100

pole = []

# --------------------------------------------------------------------------- #


def nova_hra():
    init_hraci_pole()
    vykresli_hraci_pole()
    return

# --------------------------------------------------------------------------- #


def init_hraci_pole():
    cisla = []
    for i in range(1, ROWCOUNT * COLCOUNT):
        cisla.append(i)

    pole.clear()
    while len(cisla) > 0:
        cislo = random.choice(cisla)
        pole.append(cislo)
        cisla.remove(cislo)

    pole.append("")

    # Odladeni hotovo() #
    #    pole.clear()#
    #    for i in range(1, ROWCOUNT * COLCOUNT):#
    #        pole.append(i)#
    #    pole.append("")#

    return

# --------------------------------------------------------------------------- #


def hotovo():
    i = 0
    ok = True

    # posledni prvek je mezera, kterou nebudu kontrolovat #
    while ok and (i < len(pole) - 1):
        if pole[i] == i + 1:
            ok = True
        else:
            ok = False
        i = i + 1

    return ok

# --------------------------------------------------------------------------- #


def kontrola_vitezstvi():
    if hotovo():
        messagebox.showinfo("Puzzle", "Vyhrál jsi")
        nova_hra()

# --------------------------------------------------------------------------- #


def vykresli_dlazdici(x, y, text):
    screen.tracer(0)

    t.penup()
    t.goto(x + PENSIZE * 2 - ZAOBLENI, y)
    t.pendown()

    t.begin_fill()

    if text == "":
        t.pen(pencolor="white", fillcolor="white", pensize=PENSIZE, speed=9)
    else:
        t.pen(pencolor="black", fillcolor="DarkGray", pensize=PENSIZE, speed=9)

    for _ in range(2):
        t.forward(BTNWIDTH - 3 * ZAOBLENI)
        t.circle(ZAOBLENI, 90)
        t.forward(BTNHEIGHT - 3 * ZAOBLENI)
        t.circle(ZAOBLENI, 90)

    t.end_fill()

    t.penup()
    t.goto(x + BTNWIDTH // 2, y + BTNHEIGHT // 2 - 20)
    t.pendown()
    t.write(text, align="center", font=("Arial", 30, "bold"))

    screen.tracer(1)

    return

# --------------------------------------------------------------------------- #


def vykresli_hraci_pole():
    for i in range(ROWCOUNT * COLCOUNT):
        sloupec = i % COLCOUNT
        x = (- screen_width // 2) + sloupec * BTNWIDTH + 9

        radek = i // COLCOUNT + 1
        y = (screen_height // 2) - radek * BTNHEIGHT

        vykresli_dlazdici(x, y, str(pole[i]))
    return

# --------------------------------------------------------------------------- #


def vykresli_pole(index):
    sloupec = index % COLCOUNT
    x = (- screen_width // 2) + sloupec * BTNWIDTH + 9

    radek = index // COLCOUNT + 1
    y = (screen_height // 2) - radek * BTNHEIGHT

    vykresli_dlazdici(x, y, str(pole[index]))

# --------------------------------------------------------------------------- #


def index_pole_na_pozici(x, y):
    for i in range(ROWCOUNT * COLCOUNT + 1):
        sloupec = i % COLCOUNT
        xpoz = (- screen_width // 2) + sloupec * BTNWIDTH

        radek = i // COLCOUNT
        ypoz = (screen_height // 2) - radek * BTNHEIGHT

        if (xpoz <= x) and (x <= (xpoz + BTNWIDTH)):
            if (ypoz >= y) and (y >= ypoz - BTNHEIGHT):
                return i

    return -1

# --------------------------------------------------------------------------- #


def hodnota_pole_na_pozici(x, y):
    index = index_pole_na_pozici(x, y)
    if index > -1:
        return pole[index]
    else:
        return -1

# --------------------------------------------------------------------------- #


def click_na_dlazdici(x, y):
    nalezeno = index_pole_na_pozici(x, y)

    sloupec = nalezeno % COLCOUNT
    radek = nalezeno // COLCOUNT

    mezera = -1
    # mezara dole
    if (radek + 1) < ROWCOUNT:
        index = ((radek + 1) * COLCOUNT) + sloupec
        if pole[index] == "":
            mezera = index

    # mezara nahore
    if (mezera == -1) and (radek > 0):
        index = ((radek - 1) * COLCOUNT) + sloupec
        if pole[index] == "":
            mezera = index

    # mezara vpravo
    if (mezera == -1) and ((sloupec + 1) < COLCOUNT):
        index = (radek * COLCOUNT) + sloupec + 1
        if pole[index] == "":
            mezera = index

    # mezara vpravo
    if (mezera == -1) and (sloupec > 0):
        index = (radek * COLCOUNT) + sloupec - 1
        if pole[index] == "":
            mezera = index

    if mezera > -1:
        pole[mezera] = pole[nalezeno]
        pole[nalezeno] = ""

        vykresli_pole(nalezeno)
        vykresli_pole(mezera)

        kontrola_vitezstvi()
    return

# --------------------------------------------------------------------------- #


def posun_pole(kam):
    # Najdu mezeru

    mezera = pole.index("")

    sloupec = mezera % COLCOUNT
    radek = mezera // COLCOUNT

    index = -1
    # mezara dole
    if (kam == "Up") and (radek + 1) < ROWCOUNT:
        index = ((radek + 1) * COLCOUNT) + sloupec

    # mezara nahore
    if (kam == "Down") and (radek > 0):
        index = ((radek - 1) * COLCOUNT) + sloupec

    # mezara vpravo
    if (kam == "Left") and ((sloupec + 1) < COLCOUNT):
        index = (radek * COLCOUNT) + sloupec + 1

    # mezara vpravo
    if (kam == "Right") and (sloupec > 0):
        index = (radek * COLCOUNT) + sloupec - 1

    if index > -1:
        pole[mezera] = pole[index]
        pole[index] = ""

        vykresli_pole(index)
        vykresli_pole(mezera)

        kontrola_vitezstvi()
    return

# --------------------------------------------------------------------------- #


def key_arrow_down():
    posun_pole('Down')
    return

# --------------------------------------------------------------------------- #


def key_arrow_up():
    posun_pole('Up')
    return

# --------------------------------------------------------------------------- #


def key_arrow_left():
    posun_pole('Left')
    return

# --------------------------------------------------------------------------- #


def key_arrow_right():
    posun_pole('Right')
    return

# --------------------------------------------------------------------------- #


def key_Esc():
    if (messagebox.askquestion("Puzzle",
                               "Ukončit ?",
                               icon='question') == 'yes'):
        screen.bye()
    return

# --------------------------------------------------------------------------- #


def keyboard_commands():
    #    screen.onkey(key_Arrow_Up,"w")
    #    screen.onkey(key_Arrow_Down,"s")
    #    screen.onkey(key_Arrow_Right,"d")
    #    screen.onkey(key_Arrow_Left,"a")

    screen.onkey(key_arrow_up, "Up")
    screen.onkey(key_arrow_down, "Down")
    screen.onkey(key_arrow_right, "Right")
    screen.onkey(key_arrow_left, "Left")
    screen.onkey(key_Esc, "Escape")
    return

# --------------------------------------------------------------------------- #


if __name__ == '__main__':
    screen = Screen()

    screen_width = BTNWIDTH * COLCOUNT + PENSIZE * (COLCOUNT - 1) + 2
    screen_height = BTNHEIGHT * ROWCOUNT + PENSIZE * (COLCOUNT - 1) + 2
    screen.setup(screen_width, screen_height)

    screen.title("Puzzle")
    screen.bgcolor("white")

    t = Turtle()
    t.hideturtle()
    t.speed(9)

    nova_hra()

    keyboard_commands()
    screen.onclick(click_na_dlazdici)
    screen.listen()
    screen.mainloop()
