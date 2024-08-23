import random

# Welcome message
print("Welcome to the Rock, Paper, Scissors game!")
print("Type 'end' to quit the game at any time.\n")

# Initialize scores
user_score = 0
cpu_score = 0

# List of possible choices
choices = ['rock', 'paper', 'scissors']

while True:
    # Get user's choice
    user_choice = input("Rock, Paper or Scissors? ").lower()

    # Check if the user wants to end the game
    if user_choice == 'end':
        break

    # Validate user's choice
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Get computer's choice
    cpu_choice = random.choice(choices)

    # Display choices
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {cpu_choice.capitalize()}\n")

    # Determine the winner
    if user_choice == cpu_choice:
        print("It's a tie!\n")
    elif (user_choice == 'rock' and cpu_choice == 'scissors') or \
         (user_choice == 'paper' and cpu_choice == 'rock') or \
         (user_choice == 'scissors' and cpu_choice == 'paper'):
        print(f"You win! {user_choice.capitalize()} beats {cpu_choice.capitalize()}\n")
        user_score += 1
    else:
        print(f"You lose. {cpu_choice.capitalize()} beats {user_choice.capitalize()}\n")
        cpu_score += 1

# Final Scores
print("Final Scores:")
print(f"CPU: {cpu_score}")
print(f"Player: {user_score}")
