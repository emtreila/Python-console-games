from hangman.service import Service


class UI(Service):
    def __init__(self, service: Service = Service):
        super().__init__()
        self._service = service

    def display_progress(self, sentence, correct_letters, hangman_index):
        words = sentence.strip().split()
        for word in words:
            print(f"{word[0]}", end=" ")
            for letter in word[1:-1]:
                if letter in correct_letters:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print(f"{word[-1]}", end=" ")
        print(f" - {self._service.word_hangman(hangman_index)}")
        print()

    def main(self):
        print("1. Add a sentence.")
        print("2. Start new game.")
        option = input("Choose your option: ")

        try:
            option = int(option)
        except:
            print("Invalid option!")
            return
        if not (1 <= option <= 2):
            print("Invalid option!")
        if not option:
            print("Invalid option!")

        if option == 1:
            while True:
                sentence = input("Enter sentence: ")
                words = sentence.strip().split()
                if not sentence:
                    print("No sentence!")
                    continue
                for word in words:
                    if len(word) < 3:
                        print("Words must have at least 3 letters!")
                        continue

                try:
                    self._service.add_sentence(sentence)
                    print("Sentence added!")
                    break
                except Exception as e:
                    print(e)

        elif option == 2:
            hangman_index = 0
            sentence = self._service.choose_sentence(self._service.get_all_sentences())
            words = sentence.strip().split()
            correct_letters = ""
            for word in words:
                correct_letters += word[0]
                correct_letters += word[-1]
                print(correct_letters)

            guessed_letters = set()

            while True:
                self.display_progress(sentence, correct_letters, hangman_index)

                if all(letter in correct_letters or not letter.isalpha() for letter in sentence):
                    print("\nYou won!")
                    break

                if hangman_index >= 6:
                    print("\nYou lost! The sentence was:", sentence)
                    break

                guess = input("Guess a letter: ").lower()

                if not guess.isalpha():
                    print("Invalid letter!")
                    continue
                if guess in guessed_letters:
                    hangman_index += 1
                    print("You already guessed that letter!")
                    continue
                guessed_letters.add(guess)

                if guess in sentence:
                    correct_letters.add(guess)
                else:
                    hangman_index += 1
