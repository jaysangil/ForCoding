# # hangman incomplete
# import random

# # list of words to be picked
# word_list = ["apple", "banana", "orange"]

# # ASCII Art for different stages of the hangman
# HANGMAN_PICS = [
#     """
#      +---+
#          |
#          |
#          |
#         ===""",
#     """
#      +---+
#      O   |
#          |
#          |
#         ===""",
#     """
#      +---+
#      O   |
#      |   |
#          |
#         ===""",
#     """
#      +---+
#      O   |
#     /|   |
#          |
#         ===""",
#     """
#      +---+
#      O   |
#     /|\\  |
#          |
#         ===""",
#     """
#      +---+
#      O   |
#     /|\\  |
#     /    |
#         ===""",
#     """
#      +---+
#      O   |
#     /|\\  |
#     / \\  |
#         ==="""
# ]


# # rungs the hangman function
# def hangman():
    
#     # picks a random word from the list
#     chosen_word = random.choice(word_list)
#     print(f"The chosen word is {chosen_word}")
    
#     word_length = len(chosen_word)
#     display = []
#     remaining_attempts = 6
    
#     for _ in range(word_length):
#         display += "_"
#     print(display)
    
#     end_game = False
    
#     while not end_game:
        
#         chosen_letter = input("Please choose a letter: ").lower()
        
#         for position in range(word_length):
#             letter = chosen_word[position]
#             if letter == chosen_letter:
#                 display[position] += letter
                
#         if chosen_letter not in chosen_word:
#             remaining_attempts -= 1
#             if remaining_attempts == 0:
#                 end_game = True
#                 print("You lose!")
                
#         print(display)
        
#         if "_" not in display:
#             end_game = True
#             print("Try again!")
#             break  
    
# hangman()


import random

# List of words to be picked
word_list = ["apple", "banana", "orange"]

# ASCII Art for different stages of the hangman
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

# Runs the hangman function
def hangman():
    chosen_word = random.choice(word_list)
    print("Welcome to Hangman!")

    word_length = len(chosen_word)
    display = ["_"] * word_length
    guessed_letters = set()
    remaining_attempts = 6

    while remaining_attempts > 0 and "_" in display:
        print(HANGMAN_PICS[-remaining_attempts])  # Display hangman stage
        print(f"Word: {' '.join(display)} | Remaining Attempts: {remaining_attempts}")
        chosen_letter = input("Please choose a letter: ").lower()

        if chosen_letter in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(chosen_letter)

        if chosen_letter in chosen_word:
            for position in range(word_length):
                if chosen_word[position] == chosen_letter:
                    display[position] = chosen_letter
        else:
            remaining_attempts -= 1
            print(f"Incorrect guess. You have {remaining_attempts} attempts left.")

    print(HANGMAN_PICS[-remaining_attempts])
    if remaining_attempts == 0:
        print(f"You lose! The word was {chosen_word}.")
    else:
        print(f"Congratulations! You guessed the word: {''.join(display)}")

hangman()

    
    