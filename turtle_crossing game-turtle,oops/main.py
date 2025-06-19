import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)
screen.listen()


turtle = Player()
screen.onkeypress(key='Up', fun=turtle.move_up)
screen.onkeypress(key='Down', fun=turtle.move_down)

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
run_time = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if car_manager.check_car_collision(turtle):
        game_is_on = False
        scoreboard.game_over()

    if run_time % 4 == 0:
        car_manager.create_a_car()

    if turtle.at_finish_line():
        car_manager.move_distance += car_manager.move_increment
        car_manager.new_level()
        turtle.refresh_turtle_pos()
        scoreboard.update_score()

    car_manager.move_cars()

    run_time += 1

screen.exitonclick()
