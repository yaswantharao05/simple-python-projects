from turtle import Screen, Turtle

screen = Screen()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.timmy = Turtle()
        self.timmy.speed(0)
        self.timmy.hideturtle()
        self.turtles = []
        self.turtles_positions = []
        self.head = Turtle()

    def create_snake(self):
        for i in range(3):
            self.add_turtle(x=-20 * i, y=0)
        self.head = self.turtles[0]

    def add_turtle(self, x, y):
        turtle = Turtle('square')
        turtle.penup()
        turtle.color('white')
        turtle.goto(x, y)
        self.turtles.append(turtle)

    def remove_snake(self):
        for turtle in self.turtles:
            turtle.hideturtle()
        self.turtles.clear()
        self.create_snake()

    def extend(self):
        self.add_turtle(x=self.turtles[-1].xcor(), y=self.turtles[-1].ycor())

    def move(self):
        self.turtles_positions = []
        for num in range(len(self.turtles) - 1, 0, -1):
            new_x, new_y = self.turtles[num - 1].xcor(), self.turtles[num - 1].ycor()
            self.turtles_positions.append((new_x, new_y))
            self.turtles[num].goto(new_x, new_y)
        self.head.forward(20)

    def snake_tail_collision(self):
        if (self.head.xcor(), self.head.ycor()) in self.turtles_positions:
            return True

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def boundary(self):
        self.timmy.penup()
        self.timmy.color('yellow')
        self.timmy.pensize(2)
        self.timmy.goto(-300, 300)
        self.timmy.pendown()
        self.timmy.goto(300, 300)
        self.timmy.goto(300, -300)
        self.timmy.goto(-300, -300)
        self.timmy.goto(-300, 300)
