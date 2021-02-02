import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title('U.S. States - Game')

image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
correct_number = 0

while True:

    answer_state = screen.textinput(title=f'{correct_number}/50 States Correct', prompt='What is another state name is?').title()

    if answer_state in data.state.values:
        correct_number += 1

        state_row = data[data.state == answer_state]
        tuple_coordinates = (state_row.x.values[0], state_row.y.values[0])

        new_state = State(answer_state, tuple_coordinates)







screen.exitonclick()