import turtle

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#giocatore1
giocatore1 = turtle.Turtle()
giocatore1.speed(0)
giocatore1.shape("square")
giocatore1.color("white")
giocatore1.shapesize(stretch_wid=5, stretch_len=1)
giocatore1.penup()
giocatore1.goto(-350, 0)

#giocatore2
giocatore2 = turtle.Turtle()
giocatore2.speed(0)
giocatore2.shape("square")
giocatore2.color("white")
giocatore2.shapesize(stretch_wid=5, stretch_len=1)
giocatore2.penup()
giocatore2.goto(350, 0)

#palla
palla = turtle.Turtle()
palla.speed(0)
palla.shape("circle")
palla.color("white")
palla.penup()
palla.goto(0, 0)
palla.dx = 0.2     #d = delta
palla.dy = 0.2
#funzioni
def giocatore1_su():
    y = giocatore1.ycor()
    y += 20
    giocatore1.sety(y)

def giocatore1_giu():
    y = giocatore1.ycor()
    y -= 20
    giocatore1.sety(y)

def giocatore2_su():
    y = giocatore2.ycor()
    y += 20
    giocatore2.sety(y)

def giocatore2_giu():
    y = giocatore2.ycor()
    y -= 20
    giocatore2.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(giocatore1_su, 'w')
wn.onkeypress(giocatore1_giu, 's')
wn.onkeypress(giocatore2_su, 'Up')
wn.onkeypress(giocatore2_giu, 'Down')

#loop principale
while True:
    wn.update()

    #muovo palla
    palla.setx(palla.xcor() + palla.dx)
    palla.sety(palla.ycor() + palla.dy)
    #controllo bordi
    if palla.ycor() > 290:
        palla.sety(290)
        palla.dy *= -1
    if palla.ycor() < -290:
        palla.sety(-290)
        palla.dy *= -1
    if palla.xcor() > 390:
        palla.goto(0, 0)
        palla.dx *= -1
    if palla.xcor() < -390:
        palla.goto(0, 0)
        palla.dx *= -1

    #collisione giocatore-palla
    if (palla.xcor() > 340 and palla.xcor() < 350) and (palla.ycor() < giocatore2.ycor() + 50 and palla.ycor() > giocatore2.ycor() - 50):
        palla.setx(340)
        palla.dx *= -1
    if (palla.xcor() < -340 and palla.xcor() < -350) and (palla.ycor() < giocatore1.ycor() + 50 and palla.ycor() > giocatore1.ycor() - 50):
        palla.setx(-340)
        palla.dx *= -1
