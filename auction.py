
from art import logo
print(logo)

auction_dictionary = {}



def user_input():
  name = input("What is your name?: ")
  bid = int(input("How much do you want to bid?: $"))
  auction_dictionary[name] = bid
  additional_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if additional_bids == "yes":
    user_input()


user_input()

x = 0
for highest_bid in auction_dictionary:
  y = auction_dictionary[highest_bid]
  if y > x:
    x = y
    winner = highest_bid
print(f"The winner is {winner} with a bid of ${x}")


  












