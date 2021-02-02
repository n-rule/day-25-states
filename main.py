import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title('U.S. States - Game')

image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
guessed_states = []
states_to_learn = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                    prompt='What is another state name is?').title()

    if answer_state == 'Exit':
        break

    if answer_state in data.state.values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_row = data[data.state == answer_state]
        # tuple_coordinates = (state_row.x.values[0], state_row.y.values[0])
        # Both variants works fine
        tuple_coordinates = (int(state_row.x), int(state_row.y))
        new_state = State(answer_state, tuple_coordinates)


for state in data.state.values:
    if state not in guessed_states:
        states_to_learn.append(state)


states_to_learn = pandas.DataFrame(states_to_learn)
print(states_to_learn)
states_to_learn.to_csv('states_to_learn')




