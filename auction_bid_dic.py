from turtle import clear

auction_bidders = {}


def find_max_value():
    values = []
    for bidder in auction_bidders:
        values.append(auction_bidders[bidder])
        values = list(map(int, values))  # now values is a list of integers
    max_value = max(values)
    # keys here in this list key_list_auction_bidders are stored in the same index as the values in values list
    key_list_auction_bidders = list(auction_bidders.keys())

    # find the index of max_value in values list `values.index(max_value)`
    # then highest bidder's name is at the same index in
    # `key_list_auction_bidders list[same index as max_value in values list]`
    print(f"The winner is {key_list_auction_bidders[values.index(max_value)]} with bid of {max_value}")


def add_to_auction_bidders():
    bidder_name = input("What is your name ? \n")
    bid_amt = int(input("What's your bid in $ ? \n").replace("$", ""))
    auction_bidders[bidder_name] = f"{bid_amt}"
    additional_bidders = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if additional_bidders == 'yes':
        add_to_auction_bidders()

    elif additional_bidders == 'no':
        return find_max_value()


add_to_auction_bidders()

# print(auction_bidders)
