import random

word_list = ["apple", "banana", "orange"]

def hang_man():
  chosen_word = random.choice(word_list)
  print(f"The chosen word is {chosen_word}.")
  
  display = []
  word_length = len(chosen_word)
  
  for _ in range(word_length):
    display += "_"
  print(display)
  
  end_of_game = False
  
  while not end_of_game:
  
    user_choice = input("Guess a letter. ").lower()
      
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == user_choice:
        display[position] = letter
        
    print(display)
    
    if "_" not in display:
      end_of_game = True
      print("Please try again!")
      break
  
hang_man()
    
    
      

  


