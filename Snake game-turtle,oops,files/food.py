from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('red')
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh_food()

    def refresh_food(self):
        self.goto(random.randint(-275, 275), random.randint(-275, 275))
