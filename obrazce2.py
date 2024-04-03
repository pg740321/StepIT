import turtle as tur

tur.hideturtle()
tur.speed(0)
tur.tracer(0)
tur.width(2)
tur.bgcolor('black')
r, g, b = 255, 0, 0

colordiv = 0.65;

#tur.begin_fill()

for i in range(255*3):
    tur.colormode(255)

    if i < 255//colordiv:
        g += colordiv
    elif i < (255*3)//colordiv:
        r -= colordiv
    elif i < 255:
        b += colordiv
    elif i < (255*4)//colordiv:
        g -= colordiv
    elif i < (255*5)//colordiv:
        r += colordiv
    else:
        b -= colordiv

    tur.fd(1 + i * 0.9)
#    tur.rt(89)
#    tur.rt(156)
#    tur.rt(198)
    tur.rt(105)
##    tur.rt(205)
    try:
      tur.pencolor(round(r), round(g), round(b))
    except:
      tur.pencolor(100, 100, 100)

#tur.end_fill()
tur.done()