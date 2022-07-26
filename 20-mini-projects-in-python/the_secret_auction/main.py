from replit import clear

from art import logo

print(logo)

print('Welcome to the secret auction program.')
bids = {}
continue_bidding = True


def highest_bidder(bidding_record):
    """
    Computes and displays the highest bidder

    Args:
        bidding_record (dictionary): contains name(key) and 
                                              bid_amount(value) for everyone
    """
    max_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of {max_bid}')


while continue_bidding:
    try:
        name = input('what is your name?: ').title()
        bid = int(float(input('what is your bid?: ')))
        bids[name] = bid
        should_continue = input('Are there any other bidders? Type "yes" or "no": ').lower()
        if should_continue == "no":
            continue_bidding = False
            highest_bidder(bids)
        elif should_continue == "yes":
            clear()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt not allowed")
    except Exception as ex:
        print(ex)
