from spaceman import get_guessed_word, is_guess_in_word, is_word_guessed
import unittest

# ---- TESTING ---- #
class ComplimentsTest(unittest.TestCase):
    def test_is_word_guessed(self):
        self.assertEqual(is_word_guessed("wood", ["w", "o", "o", "d"]), True)
        self.assertEqual(is_word_guessed("wood", ["e", "o", "o", "d"]), False)

    def test_get_guessed_word(self):
        self.assertEqual(get_guessed_word("a", "cat", ['_', '_', '_']), ["_", "a", "_"])

    def test_is_guess_in_word(self):
        self.assertEqual(is_guess_in_word('v', 'volatile'), True)
        self.assertEqual(is_guess_in_word('d', 'pop'), False)

def test_functions():
    assert is_word_guessed("road", ["r", "o", "a", "d"]) == True
    assert is_word_guessed("road", ["r", "o", "v", "d"]) == False
    assert get_guessed_word("d", "dog", ['_', 'o', 'g']) == ['d', 'o', 'g']
    assert get_guessed_word("e", "car", ['_', 'a', 'r']) == ['_', 'a', 'r']
    assert is_guess_in_word("t", "tailor") == True
    assert is_guess_in_word("r", "late") == False
    
if __name__ == "__main__":
    unittest.main()
