from quiz_master.domain import Question


class Repo:
    def __init__(self, filename="questions_list.txt"):
        self._filename = filename
        self._questions_data: dict[int, Question] = {}
        self.id_list = []
        self.number_of_questions = 0
        self.quiz_files = []
        self.read_from_file()

    def read_from_file(self):
        """
        Reads the questions from the file
        """
        try:
            with open(self._filename, "r") as f:
                for line in f.readlines():
                    attributes = line.strip().split(",")
                    if len(attributes) != 7:
                        continue
                    question_id = int(attributes[0])
                    text = attributes[1]
                    choice_a = attributes[2]
                    choice_b = attributes[3]
                    choice_c = attributes[4]
                    correct = attributes[5]
                    difficulty = attributes[6]

                    question = Question(question_id, text, choice_a, choice_b, choice_c, correct, difficulty)
                    self._questions_data[question_id] = question
                    self.id_list.append(question_id)
                    self.number_of_questions += 1
        except FileNotFoundError:
            raise Exception("File not found")

    def write_to_file(self):
        """
        Writes the questions to the file
        """
        with open(self._filename, "w") as f:
            for question in self._questions_data.values():
                f.write(
                    f"{question.question_id},{question.text},{question.choice_a},{question.choice_b},{question.choice_c},{question.correct},{question.difficulty}\n")

    def add_question(self, question: Question):
        """
        Adds a question to the repository
        :param question: the new question
        """

        self._questions_data[question.question_id] = question
        self.id_list.append(question.question_id)
        self.number_of_questions += 1
        self.write_to_file()

    def get_question_list(self):
        """
        :return: the list of questions
        """
        return self._questions_data

    def write_quiz(self, questions, file):
        """
        Writes a quiz to a file
        :param questions: the questions
        :param file: the file to write to
        """
        self.quiz_files.append(file)
        with open(file, "w") as f:
            for question in questions:
                f.write(
                    f"{question.question_id},{question.text},{question.choice_a},{question.choice_b},{question.choice_c},{question.correct},{question.difficulty}\n")

    def read_quiz(self, file):
        """
        Reads a quiz from a file
        :param file: the file to read from
        :return: the list of questions
        """
        questions = []
        with open(file, "r") as f:
            for line in f.readlines():
                attributes = line.strip().split(",")
                if len(attributes) != 7:
                    continue
                question_id = int(attributes[0])
                text = attributes[1]
                choice_a = attributes[2]
                choice_b = attributes[3]
                choice_c = attributes[4]
                correct = attributes[5]
                difficulty = attributes[6]

                question = Question(question_id, text, choice_a, choice_b, choice_c, correct, difficulty)
                questions.append(question)
        return questions
