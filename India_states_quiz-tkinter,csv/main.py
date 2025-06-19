import turtle
import pandas

screen = turtle.Screen()
screen.title('India States Name')

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

image = 'states2.gif'

screen.addshape(image)

turtle.shape(image)

# Once created not required to create again
# states_df = pandas.read_csv('states_name_x_y_cor')
# states_df.to_csv('states_Name_x_y.csv')

states_data = pandas.read_csv('states_Name_x_y.csv')

states_name = states_data['state'].to_list()

states_found = 0

while states_found < 28:
    state_guessed = screen.textinput(title=f'{states_found}/28 States Correct. Guess the State.',
                                     prompt="What's another state name?").title()
    if state_guessed == 'Exit':
        break

    if state_guessed in states_name:
        states_found += 1
        states_name.remove(state_guessed)
        state_x_y = states_data[states_data.state == state_guessed]
        state_x_cor, state_y_cor = int(state_x_y.x), int(state_x_y.y)
        writer.goto(state_x_cor, state_y_cor)
        writer.write(arg=state_guessed, font=('Courier', 8, 'normal'), align='center')

states_name_df = pandas.DataFrame(states_name)
states_name_df.to_csv('Missed_States_Name.csv')
