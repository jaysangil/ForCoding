# test H and L game

import random

def high_low():
  
  current_number = random.randint(1, 100)
  score = 0
  
  
  while True:
    
    print(f"The current number is {current_number}")
    guess = input("Will the next number be higher or lower? Please enter 'h' for higher and 'l' for lower. ").lower()
    
    next_number = random.randint(1, 100)
    
    if guess not in ['h', 'l']:
      print("Please enter a valid option! ")
      continue
    
    if (guess == 'h' and next_number > current_number) or (guess == 'l' and next_number < current_number):
      
      print("You got it right!")
      score += 1
      
    else: 
      print("try again!")
      break
    
    current_number = next_number
    
  print(f"Your score is {score}")
  
high_low()
      
      
  

  
