## Blackjack Game

This project is part of the 100 Days of Python Udemy course challenge for Day 11. The goal was to build a simplified version of the card game Blackjack, where a player competes against the computer. This challenge allowed me to practice coding fundamentals, focusing on logical flow, function creation, and understanding variable scope within functions.

### Game Description
In this Blackjack game, the player competes against a computer dealer. The goal is to have a hand as close to 21 as possible without going over, with face cards (Jack, Queen, King) worth 10 points and an Ace worth either 11 or 1, depending on the player's total score.

### Requirements (given by the instructor):

#### Initial Deal: 
Both the player and computer receive two random cards.

#### Blackjack Detection:
If the computer gets a Blackjack (an Ace and a 10-value card), the player loses immediately, even if the player also has a Blackjack.
If the player gets a Blackjack, they win instantly (unless the computer also has a Blackjack, in which case it's a tie).
#### Score Calculation:
If an Ace is drawn, it counts as 11 unless this would make the score exceed 21, in which case it counts as 1.
#### Gameplay Flow:
The computer’s first card is revealed to the player.
The game ends immediately if the player’s score goes over 21 or if either the player or the computer has a Blackjack.
If the game continues, the player decides whether to "hit" (draw another card) or "stand" (keep their current hand).
#### Computer’s Turn:
Once the player stands, the computer continues to draw cards until its score reaches 17 or higher.
#### Game Outcome:
Scores are compared, with the closest to 21 without exceeding it winning the game. The final hands and scores of both player and computer are displayed.

### Concepts Practiced

**Function Creation:** Divided game logic into functions like deal_card(), calculate_score(), and compare_score() to improve readability and organization.

**Variable Scope:** Managed variable scope by carefully defining where variables like hands and scores are created and updated.

**Logical Flow:** Implemented conditionals to handle various game outcomes, such as detecting Blackjacks and adjusting Ace values dynamically based on the player’s score.

**Loop Control:** Used while loops for gameplay, including letting the player decide whether to draw additional cards and managing the computer’s actions automatically after the player’s turn.

**User Input:** Allowed player choices for drawing more cards or ending the game, with feedback on current scores and options to continue.

**Additional Features:** The game asks if the player would like to play again after each round and clears the console if they choose to continue.
