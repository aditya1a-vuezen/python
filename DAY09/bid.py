mport art

print(art.logo)

def find_highest_bidder(biddict):
    winner = ""
    for  bidder in biddict:
        bid_amount = biddict[bidder]
        if bid_amount > biddict[bidder]:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")




bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?:")
    price = int(input("What is your bid?:$"))
    bids[name] = price
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif other == "yes":
        print("\n" * 20)






