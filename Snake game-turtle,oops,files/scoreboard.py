from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.score = 0
        with open('HighScore.txt', 'r') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.goto(0, 300)
        self.score_refresh()

    def score_refresh(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    # def game_over(self, reason):
    #     self.goto(0, 0)
    #     self.color('red')
    #     space = " "
    #     self.write(arg=space*5+f"GAME OVER \n {reason}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('HighScore.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.score_refresh()
