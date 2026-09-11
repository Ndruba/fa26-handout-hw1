"""HW1 Question 3 Tests"""

import sys

sys.path.append('.')
from src.q3 import capitalize_words


"""Please write your tests here."""
def test_capitalize_words_firstletter() -> None:
    """capitalises the first letter in a word"""
    assert capitalize_words("isaac") == "Isaac"

def test_capitalize_words_non_letter_character() -> None:
    """fist non-letter character in a word"""
    assert capitalize_words("8isaac") == "8Isaac"

def test_capitalize_words_space() -> None:
    """characters are separated by space"""
    assert capitalize_words("i s a a c") == "I S A A C"