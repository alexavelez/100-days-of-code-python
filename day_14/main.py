import random
import art
from data import data

# Initialize score and game control variables
score = 0
to_continue = True

# Select two random characters from data
characters = random.sample(data, 2)
available_characters = data[:]  # Copy the original list
for char in characters:
    available_characters.remove(char)

random.shuffle(available_characters)  # Shuffle characters for efficiency

# Function to print comparison
def print_comparison():
    print(f"Compare A: {characters[0]['name']}, a {characters[0]['description']}, from {characters[0]['country']}.")
    print(f"{art.vs} \nAgainst B: {characters[1]['name']}, a {characters[1]['description']}, from {characters[1]['country']}.")

# Function to check user's answer
def check_answer(answer, followers_a, followers_b, score, to_continue):
    if answer == 'a' and followers_a > followers_b:
        score += 1 
        del characters[1]  # Remove the losing character
        print(f"{art.logo} \nYou're right! Your score: {score}")
    elif answer == 'b' and followers_b > followers_a:
        score += 1 
        del characters[0]  # Remove the losing character
        print(f"{art.logo} \nYou're right! Your score: {score}")
    else:
        to_continue = False  # Stop the game if the user is wrong
        print(f"{art.logo} \nSorry, that's wrong. Game over. Final score: {score}")
    
    if len(available_characters) == 0:
        to_continue = False
        print(f"{art.logo} \nYou win. Game over")
    
    return score, to_continue

print(f"{art.logo}")
# Game loop
while to_continue:
    print_comparison()

    # Get follower counts
    followers_a = characters[0]["follower_count"]
    followers_b = characters[1]["follower_count"]

    # Get user input
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    while answer not in ['a', 'b']:
        print(f"{art.logo} \nWrong input. Please type 'A' or 'B'.")
        print_comparison()
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if the answer is correct
    score, to_continue = check_answer(answer, followers_a, followers_b, score, to_continue)

    # If the game is still on, replace the eliminated character
    if to_continue and available_characters:
        new_chosen_character = available_characters.pop()
        characters.append(new_chosen_character)
