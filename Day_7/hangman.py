import random
from hangman_art import hangman, encouraging_messages, correct_guess_messages

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)

#1. Creating the word directory to choose random words
# Source: https://github.com/Tom25/Hangman/blob/master/wordlist.txt
with open("/Users/alexandravelez/Desktop/python/py100days/wordlist.txt", "r") as words_directory:
	word_list = words_directory.readlines()
	
# This is a .txt list where every word is in a different line separated by ",\n", so it needs to be removed
# in order to have a list of words separated by ,

# initialize character
char = "\n"
 
# Remove character \n from Strings list using loop + replace() + enumerate()
for idx, ele in enumerate(word_list):
    word_list[idx] = ele.replace(char, "")

#2. Choosing a random word and showing the user the length of the word
chosen_word = random.choice(word_list)
lenght_chosen_word = len(chosen_word)

placeholder = "_" * lenght_chosen_word
print(f"The word to guess is: {placeholder}")

#3 Functionality variables
game_over = False
correct_letters = []
previous_guess = []
lives = 6

#4 Asking user to guess a letter
while not game_over and lives > 0:
    guess = input("Guess a letter:\n").lower()
#5 Checking it is a valid input
    if not guess.isalpha() or len(guess) >1:
        print("Invalid input. Please type one letter.")
    else:
#6 If letter was guessed before in the game
        if guess in previous_guess:
            print(f"You've already guessed {guess}.")
            print(display)
    #If correct
        else:
            display = ""
            for letter in chosen_word:
                    if letter == guess:
                         display +=guess
                         correct_letters.append(guess)
                    elif letter in correct_letters:
                         display += letter
                    else:
                         display += "_"

            print(random.choice(correct_guess_messages))
            print(display)
    #If not correct
            if guess not in chosen_word:
                lives -=1
                print(random.choice(encouraging_messages))
                print(f"The letter {guess} is not in the word.\n")
                print(f"******************* Lives remaining: {lives}/6 *******************\n")
                if lives ==0:
                    print(f"The word was {chosen_word}\n")
                    print("************************ Game over! ************************")

            previous_guess.append(guess)
            print(hangman[lives])

            if "_" not in display:
                     game_over = True
                     print("***********************You win!***********************")
