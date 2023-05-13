import random
from typing import Tuple, List


class MasterMindBinary:
    _ZERO_BIT = '0'
    _ONE_BIT = '1'
    _ZERO_AND_ONE = [_ZERO_BIT, _ONE_BIT]

    def __int__(self, number=4, number_of_guesses=10):
        self._guesses_feedbacks: List[Tuple[str, number]] = []  # tuple feedback guess
        self._computer_guess = None  # computer guess
        self._bits = 4
        self._number_of_guesses = number_of_guesses

    def play_game(self):
        print("Welcome to MasterMind")
        print("Guess the secret code in {} tries or fewer".format(self._bits))
        self._generate_random()
        for i in range(self._number_of_guesses):
            guess = self._get_user_guess()
            self._guesses_feedbacks.append((guess, self._evaluate_guess(guess)))

            if self._get_feedback(-1) == self._bits:
                print("Congrats you have guesses it")  # TODO maybe print array
                return

        print("Loser you have lost")

    def _get_user_guess(self):
        guess = input("Enter your guess ({} digits): ".format(self._computer_guess))
        while len(guess) != self._computer_guess or not all(
                char in MasterMindBinary._ZERO_AND_ONE for char in
                self._get_guess(-1)):  # access the last element in the array
            guess = input("Enter your guess ({} digits): ".format(self._computer_guess))
        return guess

    def _evaluate_guess(self, code: str):
        return sum(int(code[i] == self._computer_guess[i]) for i in range(self._bits))

    def _get_guess(self, index):
        return self._guesses_feedbacks[index][0]

    def _get_feedback(self, index):
        return self._guesses_feedbacks[index][1]

    def _generate_random(self):
        self._computer_guess = ''.join([random.choice(MasterMindBinary._ZERO_AND_ONE) for i in range(self._bits)])


if __name__ == "__main__":
    masterMind = MasterMindBinary()
    masterMind.play_game()
