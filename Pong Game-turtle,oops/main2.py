from turtle import Screen,Turtle
import time

screen = Screen()
# screen.screensize(canvwidth=1000, canvheight=900)
screen.setup(width=1.0, height=1.0)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

paddle = Turtle('square')
paddle.color('white')
paddle.speed(0)
paddle.setheading(90)
paddle.penup()
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.goto(630, 0)

timmy = Turtle()
timmy.penup()
timmy.pensize(6)
timmy.goto(0, -320)
timmy.setheading(90)
timmy.color('white')
for _ in range(21):
    timmy.pendown()
    timmy.forward(15)
    timmy.penup()
    timmy.forward(20)


def move_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)


def move_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)


screen.listen()
screen.onkeypress(key='Up', fun=move_up)
screen.onkeypress(key='Down', fun=move_down)

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    screen.update()

screen.exitonclick()
