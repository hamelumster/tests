import unittest
from palindroms import solve

class TestPalindromicPhrases(unittest.TestCase):

    def test_palindromic_phrases(self):
        phrases = [
            "нажал кабан на баклажан",  # палиндром
            "дом как комод",           # не палиндром
            "рвал дед лавр",           # палиндром
            "азот калий и лактоза",    # палиндром
            "а собака боса",           # палиндром
            "тонет енот",              # палиндром
            "карман мрак",             # не палиндром
            "пуст суп"                 # палиндром
        ]
        expected = [
            "нажал кабан на баклажан",
            "рвал дед лавр",
            "азот калий и лактоза",
            "а собака боса",
            "тонет енот",
            "пуст суп"
        ]
        result = solve(phrases)
        self.assertEqual(result, expected)

    def test_no_palindromic_phrases(self):
        phrases = [
            "дом как комод",
            "карман мрак"
        ]
        expected = []
        result = solve(phrases)
        self.assertEqual(result, expected)

    def test_mixed_phrases(self):
        phrases = [
            "тонет енот",  # палиндром
            "карман мрак",  # не палиндром
            "пуст суп"  # палиндром
        ]
        expected = [
            "тонет енот",
            "пуст суп"
        ]
        result = solve(phrases)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()