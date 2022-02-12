import json
import itertools
import random

HAND_SIZE = 5


def fill_hand(hand, deck):
    while len(hand) < HAND_SIZE:
        card = pick_card(deck)
        hand.append(card)
    return hand


def pick_card(deck):
    picked_number = random.randint(0, len(deck))
    card = deck.pop(picked_number)
    return card


def print_hand(hand):
    print("Your hand is: ")
    card_num = 1
    for card in hand:
        print(str(card_num) + ". " + card)
        card_num = card_num + 1


if __name__ == '__main__':
    hand = []

    # Opening JSON file
    f = open('cah-cards-full.json', encoding='utf8')

    # returns JSON object as
    # a dictionary
    game_packs = json.load(f)

    # Closing file
    f.close()

    white_cards = list(itertools.chain(*[pack['white'] for pack in game_packs]))
    white_cards = [x['text'] for x in white_cards]

    black_cards = list(itertools.chain(*[pack['black'] for pack in game_packs]))

    hand = fill_hand(hand, white_cards)
    # print_hand(hand)

    # black_card = pick_card(black_cards)

    card_chosen = 0
    while card_chosen != 999:
        black_card = pick_card(black_cards)
        print("Black card chosen: " + black_card['text'])
        print_hand(hand)
        card_chosen = int(input("Pick a card (1111 to skip this card, 999 to exit): "))
        if card_chosen == 1111 or card_chosen == 999:
            continue
        else:
            print("The created sentence is: ")
            print(black_card['text'].replace('_', hand[card_chosen - 1]))
            hand.pop(card_chosen - 1)
            hand = fill_hand(hand, white_cards)