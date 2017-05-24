import turtle as T
import math

def circle(radio, x, y, color):
    T.color(color, color)
    T.setheading(0)
    T.begin_fill()
    T.penup()
    T.setx(x)
    T.sety(y - radio)
    T.pendown()
    T.circle(radio)
    T.end_fill()

def poligonoRegular(longitud, numeroLados, x_o, y_o, color):
    T.color(color, color)
    T.setheading(0)
    T.begin_fill()
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    anguloPoligono = 360 // numeroLados
    for i in range(numeroLados):
        T.forward(longitud)
        T.left(anguloPoligono)

def estrella(longitud, x_o, y_o, color):
    T.color(color, color)
    T.setheading(0)
    T.begin_fill()
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    for i in range(10):
        if i % 2 == 0:
            T.left(72)
        else:
            T.right(144)
        T.forward(longitud)
    T.end_fill()

def corazon(longitud, x_o, y_o, color):
    T.color(color, color)
    T.setheading(0)
    T.begin_fill()
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    T.left(90)
    T.circle(longitud, 180 + 53)
    tmp = longitud / math.tan(53 * math.pi / 360)
    T.forward(tmp)
    T.penup()
    T.setx(x_o)
    T.right(180 + 53)
    T.sety(y_o)
    T.pendown()
    T.left(180)
    T.circle(longitud, -(180 + 53))
    T.backward(tmp)
    T.end_fill()

def sierpinsky(longitud, nivel, x_o, y_o, color):
    T.color(color, color)
    T.setheading(0)
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    T.begin_fill()
    if nivel == 1:
        T.forward(longitud)
        T.left(120)
        T.forward(longitud)
        T.left(120)
        T.forward(longitud)
        T.left(120)
    else:
        x = T.xcor()
        y = T.ycor()
        sierpinsky(longitud / 2, nivel - 1, x, y, color)
        sierpinsky(longitud / 2, nivel - 1, x + longitud / 2, y, color)
        sierpinsky(longitud / 2, nivel - 1, x + longitud / 4, y + longitud / 4 * 3 ** 0.5, color)
    T.end_fill()


def koch(longitud, nivel, color):
    T.color(color, color)
    T.begin_fill()
    if nivel == 0:
        T.forward(longitud)
    else:
        koch(longitud / 3, nivel - 1, color)
        T.left(60)
        koch(longitud / 3, nivel - 1, color)
        T.right(120)
        koch(longitud / 3, nivel - 1, color)
        T.left(60)
        koch(longitud / 3, nivel - 1, color)
    T.end_fill()


def trianguloCircular(longitud, x_o, y_o, color):
    T.color(color, color)
    T.begin_fill()
    T.setheading(0)
    T.circle(longitud, 60)
    T.left(60)
    T.circle(longitud, 60)
    T.left(60)
    T.circle(longitud, 60)
    T.end_fill()


def figuraRara1(longitud, x_o, y_o, color):
    T.color(color, color)
    T.begin_fill()
    T.setheading(0)
    T.circle(longitud, 120)
    T.left(120)
    T.circle(longitud, 120)
    T.left(120)
    T.circle(longitud, 120)
    T.end_fill()


def cuadradoCircular(longitud, x_o, y_o, color):
    T.color(color, color)
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    T.begin_fill()
    T.setheading(135)
    T.circle(longitud, 90)
    T.setheading(45)
    T.circle(longitud, 90)
    T.setheading(315)
    T.circle(longitud, 90)
    T.setheading(225)
    T.circle(longitud, 90)
    T.end_fill()


def trianguloRaro(longitud, x_o, y_o, color):
    T.color(color, color)
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    T.begin_fill()
    T.setheading(120)
    T.circle(longitud, 120)
    T.left(180)
    T.forward(longitud * 2)
    T.end_fill()


def figuraRara2(longitud, x_o, y_o, color):
    T.color(color, color)
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    T.begin_fill()
    T.setheading(180)
    T.circle(longitud, 180)
    T.setheading(90)
    T.circle(-longitud, 90)
    T.setheading(180)
    T.circle(-longitud, 90)
    T.end_fill()


def pacman(longitud, x_o, y_o, color):
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    T.color(color, color)
    T.begin_fill()
    T.setheading(150)
    T.circle(longitud, 270)
    T.left(90)
    T.forward(longitud)
    T.end_fill()
    T.penup()
    x, y = T.pos()
    T.setx(x - longitud / 3)
    T.sety(y + longitud / 2)
    T.pendown()


def cruz(longitud, x_o, y_o, color):
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    T.color(color, color)
    T.setheading(-30)
    T.begin_fill()
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    anguloPoligono = 360 // 3
    for i in range(4):
        T.left(90)
        for j in range(3):
            T.forward(longitud)
            T.left(anguloPoligono)
    T.end_fill()


def flor(longitud, x_o, y_o, color):
    T.color("black", color)
    T.setheading(-30)
    T.begin_fill()
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    T.pensize(2)
    anguloPoligono = 360 // 3
    for i in range(10):
        T.left(36)
        for j in range(3):
            if i % 2 == 0:
                T.forward(longitud // 2)
            else:
                T.forward(longitud)
            T.left(anguloPoligono)
    T.end_fill()
    T.pensize(1)


def figuraRara3(longitud, x_o, y_o, color):
    T.color("black", color)
    T.setheading(90)
    T.begin_fill()
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    T.circle(longitud, 180)
    T.circle(longitud // 2, 180)
    T.left(180)
    T.circle(longitud // 2, 180)
    T.end_fill()


def figuraRara4(longitud, x_o, y_o, color):
    T.color(color, color)
    T.setheading(90)
    T.begin_fill()
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    T.circle(longitud, 180)
    T.circle(longitud // 2, 180)
    T.left(360)
    T.circle(-longitud // 2, 180)
    T.end_fill()


def trapecioCircular(longitud, x_o, y_o, color):
    T.color(color, color)
    T.setheading(120)
    T.begin_fill()
    T.penup()
    T.setx(x_o)
    T.sety(y_o)
    T.pendown()
    T.circle(longitud, 120)
    T.left(180)
    T.forward(1.3 * longitud)
    T.left(-120)
    T.circle((1 - 1.3 / 3 ** 0.5) * longitud, 120)
    T.end_fill()

# MAIN

circle( 50, 1, 100, "red")
estrella( 90,  90, 200, "orange")
corazon( 30, -150, -100, "blue")
sierpinsky( 60, 3, -100, -100, "green")
koch( 150, 3, "chocolate")
trianguloCircular( 120, -50, -100, "cyan")
figuraRara1( 150, 40, -40, "gold")
cuadradoCircular( 65, 50, -200, "gray")
trianguloRaro( 111, 99, 45, "lavender")
figuraRara2( 109, -200, -30, "peru")
pacman( 20, 88, 99, "pink")
cruz( 45, 100, 45, "wheat")
flor( 74, -33, 90, "tomato")
figuraRara3(-120, 99, -99, "violet")
figuraRara4(-170, 99, -70, "tan")
poligonoRegular(100, 9, 0, 0, "red")
T.done()
