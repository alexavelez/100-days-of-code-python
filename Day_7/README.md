# Day 7 - Hangman
This is a Python implementation of the classic Hangman game, where the player tries to guess a hidden word by suggesting letters one at a time.

## Features:
**Interactive Gameplay:** The user guesses letters, and with each wrong guess, a part of the hangman is drawn.
**Friendly Feedback:** Fun or encouraging messages appear when incorrect guesses are made, adding a lighthearted twist to the traditional game.
**Win/Loss Condition:** The game ends when the user either guesses the word correctly or runs out of guesses.

## Sources and Implementation:
**Word List:** The word list is a .txt file sourced from [this repository](https://github.com/Tom25/Hangman/blob/master/wordlist.txt). The strings were manipulated to remove the \n characters so that they could be imported and used as a Python list.
**ASCII Art:** The hangman ASCII art was sourced from ascii.co.uk.
**Starter Code:** The starting code was provided by the 100 Days of Code Python Udemy course.
**Additional Features:** Added error checking for user inputs, improving the game's overall functionality.

## How to Play:
Download all files in the same folder and run hangman.py with your code editor or python3. 
Start the game, and a random word will be chosen.
Guess one letter at a time by entering it into the prompt.
For each correct guess, the letter will be revealed in the word. For each wrong guess, you'll receive a playful message and lose a chance.
The game ends when you've either guessed the word or made too many wrong guesses.
Enjoy playing and feel free to modify the code or add new features!
