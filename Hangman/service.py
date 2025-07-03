import random

from hangman.repository import TextMemoRepo


class Service(TextMemoRepo):
    def __init__(self, sentence_repo: TextMemoRepo = TextMemoRepo):
        super().__init__()
        self._sentence_repo = sentence_repo

    def add_sentence(self, new_sentence):
        """
        Adds a new sentence to  the file
        :param new_sentence:
        """
        self._sentence_repo.add_sentence(new_sentence)

    def choose_sentence(self, all_sentences):
        """
        Choose randomly a sentence
        :param all_sentences: all the sentences from the file
        :return: the randomly chosen sentence
        """
        random_sentence = random.choice(all_sentences)
        return random_sentence

    def word_hangman(self, index):
        """
        :param index:
        :return: returns the word hangman meaning how many more tries
        """
        if index == 1:
            return "h"
        elif index == 2:
            return "ha"
        elif index == 3:
            return "han"
        elif index == 4:
            return "hang"
        elif index == 5:
            return "hangm"
        elif index == 6:
            return "hangma"
        elif index == 7:
            return "hangman"
        elif index == 0:
            return ""
