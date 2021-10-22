import turtle
import pandas as pd
turtle.Screen()
screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

with open("50_states.csv") as states_file:
    data = pd.read_csv(states_file)
    states_data = data['state'].to_list()

score = 0
guessed_answers = []
user_guess_counts = 0
while len(guessed_answers) < 50:

    user_guess = screen.textinput(f" Score {score}/{len(states_data)} - {user_guess_counts} - US_states_guess_game", "Guess US state or type exit to learn").title()
    user_guess_counts += 1
    if user_guess in guessed_answers:
        turtle.textinput("State already guessed!", "Type OK to continue")
    else:
        if user_guess in states_data:
            guessed_answers.append(user_guess)
            new_state = data[data.state == user_guess]
            tim = turtle.Turtle()
            tim.penup()
            tim.hideturtle()
            tim.goto(int(new_state.x), int(new_state.y))
            tim.write(user_guess)
            score += 1

        elif user_guess == "Exit":
            tim = turtle.Turtle()
            tim.penup()
            tim.hideturtle()
            for x in states_data:
                if x not in guessed_answers:
                    new_data = states_data
                    # shorter code for above three lines
            # new_data = [x for x in states_data if x not in guessed_answers]
                    for n in new_data:
                        new_data_states = data[data.state == n]
                        tim.goto(int(new_data_states.x), int(new_data_states.y))
                        tim.write(n)
                    tim.goto(0,250)
                    tim.write("All states are updated", align="center", font=("Arial", 50, "normal"))

            if score == len(states_data):
                print("You have guessed all the states!")
                game_on = False

turtle.mainloop()









