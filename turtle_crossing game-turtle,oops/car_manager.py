from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT

    def create_a_car(self):
        car = Turtle()
        car.penup()
        car.shape('square')
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(300, random.randint(-240, 240))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def new_level(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()

    def check_car_collision(self, turtle):
        for car in self.cars:
            if car.distance(turtle) <= 25 and turtle.ycor() <= car.ycor():
                return True
