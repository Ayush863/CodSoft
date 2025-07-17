import random

def get_user_choice():
    print("\nChoose one: Rock, Paper, or Scissors")
    user_input = input("Your choice: ").strip().lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please choose Rock, Paper, or Scissors.")
        user_input = input("Your choice: ").strip().lower()
    return user_input

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user, computer, result):
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")

    if result == "tie":
        print("Result: It's a tie!")
    elif result == "user":
        print("Result: You win!")
    else:
        print("Result: You lose!")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("=== Welcome to Rock, Paper, Scissors Game ===")

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, result)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"\nScore => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

        round_number += 1

# Run the game
play_game()