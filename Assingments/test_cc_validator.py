import unittest

from Assingments.card_validator import card_type, length_of_card_number, even_double_digits, odd_digits


class TestCardValidity(unittest.TestCase):
    def test_card_type(self):
        self.assertEqual(card_type("4111111111111111"), "visa")
        self.assertEqual(card_type("5555555555554444"), "MasterCard")
        self.assertEqual(card_type("371449635398431"), "AmericanExpress")
        self.assertEqual(card_type("6011111111111117"), "DiscoveryCard")
        self.assertEqual(card_type("1234567890"), "card is unknown")

    def test_length_of_card_number(self):
        self.assertEqual(length_of_card_number("4111111111111111"), 16)
        self.assertEqual(length_of_card_number("5555555555"), 10)
        self.assertEqual(length_of_card_number("371449635398431"), 15)
        self.assertEqual(length_of_card_number("60111111111111"), "card length is invalid")

    def test_even_double_digits(self):
        self.assertEqual(even_double_digits("4111111111111111"), 28)
        self.assertEqual(even_double_digits("5555555555554444"), 40)
        self.assertEqual(even_double_digits("371449635398431"), 20)
        self.assertEqual(even_double_digits("6011111111111117"), 30)

    def test_odd_digits(self):
        self.assertEqual(odd_digits("4111111111111111"), 14)
        self.assertEqual(odd_digits("5555555555554444"), 20)
        self.assertEqual(odd_digits("371449635398431"), 15)
        self.assertEqual(odd_digits("6011111111111117"), 15)

    def test_validity_of_card(self):
        self.assertEqual(even_double_digits("4111111111111111") + odd_digits("4111111111111111") % 10, 0)
        self.assertEqual(even_double_digits("5555555555554444") + odd_digits("5555555555554444") % 10, 0)
        self.assertEqual(even_double_digits("371449635398431") + odd_digits("371449635398431") % 10, 0)
        self.assertEqual(even_double_digits("6011111111111117") + odd_digits("6011111111111117") % 10, 0)


if __name__ == '__main__':
    unittest.main()
