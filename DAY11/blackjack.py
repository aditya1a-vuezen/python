import random
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user1_score, computer1_score):
    if user1_score == computer1_score:
        return "Draw 🙃"
    elif computer1_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user1_score == 0:
        return "Win with a Blackjack 😎"
    elif user1_score > 21:
        return "You went over. You lose 😭"
    elif computer1_score > 21:
        return "Opponent went over. You win 😁"
    elif user1_score > computer1_score:
        return "You win 😃"
    else:
        return "You lose 😤"



def play_game():
    print(logo)
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"your cards {user_card}, current score : {user_score}")
        print(f"computer first cards: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
           user_should_deal = input("type 'y' to get another card or type 'n' to stop")
           if user_should_deal == "y":
               user_card.append(deal_card())
           else:
               game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your Final Card : {user_card}, final score : {user_score}")
    print(f"Computer final Card : {computer_card}, final score : {computer_score}")
    print(compare(user_score, computer_score))


while input("type 'y' to continue or type 'n' to stop") == 'y':
    print("\n"*40)
    play_game()
