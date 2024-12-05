import random
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def get_attempts(difficulty):
    """Returns the number of attempts based on difficulty."""
    if difficulty == 'h':
        return HARD_ATTEMPTS
    elif difficulty == 'e':
        return EASY_ATTEMPTS
    else:
        return None

def get_guess():
    """Prompts the user for a guess and validates it."""
    while True:
        guess = input("Make a guess (1-100): ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        else:
            print("Invalid input. Please enter a valid number.")

def play_game():
    """Main game logic."""
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number from 1 to 100.")
    
    number = random.randint(1, 100)
    difficulty = input('Choose difficulty: type "e" for easy or "h" for hard: ').lower()
    remaining_attempts = get_attempts(difficulty)
    
    if remaining_attempts is None:
        print("Invalid difficulty selected. Starting in easy mode.")
        remaining_attempts = EASY_ATTEMPTS
    
    while remaining_attempts > 0:
        print(f"You have {remaining_attempts} attempts remaining.")
        guess = get_guess()
        
        if guess == number:
            print(f"You win! The number was {number}.")
            break
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
        
        remaining_attempts -= 1
        
        if remaining_attempts == 0:
            print(f"You lose! The number was {number}.")
        else:
            print("Guess again!")

def main():
    """Runs the game loop."""
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye!")
            break

main()