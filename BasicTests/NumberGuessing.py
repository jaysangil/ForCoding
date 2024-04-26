import random

def guess_the_number():
    # Set the range for the random number
    min_value = 1
    max_value = 100
    
    # Generate a random number between min_value and max_value
    random_number = random.randint(min_value, max_value)
    
    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between {min_value} and {max_value}. You have 10 attempts to guess it.")
    
    # Keep track of the number of attempts
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        # Get user input
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        attempts += 1
        
        # Check if the guess is correct
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
    else:
        # If the loop completes without breaking, the user has exhausted their attempts
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {random_number}.")

# Run the game
guess_the_number()
