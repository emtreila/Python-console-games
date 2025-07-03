class TextMemoRepo:
    def __init__(self, file_name: str = "sentences.txt"):
        self._file_name = file_name
        self._data_sentences = []

    def load_sentences(self):
        """
        Loads the sentences to the file
        """
        with open(self._file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def save_sentences(self, sentences):
        """
        Saves the sentences
        :param sentences: the sentences to be saved
        """
        with open(self._file_name, 'w') as file:
            file.writelines([sentence + '\n' for sentence in sentences])

    def add_sentence(self, sentence):
        """
        Adds a new sentence to the file
        :param sentence: the new sentence
        """
        sentences = self.load_sentences()
        if sentence in sentences:
            raise ValueError("Duplicate sentence.")
        if not self.is_valid_sentence(sentence):
            raise ValueError("Invalid sentence. Words must have at least 3 letters.")
        sentences.append(sentence)
        self.save_sentences(sentences)

    def is_valid_sentence(self, sentence):
        """
        Check if all the words have at least 3 letters and if there are no duplicate sentences
        :param sentence: the sentence to be checked
        :return: True = if it's ok, False = otherwise
        """
        words = sentence.split()
        for word in words:
            if len(word) < 3:
                return False
        return True

    def get_all_sentences(self):
        """
        :return: returns all the sentences in a list
        """
        return self.load_sentences()
