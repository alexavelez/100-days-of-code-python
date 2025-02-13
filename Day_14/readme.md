# Higher Lower Game

<img width="467" alt="higher" src="https://github.com/user-attachments/assets/6b4f9ff1-51c5-4b80-85dd-56a6ec1c734f" />



<br />
<br />
This is a Python implementation of the **Higher Lower Game** , a project from ** Day 14** of the **100 Days of Python** Udemy course. In this game, the player is presented with two famous individuals or organizations and must guess who has more followers on social media. The goal is to keep guessing correctly and achieve the highest score possible.

## How It Works
- The game randomly selects two characters from a dataset.
- The player is shown both options with their name, description, and country.
- The player must guess who has more followers by typing **'A'** or **'B'**.
- If the guess is correct, the score increases, and the game continues with a new comparison.
- If the guess is wrong, the game ends, and the final score is displayed.

## Features
- Displays a message when the user gets an answer correct: `You're right! Your score: X`.
- Prevents duplicate choices by keeping track of available characters.
- Handles invalid inputs and prompts the user to enter a valid choice.

## Installation & Usage
1. Clone this repository:
   
   ```sh
   git clone https://github.com/alexavelez/higher-lower-game.git
   ```
2. Navigate to the project directory:
   
   ```sh
   cd higher-lower-game
   ```
3. Run the game:
   
   ```sh
   python main.py
   ```
## Requirements

- Python 3.x

- art.py and data.py files should be included in the same directory.

## File Structure
```sh
├── art.py           # Contains ASCII art for the game
├── data.py          # Contains dataset of characters with follower counts
├── main.py          # Main game logic
├── README.md        # Project documentation
```
## Credits
This project is part of the 100 Days of Python course on Udemy (Day 14).

## License
This project is for educational purposes only. Feel free to modify and experiment with it!

   
