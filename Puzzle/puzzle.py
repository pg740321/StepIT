#    Puzzle

# import turtle
import random
from tkinter import messagebox
from turtle import Turtle, Screen

ROWCOUNT = 4
COLCOUNT = 4
PENSIZE = 5
ZAOBLENI = 4

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
    if pole[ROWCOUNT - 1][COLCOUNT - 1] == '':
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
                j = j + 1

            i = i + 1

    return ok


# -------------------------------------------------------------------------------


def init_hraci_pole():
    cisla = []
    for i in range(1, ROWCOUNT * COLCOUNT):
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

    return


# -------------------------------------------------------------------------------


def hodnota_pole_na_pozici(x, y):
    ypoz = screen.window_height() // 2
    # screen.title(f"{x},{y}")
    for radky in pole:
        if (y <= ypoz) and (y >= ypoz - BTNHEIGHT):
            xpoz = - (screen.window_width() // 2)
            for sloupce in radky:
                if (x >= xpoz) and (x <= xpoz + BTNWIDTH):
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

            kontrola_vitezstvi()
    return


# -------------------------------------------------------------------------------


def vykresli_dlazdici(x, y, text):
    t.penup()
    t.goto(x + PENSIZE * 2 - ZAOBLENI, y)
    t.pendown()

    t.begin_fill()

    t.pen(pencolor="black", fillcolor="DarkGray", pensize=PENSIZE, speed=9)

    for _ in range(2):
        t.forward(BTNWIDTH - (2 * ZAOBLENI))
        t.circle(ZAOBLENI, 90)
        t.forward(BTNHEIGHT - (2 * ZAOBLENI))
        t.circle(ZAOBLENI, 90)

    t.end_fill()

    t.penup()
    t.goto(x + BTNWIDTH // 2, y + BTNHEIGHT // 2 - 20)
    t.pendown()
    t.write(text, align="center", font=("Arial", 30, "bold"))

    return


# -------------------------------------------------------------------------------


def hraci_pole():

    screen.tracer(0)

    t.hideturtle()

    vykresli_mezeru()

    for i in range(COLCOUNT):
        for j in range(ROWCOUNT):
            x = ((j - (COLCOUNT // 2)) * BTNHEIGHT) - PENSIZE + 1
            y = (((ROWCOUNT // 2) - i - 1) * BTNWIDTH) + PENSIZE - 2
            if pole[i][j] != '':
                vykresli_dlazdici(x, y, str(pole[i][j]))

    screen.tracer(1)

    return


# -------------------------------------------------------------------------------

def vykresli_mezeru():
    # Najdu mezeru
    i = 0
    j = 0

    while (i < ROWCOUNT) and (pole[i][j] != ''):
        j = 0
        while (j < COLCOUNT) and (pole[i][j] != ''):
            j = j + 1

        if (j >= COLCOUNT):
            j = 0
            i = i + 1

    x = - screen.window_width() // 2
    y = screen.window_height() // 2

    for _ in range(j):
        x = x + BTNWIDTH

    for _ in range(i):
        y = y - BTNHEIGHT

    t.hideturtle()
    t.fillcolor("white")

    t.begin_fill()

    t.penup()
    t.goto(x - 10, y + 10)
    t.pendown()

    for _ in range(2):
        t.forward(BTNWIDTH + 20)
        t.right(90)
        t.forward(BTNHEIGHT + 20)
        t.right(90)

    t.end_fill()

    return

# -------------------------------------------------------------------------------


def posun_pole(kam):
    # Najdu mezeru
    i = 0
    j = 0
    while (i < ROWCOUNT) and (pole[i][j] != ''):
        j = 0
        while (j < COLCOUNT) and (pole[i][j] != ''):
            j = j + 1

        if (j >= COLCOUNT):
            j = 0
            i = i + 1

    if (j < COLCOUNT) and (i < ROWCOUNT) and (pole[i][j]) == '':
        x = -1
        y = -1

        if (kam == "Up"):
            x = i + 1
            y = j
        elif (kam == "Down"):
            x = i - 1
            y = j
        elif (kam == "Left"):
            x = i
            y = j + 1
        elif (kam == "Right"):
            x = i
            y = j - 1

    if (((x >= 0) and (x < COLCOUNT))
            and ((y >= 0) and (y < ROWCOUNT))):
        pole[i][j] = pole[x][y]
        pole[x][y] = ''

        hraci_pole()

        kontrola_vitezstvi()
    return


# -------------------------------------------------------------------------------


def key_arrow_Down():
    posun_pole('Down')
    return


# -------------------------------------------------------------------------------


def key_arrow_Up():
    posun_pole('Up')
    return


# -------------------------------------------------------------------------------


def key_arrow_Left():
    posun_pole('Left')
    return


# -------------------------------------------------------------------------------


def key_arrow_Right():
    posun_pole('Right')
    return


# -------------------------------------------------------------------------------


def key_Esc():
    Screen().bye()
    return


# -------------------------------------------------------------------------------


def keyboard_commands():
    #    screen.onkey(key_Arrow_Up,"w")
    #    screen.onkey(key_Arrow_Down,"s")
    #    screen.onkey(key_Arrow_Right,"d")
    #    screen.onkey(key_Arrow_Left,"a")

    screen.onkey(key_arrow_Up, "Up")
    screen.onkey(key_arrow_Down, "Down")
    screen.onkey(key_arrow_Right, "Right")
    screen.onkey(key_arrow_Left, "Left")
    screen.onkey(key_Esc, "Escape")
    return


# -------------------------------------------------------------------------------


def kontrola_vitezstvi():
    if hotovo() == True:
        messagebox.showinfo("Puzzle", "Vyhrál jsi")
        nova_hra()

# -------------------------------------------------------------------------------


screen = Screen()
screen.setup(BTNWIDTH * COLCOUNT + PENSIZE * (COLCOUNT - 1),
             BTNHEIGHT * ROWCOUNT + PENSIZE * (COLCOUNT - 1)
             )
screen.title("Puzzle")
screen.bgcolor("white")

t = Turtle()
t.hideturtle()
t.speed(0)

nova_hra()

keyboard_commands()
screen.onclick(click_na_dlazdici)
screen.listen()
screen.mainloop()
