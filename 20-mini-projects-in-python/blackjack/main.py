import random

from replit import clear

from art import logo


def deal_card():
    """
    Returns a random card from the deck.\n
    Returns:
        int: a random card value
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Takes in a list of cards and returns the score calculated from the cards.
    Args:
        cards (list): List of user cards

    Returns:
        int: sum of user cards, 0 if blackjack
    """
    card_sum = sum(cards)
    if (card_sum == 21) and (len(cards) == 2):
        return 0
    if (11 in cards) and (card_sum > 21):
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """
    Compares user score and computer score

    Args:
        user_score (int): user's score
        computer_score (int): computer's score

    Returns:
        str: results of comparison
    """
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over, You lose 😭"
    elif computer_score > 21:
        return "Opponent went over, you win 😄"
    elif user_score > computer_score:
        return "You win 🙂"
    else:
        return "You lose 🤕"


def play_game():
    """
    Main logic of the game
    """
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'    Your cards: {user_cards}, current score: {user_score}')
        print(f'    Computer\'s first card: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    clear()
    play_game()
