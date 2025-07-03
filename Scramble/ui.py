import random

from scramble.service import Service


class UI:
    def __init__(self, service: Service = Service):
        self._service = service

    def check_victory(self, sentence, score, unscrambled_sentence):
        if sentence == unscrambled_sentence:
            print("\nCongratulations! You have unscrambled the sentence!")
            print(f"Final score: {score}")
            exit()

        elif score == 0:
            print("\nYou have run out of moves!")
            print(f"The sentence was: {self._service.get_sentences()[0]}")
            exit()

        return

    def handle_swap(self, command, sentence, score, undo_swaps, unscrambled_sentence):
        if len(command) != 5:
            raise ValueError("The command is incorrect.")

        word1 = command[1]
        letter1 = command[2]
        word2 = command[3]
        letter2 = command[4]

        try:
            word1 = int(word1)
            word2 = int(word2)
            letter1 = int(letter1)
            letter2 = int(letter2)
        except:
            raise ValueError("The parameters must be integers.")

        w1 = sentence[word1]
        w2 = sentence[word2]
        l1 = [x for x in w1]
        l2 = [x for x in w2]

        if word1 > len(sentence) or word2 > len(sentence):
            raise ValueError("The words are not in the sentence!")

        if letter1 == 0 or letter2 == 0 or letter1 == len(l1) - 1 or letter2 == len(l2) - 1:
            raise ValueError("Cannot swap the first or last letter of a word!")

        undo_swaps.append(sentence[:])
        new = self._service.swap(sentence, word1, letter1, word2, letter2)
        score -= 1
        print(f"\nNew sentence: {new}")
        print(f"Score: {score}")

        self.check_victory(new, score, unscrambled_sentence)
        return score

    def handle_undo(self, command, undo_swaps):
        if len(command) != 1:
            raise ValueError("The command is incorrect.")

        if not undo_swaps:
            raise Exception("No more undos!")

        sentence = undo_swaps.pop()
        sentence = " ".join(sentence)
        print(f"\nNew sentence: {sentence}")

    def main(self):

        sentences = self._service.get_sentences()
        playing = random.choice(sentences)
        sentence = playing.strip().split()
        undo_swaps = []

        score = 0
        for word in sentence:
            score += len(word)

        scrambled_sentence = self._service.scramble_letters(sentence)
        print(f"Scrambled sentence: {scrambled_sentence}")
        print(f"Score: {score}")

        scrambled_sentence = scrambled_sentence.strip().split()

        commands = {
            "swap": self.handle_swap,
            "undo": self.handle_undo
        }

        print("\nCOMMANDS:")
        print("swap <word1> <letter1> <word2> <letter2>")
        print("undo")
        while True:
            command = input("\nEnter command: ")
            if not command:
                print("No command given!")
                continue
            arguments = command.split()
            command_name = arguments[0].strip()

            handle_for_command = commands.get(command_name)
            if not handle_for_command:
                print(f"Command {command_name} is not accepted!")
                continue

            try:
                if command_name == "swap":
                    score = handle_for_command(arguments, scrambled_sentence, score, undo_swaps, playing)

                elif command_name == "undo":
                    handle_for_command(arguments, undo_swaps)

            except Exception as e:
                print(e)
