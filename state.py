from turtle import Turtle


class State(Turtle):
    def __init__(self, state_name, tuple_coord):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(tuple_coord)
        self.write(f'{state_name}', False, align='center', font=("Courier", 10, "bold"))
