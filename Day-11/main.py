import random
from art import logo
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare_score(player_score, computer_score, player_hand, computer_hand):
    if player_score > 21:
        print(f"You are busted! Your final hand: {player_hand}, your final score: {player_score}")
    elif computer_score > 21:
        print(f"Computer went over. You win! Your final hand: {player_hand}, Computer's final hand: {computer_hand}, computer final score: {computer_score}")
    elif computer_score == player_score:
        print(f"It's a tie! Your final hand: {player_hand}, Computer's final hand: {computer_hand}, final score: {computer_score}")
    elif player_score == 21:
        print(f"You win!\n Your final hand: {player_hand}.\n Computer's hand: {computer_hand}, computer's score: {computer_score}")
    elif computer_score == 21:
        print(f"Computer wins!\n Computer's final hand: {computer_hand}")
    elif player_score > computer_score:
        print(f"You win! Your final hand: {player_hand}, Computer's final hand: {computer_hand}")
    else:
        print(f"Computer wins! Your final hand: {player_hand}, Computer's final hand: {computer_hand}")

def play_game():
    print(logo)
    player_hand = []
    computer_hand = []
    continue_game = True
    player_turn = True

    # Deal initial two cards
    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())
    
    # Calculate initial scores after dealing two cards
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    # Check for initial blackjack
    if computer_score == 0:
        continue_game = False
        print(f"Computer has Blackjack! You lose. Computer's final hand: {computer_hand}")
    elif player_score == 0:
        continue_game = False
        print(f"You have Blackjack! You win! Your final hand: {player_hand}")
    else:
        # Game continues if no one has blackjack initially
        while continue_game:
            if player_turn:
                print(f"   Your cards: {player_hand}, your current score: {player_score}")
                print(f"   Computer's first card: {computer_hand[0]}")

                # Check if the player wants to draw another card
                draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if draw_another_card == "y":
                    player_hand.append(deal_card())
                    player_score = calculate_score(player_hand)
                    if player_score >= 21:
                        player_turn = False
                else:
                    player_turn = False
            else:
                # Computer's turn to draw if needed
                while computer_score != 0 and computer_score < 17:
                    computer_hand.append(deal_card())
                    computer_score = calculate_score(computer_hand)
                
                # Exit the main game loop after the computer's turn is complete
                continue_game = False

        # Compare scores after both turns are complete
        compare_score(player_score, computer_score, player_hand, computer_hand)

play_game()

while input("Do you want to play another round of Blackjack? Type 'y' or 'n': ") == "y":
  os.system("clear")
  play_game()
