from quiz_master.domain import Question
from quiz_master.repository import Repo


class Service:
    def __init__(self, repo: Repo = Repo):
        self.repo = repo

    def add_question(self, question_id, text, choice_a, choice_b, choice_c, correct, difficulty):
        """
        Adds a question to the repository
        :param question_id: the question id
        :param text: the question text
        :param choice_a: choice A
        :param choice_b: choice B
        :param choice_c: choice C
        :param correct: the correct answer
        :param difficulty: the difficulty level
        """
        question = Question(question_id, text, choice_a, choice_b, choice_c, correct, difficulty)
        self.repo.add_question(question)

    def get_ids(self):
        """
        :return: the list of ids
        """
        return self.repo.id_list

    def get_number_of_questions(self):
        """
        :return: the number of questions
        """
        return self.repo.number_of_questions

    def get_questions(self):
        """
        :return: the list of questions
        """
        return self.repo.get_question_list()

    def create_quiz(self, difficulty, number_of_questions, file):
        """
        Creates a quiz
        :param difficulty: the difficulty level
        :param number_of_questions: the number of questions
        :param file: the file to write the quiz to
        :return:
        """
        questions = [q for q in self.repo.get_question_list().values()]
        nr_questions = 0

        for question in questions:
            if question.difficulty == difficulty:
                nr_questions += 1

        if nr_questions < number_of_questions // 2:
            raise ValueError(f"Not enough questions for a {difficulty} quiz!")

        number_of_questions //= 2
        questions_for_quiz = []
        for question in questions:
            if question.difficulty == difficulty:
                questions_for_quiz.append(question)
                nr_questions -= 1
                if nr_questions == 0:
                    break
            elif number_of_questions > 0:
                questions_for_quiz.append(question)
                number_of_questions -= 1

        self.repo.write_quiz(questions_for_quiz, file)

    def get_quiz(self, file):
        """
        Reads a quiz from a file
        :param file: the file to read from
        :return: the list of questions
        """
        return self.repo.read_quiz(file)

    def get_quiz_files(self):
        """
        :return: the list of quiz files
        """
        return self.repo.quiz_files
