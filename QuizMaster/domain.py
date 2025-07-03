class Question:
    def __init__(self, question_id, text, choice_a, choice_b, choice_c, correct, difficulty):
        self._text = text
        self._choice_a = choice_a
        self._choice_b = choice_b
        self._choice_c = choice_c
        self._correct = correct
        self._difficulty = difficulty
        self._question_id = question_id

    @property
    def question_id(self):
        return self._question_id

    @question_id.setter
    def question_id(self, value):
        self._question_id = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def choice_a(self):
        return self._choice_a

    @choice_a.setter
    def choice_a(self, value):
        self._choice_a = value

    @property
    def choice_b(self):
        return self._choice_b

    @choice_b.setter
    def choice_b(self, value):
        self._choice_b = value

    @property
    def choice_c(self):
        return self._choice_c

    @choice_c.setter
    def choice_c(self, value):
        self._choice_c = value

    @property
    def correct(self):
        return self._correct

    @correct.setter
    def correct(self, value):
        self._correct = value

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        self._difficulty = value

    def __str__(self):
        return f"{self._text} {self._choice_a} {self._choice_b} {self._choice_c} {self._correct} {self._difficulty}"

    def __repr__(self):
        return self.__str__()
