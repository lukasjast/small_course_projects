bidders_list = {}

def new_bidder(bidder_name, bid_amount, bidder_age):
    bidder_info = {
        "bid": bid_amount,
        "age": bidder_age,
    }
    bidders_list[bidder_name] = bidder_info

new_bidder("John", 100, 19)

print(bidders_list)