from turtle import Screen
import time
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
r_paddle.divider()
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(key='Up', fun=r_paddle.move_up)
screen.onkeypress(key='Down', fun=r_paddle.move_down)
screen.onkeypress(key='w', fun=l_paddle.move_up)
screen.onkeypress(key='s', fun=l_paddle.move_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when R paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.refresh_scores()
        screen.update()
        time.sleep(1)

    # Detect when L paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.refresh_scores()
        screen.update()
        time.sleep(1)


screen.exitonclick()
