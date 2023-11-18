#    Puzzle

import turtle
import random
from tkinter import messagebox

ROWCOUNT = 4
COLCOUNT = 4
PENSIZE = 5
ZAOBLENI = 5

BTNWIDTH = 100
BTNHEIGHT = 100

pole = [['' for _ in range(ROWCOUNT)] for _ in range(COLCOUNT)]

# -------------------------------------------------------------------------------


def nova_hra():
    init_hraci_pole()
    hraci_pole()
    return

# -------------------------------------------------------------------------------


def hotovo():
    hodnota = 0
    ok = False
    if pole[ROWCOUNT-1][COLCOUNT-1] == '':
        i = 0
        ok = True
        while (ok) and (i < ROWCOUNT):
            j = 0
            while (ok) and (j < COLCOUNT):
                hodnota = hodnota + 1
                ok = (
                    (
                        (i == ROWCOUNT - 1)
                        and (j == COLCOUNT - 1)
                        and (pole[i][j] == '')
                    )
                    or
                    (pole[i][j] == hodnota)
                )
                j = j+1

            i = i+1

    return ok

# -------------------------------------------------------------------------------


def init_hraci_pole():
    cisla = []
    for i in range(1, ROWCOUNT*COLCOUNT):
        cisla.append(i)

    for i in range(ROWCOUNT):
        for j in range(COLCOUNT):
            if len(cisla) > 0:
                cislo = random.choice(cisla)
                pole[i][j] = cislo
                cisla.remove(cislo)
            else:
                pole[i][j] = ''

#    Odladeni hotovo()
#    cislo = 1
#    for i in range(ROWCOUNT):
#        for j in range(COLCOUNT):
#            pole[i][j] = cislo
#            cislo = cislo + 1
#    pole[COLCOUNT-1][ROWCOUNT-1] = ''

# -------------------------------------------------------------------------------


def hodnota_pole_na_pozici(x, y):
    ypoz = screen.window_height() // 2
    # screen.title(f"{x},{y}")
    for radky in pole:
        if (y <= ypoz) and (y >= ypoz - BTNHEIGHT):
            xpoz = - (screen.window_width() // 2)
            for sloupce in radky:
                if (x >= xpoz) and (x <= xpoz+BTNWIDTH):
                    #                   screen.title(f"{sloupce}")
                    return sloupce
                else:
                    xpoz = xpoz + BTNWIDTH
        else:
            ypoz = ypoz - BTNHEIGHT

    return "-1"

# -------------------------------------------------------------------------------


def click_na_dlazdici(x, y):
    nalezeno = hodnota_pole_na_pozici(x, y)

    # kliknuto na nejake pole
    if (nalezeno != "") and (nalezeno != "-1"):
        # podivam se nahoru, jestli je tam prazdno
        nalezenamezera = hodnota_pole_na_pozici(x, y - BTNHEIGHT)
        if nalezenamezera != "":
            # podivam se dolu, jestli je tam prazdno
            nalezenamezera = hodnota_pole_na_pozici(x, y + BTNHEIGHT)
            if nalezenamezera != "":
                # podivam se doleva, jestli je tam prazdno
                nalezenamezera = hodnota_pole_na_pozici(x - BTNWIDTH, y)
                if nalezenamezera != "":
                    # podivam se doprava, jestli je tam prazdno
                    nalezenamezera = hodnota_pole_na_pozici(x + BTNWIDTH, y)
                    if nalezenamezera != "":
                        return

        if nalezenamezera == "":
            for i in range(COLCOUNT):
                for j in range(ROWCOUNT):
                    if pole[i][j] == nalezeno:
                        pole[i][j] = ""
                    elif pole[i][j] == "":
                        pole[i][j] = nalezeno

            hraci_pole()

            if hotovo() == True:
                messagebox.showinfo("Puzzle", "Vyhrál jsi")
                nova_hra()

    return

# -------------------------------------------------------------------------------


def vykresli_dlazdici(x, y, text):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(10)

    t.up()
    t.goto(x + PENSIZE * 2 - ZAOBLENI, y)
    t.down()

    t.begin_fill()
    t.pen(pencolor="black", fillcolor="DarkGray",  pensize=PENSIZE, speed=9)

    for _ in range(2):
        t.fd(BTNWIDTH-2*ZAOBLENI)
        t.circle(ZAOBLENI, 90)
        t.fd(BTNHEIGHT-2*ZAOBLENI)
        t.circle(ZAOBLENI, 90)

    t.end_fill()

    t.up()
    t.goto(x + BTNWIDTH // 2, y + BTNHEIGHT // 2 - 20)
    t.down()
    t.write(text, align="center", font=("Arial", 30, "bold"))

# -------------------------------------------------------------------------------


def hraci_pole():
    screen.clearscreen()
    screen.resetscreen()
    screen.bgcolor("white")
    screen.onclick(click_na_dlazdici)
    screen.tracer(0)

    for i in range(COLCOUNT):
        for j in range(ROWCOUNT):
            x = ((j - (COLCOUNT // 2))*BTNHEIGHT) - PENSIZE + 1
            y = (((ROWCOUNT // 2) - i - 1)*BTNWIDTH) + PENSIZE - 2
            if pole[i][j] != '':
                vykresli_dlazdici(x, y, str(pole[i][j]))

    screen.tracer(1)

# -------------------------------------------------------------------------------


screen = turtle.Screen()
screen.setup(BTNWIDTH*COLCOUNT + PENSIZE*(COLCOUNT-1),
             BTNHEIGHT*ROWCOUNT + PENSIZE*(COLCOUNT-1))
screen.title("Puzzle")
screen.bgcolor("white")
screen.onclick(click_na_dlazdici)

nova_hra()

turtle.done()
