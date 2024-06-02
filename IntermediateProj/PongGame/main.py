from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=700)
screen.title("Pong Game")
screen.tracer(0)


l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)

def go_up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)
    
def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

is_game_on = True
while is_game_on:
  screen.update()


screen.exitonclick()

