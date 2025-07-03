class TextMemoRepo:
    def __init__(self, file_name: str = "rooms.txt"):
        self._file_name = file_name
        self._data_sentences = []
        self.__read_from_file()

    def __read_from_file(self):
        with open(self._file_name, "r") as f:
            for line in f.readlines():
                self._data_sentences.append(line.strip())

    def get_sentences(self):
        """
        :return: all the sentences
        """
        return self._data_sentences
