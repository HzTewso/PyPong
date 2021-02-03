import turtle

pencere = turtle.Screen()
canvas = pencere.getcanvas()
root = canvas.winfo_toplevel()
pencere.title('PyPong Game')
pencere.bgcolor('black')
pencere.setup(width=800, height=600)
pencere.tracer(0)

racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape('square')
racket_a.color('white')
racket_a.penup()
racket_a.goto(-350, 0)
racket_a.shapesize(5, 1)

racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape('square')
racket_b.color('white')
racket_b.penup()
racket_b.goto(350, 0)
racket_b.shapesize(5, 1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 0.15
ball.dy = 0.15

skor = turtle.Turtle()
skor.speed(0)
skor.color('white')
skor.penup()
skor.goto(0, 260)
skor.write('Oyuncu A:0    Oyuncu B:0', align='center', font=('courier', 24, 'bold'))
skor.hideturtle()
skor_a = 0
skor_b = 0


def racket_a_up():
    y = racket_a.ycor()
    y = y + 20
    racket_a.sety(y)
def racket_a_down():
    y = racket_a.ycor()
    y = y - 20
    racket_a.sety(y)
def racket_b_up():
    y = racket_b.ycor()
    y = y + 20
    racket_b.sety(y)
def racket_b_down():
    y = racket_b.ycor()
    y = y - 20
    racket_b.sety(y)

pencere.listen()
pencere.onkeypress(racket_a_up, "w")
pencere.onkeypress(racket_a_down, "s")
pencere.onkeypress(racket_b_up, "Up")
pencere.onkeypress(racket_b_down, "Down")

def winclose():
    global winbug
    winbug = False
root.protocol("WM_DELETE_WINDOW", winclose)
winbug = True

while winbug:
    pencere.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.dy = ball.dy * -1

    if ball.xcor()>390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        skor_a = skor_a + 1
        skor.clear()
        skor.write("Oyuncu A:{}    Oyuncu B:{}".format(skor_a, skor_b), align='center', font=('courier', 24, 'bold'))
    if ball.xcor()<-390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        skor_b = skor_b + 1
        skor.clear()
        skor.write("Oyuncu A:{}    Oyuncu B:{}".format(skor_a, skor_b), align='center', font=('courier', 24, 'bold'))
    if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<racket_b.ycor()+60 and ball.ycor()>racket_b.ycor()-60):
        ball.setx(340)
        ball.dx = ball.dx * -1
    if(ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<racket_a.ycor()+60 and ball.ycor()>racket_a.ycor()-60):
        ball.setx(-340)
        ball.dx = ball.dx * -1
