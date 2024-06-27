import turtle
IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)

def get_mouse_click_coor(x, y):
  print(x, y)
  

turtle.onscreenclick(get_mouse_click_coor)


turtle.mainloop()



screen.exitonclick()