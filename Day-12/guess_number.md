# Number Guessing Game

## 📋 Description
The **Number Guessing Game** is a simple interactive Python program where players try to guess a randomly generated number between 1 and 100. The game offers two difficulty levels—easy and hard—which determine the number of attempts players have to guess the correct number. It provides feedback on each guess ("Too high" or "Too low") to guide players toward the correct answer.

## 🚀 How It Works
1. **Difficulty Selection**: Players choose between "Easy" (10 attempts) and "Hard" (5 attempts).
2. **Random Number Generation**: The program generates a random number between 1 and 100.
3. **Gameplay**:
   - Players input guesses and receive feedback on whether their guess is too high, too low, or correct.
   - The game tracks the number of remaining attempts and ends when:
     - The player guesses the correct number (win).
     - The player runs out of attempts (lose).
4. **Replay Option**: After a game ends, players can choose to play again or exit.

## 🛠️ Skills and Concepts Demonstrated
### 1. **Functions**:
   - Modularized logic into reusable functions, such as:
     - `get_attempts()` for determining attempts based on difficulty.
     - `get_guess()` for handling user input and validation.
     - `play_game()` for the main game logic.
     - `main()` for the overall program loop.

### 2. **Control Flow**:
   - **Loops**: Used a `while` loop to handle multiple guesses during a game session.
   - **Conditionals**: Validated user inputs and provided game feedback (e.g., too high, too low).
   - **`break` Statement**: Exited the loop immediately when the player guessed correctly.

### 3. **Error Handling and user input validation**:
   - Managed invalid inputs, ensuring the game only accepted integers within the valid range.

### 4. **Random Number Generation**:
   - Used Python's `random.randint()` to generate a number between 1 and 100.
