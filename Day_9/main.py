from art import logo
from os import system

print(logo)
print("Welcome to the secret auction program")

bids = {}
continue_bidding = True
# Declaring a function to find the highes bid, I'll use a list to store the previous highest bid instead of a single value, in case there are multiple bids with the same price
def max_bid_finder(auction_dic):
    highest_bid = [0]
    winner = [0]
    for bidder in auction_dic:
        bid_amount = auction_dic[bidder]
        if bid_amount > highest_bid[-1]:
            highest_bid[-1] = bid_amount
            winner[-1] = bidder
        elif bid_amount == highest_bid[-1]:
            highest_bid.append(bid_amount)
            winner.append(bidder)
    delimiter = ', '
    auc_winners = delimiter.join(winner)
    if len(winner) == 1:
        print(f"The winner of the auction is {auc_winners} with a bid of {highest_bid}")
    elif len(winner) >1:
        print(f"Tie! The winners of the auction are {auc_winners} with a bid of {highest_bid[-1]}")

while continue_bidding:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n$"))
    bids[name] = price
    should_continue = input('Are there any other bidders? type "yes" or "no".\n').lower()
    if should_continue == "no":
        continue_bidding = False
        max_bid_finder(bids)
    else:
        system("clear")