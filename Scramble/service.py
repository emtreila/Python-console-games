import random

from scramble.repository import TextMemoRepo


class Service:
    def __init__(self, repo: TextMemoRepo = TextMemoRepo):
        self._repo = repo

    def get_sentences(self):
        """
        :return: all the sentences
        """
        return self._repo.get_sentences()

    def scramble_letters(self, sentence):
        """
        Scrambles the letters in the given sentence
        :param sentence: the sentence to be scrambled
        :return: the scrambled sentence
        """

        letters = []
        words = sentence
        for word in words:
            letters.append(word[1:-1])

        random.shuffle(letters)
        letters = "".join(letters)

        index = 0
        final_sentence = []
        for word in words:
            put_letters = len(word) - 2
            word_letters = [x for x in letters[index:index + put_letters]]
            new_word = word[0] + "".join(word_letters) + word[-1]
            final_sentence.append(new_word)

            index += put_letters

        return " ".join(final_sentence)

    def swap(self, sentence, word1, letter1, word2, letter2):
        """
        Swaps the letters in the given sentence
        :param sentence: the sentence to be swapped
        :param word1: the first word
        :param letter1: the first letter
        :param word2: the second word
        :param letter2: the second letter
        :return: the swapped sentence
        """
        if word1 == word2:
            w = sentence[word1]
            l = [x for x in w]
            aux = l[letter1]
            l[letter1] = l[letter2]
            l[letter2] = aux

            new = "".join(l)
            sentence[word1] = new

        else:
            w1 = sentence[word1]
            w2 = sentence[word2]
            l1 = [x for x in w1]
            l2 = [x for x in w2]

            aux = l1[letter1]
            l1[letter1] = l2[letter2]
            l2[letter2] = aux

            new1 = "".join(l1)
            new2 = "".join(l2)

            sentence[word1] = new1
            sentence[word2] = new2

        return " ".join(sentence)
