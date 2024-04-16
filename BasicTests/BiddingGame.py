# Auction Bidding program

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    bidder = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            
    print(f"The winner is {bidder} with a bid of ${highest_bid}!")

while not bidding_finished:
    
    name = input("What is your name?:\n")
    price = int(input("How much is your bid?:\n$"))
    bids[name] = price
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    
    if continue_bid == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif continue_bid == "yes":
        continue