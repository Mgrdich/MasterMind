import random


class MasterMindBinary:
    _ZERO_BIT = '0'
    _ONE_BIT = '1'
    _ZERO_AND_ONE = [_ZERO_BIT, _ONE_BIT]

    def __int__(self, number):
        self._guesses = []
        self._computer_guess = ''
        self._bits = 4
        if number is not None:
            self._bits = number

    def play_game(self):
        print("Welcome to MasterMind")
        print("Guess the secret code in {} tries or fewer")

    def get_guess(self, index):
        guess = input("Enter your guess ({} digits): ".format(self._computer_guess))
        while len(guess) != self._computer_guess or not all(
                char in MasterMindBinary._ZERO_AND_ONE for char in self._guesses[index]):
            guess = input("Enter your guess ({} digits): ".format(self._computer_guess))
        self._guesses.append(guess)

    def evaluate_guess(self, code):
        return sum(code[i] == self._computer_guess[i] for i in range(self._bits))

    @staticmethod
    def generate_random(digit_number=4):
        return ''.join([random.choice(MasterMindBinary._ZERO_AND_ONE) for i in range(digit_number)])
