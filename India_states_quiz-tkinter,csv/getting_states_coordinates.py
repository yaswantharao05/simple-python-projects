import turtle

screen = turtle.Screen()
screen.title('India States Name')
screen.listen()

image = 'states2.gif'
screen.addshape(image)

turtle.shape(image)

state = 0
states_name = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana',
               'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
               'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
               'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal']


def get_mouse_click_coordinates(x, y):
    global state
    with open('states_name_x_y_cor', 'a') as file:
        file.write(f'{states_name[state]},{x},{y}\n')
    state += 1


turtle.onscreenclick(fun=get_mouse_click_coordinates)

screen.mainloop()
