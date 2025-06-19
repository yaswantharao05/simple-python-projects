from turtle import Turtle
import random


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.score = 0
        self.timmy = Turtle()

    def move_up(self):
        if self.ycor() < 320:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -270:
            self.goto(self.xcor(), self.ycor() - 20)

    def divider(self):
        self.timmy.penup()
        self.timmy.pensize(6)
        self.timmy.goto(0, -320)
        self.timmy.setheading(90)
        self.timmy.color('white')
        for _ in range(21):
            self.timmy.pendown()
            self.timmy.forward(15)
            self.timmy.penup()
            self.timmy.forward(20)

