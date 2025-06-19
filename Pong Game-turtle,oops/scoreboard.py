from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.refresh_scores()

    def refresh_scores(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, font=('Courier', 80, 'normal'), align='center')
        self.goto(100, 200)
        self.write(self.r_score, font=('Courier', 80, 'normal'), align='center')



