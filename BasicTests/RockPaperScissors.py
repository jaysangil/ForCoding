import random

# Function to play Rock, Paper, Scissors
def play_rps():
    # Score initialization
    player_score = 0
    computer_score = 0

    # Options
    options = ["Rock", "Paper", "Scissors"]

    # Game Loop
    while True:
        # Player's choice
        player_choice = input("Choose Rock, Paper, or Scissors (or 'Exit' to end the game): ").capitalize()
        if player_choice == "Exit":
            break

        if player_choice not in options:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        # Computer's choice
        computer_choice = random.choice(options)
        print(f"Computer chose {computer_choice}")

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        # Display scores
        print(f"Score: Player {player_score}, Computer {computer_score}\n")

    # Final score
    print("Game over!")
    print(f"Final Score: Player {player_score}, Computer {computer_score}")

# Run the game
play_rps()
