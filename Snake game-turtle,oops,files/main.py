from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=620, height=670)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()


snake = Snake()
snake.boundary()
snake.create_snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='c', fun=screen.bye)

game_is_on = True


def game_over():
    # game_is_on = False
    snake.remove_snake()
    scoreboard.reset_score()
    screen.update()
    time.sleep(2)


while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh_food()
        scoreboard.score += 1
        scoreboard.score_refresh()
        snake.extend()

    if snake.snake_tail_collision():
        # scoreboard.game_over("SNAKE HIT TAIL")
        game_over()

    elif snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # scoreboard.game_over("SNAKE HIT WITH WALL")
        game_over()


screen.exitonclick()
