import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    def test_check_for_ace__True(self):
        test_card = Card("Spades", 1)
        self.assertEqual(True, CardGame.checkforAce(self, test_card))

    def test_check_for_ace__False(self):
        test_card = Card("Spades", 8)
        self.assertEqual(False, CardGame.checkforAce(self, test_card))

    def test_highest_card__card1(self):
        test_card_1 = Card("Hearts", 7)
        test_card_2 = Card("Clubs", 3)
        self.assertEqual(7, CardGame.highest_card(self, test_card_1, test_card_2).value)

    def test_highest_card__card2(self):
        test_card_1 = Card("Hearts", 4)
        test_card_2 = Card("Clubs", 9)
        self.assertEqual(9, CardGame.highest_card(self, test_card_1, test_card_2).value)

    def test_cards_total(self):
        test_card_1 = Card("Hearts", 4)
        test_card_2 = Card("Clubs", 9)
        test_card_3 = Card("Hearts", 7)
        test_card_4 = Card("Clubs", 3)
        cards = [test_card_1, test_card_2, test_card_3, test_card_4]
        self.assertEqual("You have a total of 4", CardGame.cards_total(cards))