# Колода карт

import random

class Card:
    number_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __repr__(self):
        figure_cards = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
        if self.number is None:
            return self.mast
        number = figure_cards.get(self.number, self.number)
        return f'{self.mast} {number}'

class CardsDeck:
    def __init__(self):
        self.cards = [Card(number, mast) for mast in Card.mast_list\
                      for number in Card.number_list]
        self.cards.append(Card(None, 'Joker'))
        self.cards.append(Card(None, 'Joker'))

    def shuffle(self):
        random.shuffle(self.cards)

    def get(self, card_number):
        if 1 <= card_number <= 54:
            return self.cards[card_number - 1]
        else:
            print("Wrong card number. There are 54 cards in the deck")
        return False


deck = CardsDeck()
deck.shuffle()

card_number = int(input('Choose your card number (1-54): '))
card = deck.get(card_number)
print(f'Your card is: {card}')

card_number = int(input('Choose your card number (1-54): '))
card = deck.get(card_number)
print(f'Your card is: {card}')
