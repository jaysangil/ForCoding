import turtle
import pandas

# Path to the image of the blank U.S. states map
IMAGE = "blank_states_img.gif"

# Set up the screen
screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(IMAGE)  # Add the image shape
turtle.shape(IMAGE)  # Set the turtle shape to the image

# Read the data from the CSV file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()  # Create a list of all state names
guessed_state = []  # List to keep track of guessed states

# Main game loop
while len(guessed_state) < 50:
    # Get the user's guess and capitalize the first letter of each word
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States correct", 
                                    prompt="What's another state's name?").title()
    print(answer_state)

    # Check if the user wants to exit the game
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]  # List of states not yet guessed
        new_data = pandas.DataFrame(missing_states)  # Create a DataFrame from the missing states
        print(missing_states)  # Print the missing states
        break  # Exit the loop

    # Check if the guessed state is in the list of all states
    if answer_state in all_states:
        guessed_state.append(answer_state)  # Add the guessed state to the list
        t = turtle.Turtle()
        t.hideturtle()  # Hide the turtle cursor
        t.penup()  # Lift the pen so it doesn't draw lines
        state_data = data[data.state == answer_state]  # Get the row of data for the guessed state
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))  # Move the turtle to the state's coordinates
        t.write(state_data.state.iloc[0])  # Write the state's name at its location

# Exit the screen on click
screen.exitonclick()
