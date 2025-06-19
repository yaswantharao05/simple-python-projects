from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = 'left'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(-280, 260)
        self.write(f'Level: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER!! Your Score: {self.score*10}', move=False, align='center', font=FONT)
