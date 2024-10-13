from art import logo
from os import system

print(logo)
print("Welcome to the secret auction program")

# Alternative solution using the max function instead of a loop
auction = {}
restart = True
max_bid = 0
max_bidder = ""   

while restart == True:
    name_bid = input("What is your name?\n")
    bid = int(input("What is your bid? \n $"))
    auction[name_bid] = bid
    another_bidder = input('Are there any other bidders? type "yes" or "no".\n').lower()
    max_bidder = max(auction, key=auction.get)
    max_bid = auction[max_bidder]
    if another_bidder == "no":
        restart = False
        print(f"The winner of the bid is {max_bidder} with a bid of {max_bid}")
    else:
        system("clear")

# Solution provided by the instructional video
# bids = {}
# continue_bidding = True

# def max_bid_finder(auction_dic):
#     highest_bid = 0
#     winner = 0
#     for bidder in auction_dic:
#         bid_amount = auction_dic[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner of the bid is {winner} with a bid of {highest_bid}")

# while continue_bidding:
#     name = input("What is your name?")
#     price = int(input("What is your bid?"))
#     bids[name] = price
#     should_continue = input('Are there any other bidders? type "yes" or "no".\n').lower()
#     if should_continue == "no":
#         continue_bidding = False
#         max_bid_finder(bids)
#     else:
#         system("clear")