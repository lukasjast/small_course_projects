bidders_list = {}

def new_bidder(bidder_name, bid_amount, bidder_age):
    bidder_info = {
        "bid": bid_amount,
        "age": bidder_age,
    }
    bidders_list[bidder_name] = bidder_info

def find_winner(bidders):
    highest_bid = 0
    winner = None
    for bidder, info in bidders.items():
        if info["bid"] > highest_bid:
            highest_bid = info["bid"]
            winner = bidder
    print(f"The winner is {winner}.")

players_amount = int(input("Welcome to the secret auction program. \nHow many players are you expecting ? "))

for i in range(players_amount):
    name = input(f"What's the name of the player {i+1}? ")
    age = int(input(f"How old is the player {i+1}? "))
    bid = int(input(f"What's his bid "))
    new_bidder(name, bid, age)

find_winner(bidders_list)
