# Import necessary modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create the screen object
screen = Screen()
screen.setup(width=600, height=600)  # Set the dimensions of the screen
screen.bgcolor("#2D2D2D")  # Set the background color of the screen
screen.title("Welcome to Snake Game")  # Set the title of the window
screen.tracer(0)  # Turn off animation updates (manual update)

# Create a snake object from the Snake class
snake = Snake()
food = Food()
scoreboard = Scoreboard()



# Listen for keyboard inputs
screen.listen()
screen.onkey(snake.up, "Up")  # Call snake.up when "Up" arrow key is pressed
screen.onkey(snake.down, "Down")  # Call snake.down when "Down" arrow key is pressed
screen.onkey(snake.left, "Left")  # Call snake.left when "Left" arrow key is pressed
screen.onkey(snake.right, "Right")  # Call snake.right when "Right" arrow key is pressed

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen with the latest changes
    time.sleep(0.08)  # Delay to control the speed of the game loop
    
    snake.move()  # Move the snake based on the current direction
    
    #Detect collision with food   
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        
        
        
    #Detect Collisiion with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
           
    
# Wait for a mouse click on the screen to exit, after the loop finishes
screen.exitonclick()