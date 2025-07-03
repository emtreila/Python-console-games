import unittest

from hangman.repository import TextMemoRepo


class TestRepository(unittest.TestCase):
    def __setup(self):
        self.repository = TextMemoRepo("test_sentences.txt")
        with open("test_sentences.txt", "w") as f:
            f.write("anna has apples\npatricia has pears\n")

