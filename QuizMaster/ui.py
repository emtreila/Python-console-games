from quiz_master.service import Service


class UI:
    def __init__(self, service: Service = Service):
        self.service = service
        self.id_list = self.service.get_ids()
        self.number_of_questions = self.service.get_number_of_questions()

    def handle_add_question(self, arguments):
        if len(arguments) != 8:
            raise ValueError("Invalid number of arguments!")

        question_id = arguments[1].strip()
        text = arguments[2].strip()
        choice_a = arguments[3].strip()
        choice_b = arguments[4].strip()
        choice_c = arguments[5].strip()
        correct = arguments[6].strip()
        difficulty = arguments[7].strip()

        try:
            question_id = int(question_id)
        except:
            raise ValueError("Invalid id!")

        if question_id in self.id_list:
            raise ValueError("Id already exists!")

        if correct != choice_a and correct != choice_b and correct != choice_c:
            raise ValueError("Invalid correct answer!")

        if difficulty not in ["easy", "medium", "hard"]:
            raise ValueError("Invalid difficulty level!")

        self.service.add_question(question_id, text, choice_a, choice_b, choice_c, correct, difficulty)

    def handle_exit(self):
        exit()

    def handle_create_quiz(self, arguments):
        if len(arguments) != 4:
            raise ValueError("Invalid number of arguments!")

        difficulty = arguments[1].strip()
        number_of_questions = arguments[2].strip()
        file = arguments[3].strip()

        if difficulty not in ["easy", "medium", "hard"]:
            raise ValueError("Invalid difficulty level!")

        try:
            number_of_questions = int(number_of_questions)
        except:
            raise ValueError("Invalid number of questions!")

        if number_of_questions > self.number_of_questions:
            raise ValueError("Not enough questions!")

        try:
            self.service.create_quiz(difficulty, number_of_questions, file)
        except Exception as e:
            print(e)

    def handle_start(self, arguments):
        if len(arguments) != 2:
            raise ValueError("Invalid number of arguments!")

        file = arguments[1].strip()
        names = self.service.get_quiz_files()
        if file not in names:
            raise ValueError("Invalid file name!")
        score = 0
        quiz_questions = self.service.get_quiz(file)
        for question in quiz_questions:
            print(f"Current score: {score}")
            print(f"{question.text}\nA. {question.choice_a}\nB. {question.choice_b}\nC. {question.choice_c}")
            answer = input("Enter your answer: ")
            if answer != question.correct:
                print("Wrong answer!")
            else:
                print("Correct answer!")
                if question.difficulty == "easy":
                    score += 1
                elif question.difficulty == "medium":
                    score += 2
                else:
                    score += 3
        print("Quiz finished!")
        print(f"Final score: {score}")

    def main(self):

        print("add <id> <text> <choice_a> <choice_b> <choice_c> <correct> <difficulty>")
        print("create <difficulty> <number_of_questions> <file>")
        print("start <file>")
        print("exit")

        while True:

            commands = {
                "add": self.handle_add_question,
                "create": self.handle_create_quiz,
                "start": self.handle_start,
                "exit": self.handle_exit
            }

            command = input("Enter command: ")
            if not command:
                print("No command given!")
                continue

            arguments = command.split()
            command_name = arguments[0].strip()

            handle_for_command = commands.get(command_name)
            if not handle_for_command:
                print(f"Command {command_name} not accepted!")
                continue

            try:
                if command_name == "add":
                    handle_for_command(arguments)
                elif command_name == "create":
                    handle_for_command(arguments)
                elif command_name == "start":
                    handle_for_command(arguments)
                elif command_name == "exit":
                    handle_for_command()

            except Exception as e:
                print(e)
