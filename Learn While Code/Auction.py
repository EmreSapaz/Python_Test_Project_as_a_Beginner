print("*****************************")
print("Welcome to Auction")
print("*****************************")

bidder = {}
while True:
    name: str = input("Your Name:")
    bid: int = int(input("Your Bid: $"))

    bidder.update({name: bid})
    other_bidder: str = input("Will there be any other bidder?\nYes or No?")

    if other_bidder.lower() != "yes":
        winner = max(bidder, key=bidder.get)
        print(f"Winner is {winner} with a bid of ${bidder[winner]}")
        break