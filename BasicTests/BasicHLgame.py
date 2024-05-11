# test H or L game

import random

def high_low():
  
  current_number = random.randint(1, 100)
  score = 0
  
  
  while True:
    
    print(f"The current number is {current_number}. ")
    guess = (input("Will the next number be higher or lower? Please enter 'h' if higher and 'l' if lower. ")).lower()
    
    if guess not in['h', 'l']:
      print("Please enter a valid value! ")
      continue
      
    
    next_number = random.randint(1, 100)
    
    if (guess == 'h' and next_number > current_number) or (guess == 'l' and next_number < current_number):
      print("You are correct!")
      score += 1 
      
    else:
      print("You are wrong!")
      break
      
    current_number = next_number
      
  print(f"Your total score is {score}")
    
high_low()

    
      
    
    
    
    
  