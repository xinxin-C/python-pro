import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="Name")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and not (answer_state in guessed_states):
        data_now = data[data.state == answer_state]
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.goto(int(data_now.x), int(data_now.y))
        text.write(answer_state)
        guessed_states.append(answer_state)

