import random
from typing import Tuple, List


class MasterMindBinary:
    _ZERO_BIT = '0'
    _ONE_BIT = '1'
    _ZERO_AND_ONE = [_ZERO_BIT, _ONE_BIT]

    def __init__(self, bits=4, number_of_guesses=10, auto_play=False, show_computer_guess=False):
        self._guesses_feedbacks: List[Tuple[str, int]] = []  # tuple feedback guess
        self._computer_guess = None  # computer guess
        self._bits = bits
        self._number_of_guesses = number_of_guesses
        self._auto_play = auto_play
        self._show_computer_guess = show_computer_guess
        self._all_bits_combination = []
        self._auto_play_state = {
            "first_move": True,
            "guess_value": None,  # TODO we can get rid of this
            "filtered_state": [],  # feedback number state,
            "history_of_filtered_state": []
        }

    def play_game(self):
        print("Welcome to MasterMind")
        print("Guess the secret code in {} tries or fewer".format(self._number_of_guesses))
        self._generate_random_computer_guess()

        if self._show_computer_guess:
            print("Computer Guess {}".format(self._computer_guess))

        for i in range(self._number_of_guesses):
            guess = self.auto_play_guess() if self._auto_play else self._get_user_guess()
            self._guesses_feedbacks.append((guess, self._evaluate_guess(guess)))

            if self._get_latest_feedback() == self._bits:
                print("Congrats you have guesses it")
                return

            print("****************************************************************")
            print("Your Past Guess and Feedbacks {}".format(self._guesses_feedbacks))
            print("****************************************************************")

        print("Loser you have lost")

    def _get_user_guess(self):
        guess = input("Enter your guess ({} digits): ".format(self._bits))
        while len(guess) != self._bits or not all(
                char in MasterMindBinary._ZERO_AND_ONE for char in
                guess):  # access the last element in the array
            guess = input("Wrong!! Please Enter your guess ({} digits): ".format(self._bits))
        return guess

    def _evaluate_guess(self, code: str):
        return self._evaluate_guess_core(code, self._computer_guess)

    def _evaluate_guess_core(self, code: str, other_code: str):
        return sum(int(code[i] == other_code[i]) for i in range(self._bits))

    def _get_guess(self, index):
        return self._guesses_feedbacks[index][0]

    def _get_feedback(self, index):
        return self._guesses_feedbacks[index][1]

    def _get_latest_feedback(self):
        return self._get_feedback(-1)

    def _get_latest_guess(self):
        return self._get_guess(-1)

    def _generate_random_computer_guess(self):
        self._computer_guess = ''.join([random.choice(MasterMindBinary._ZERO_AND_ONE) for i in range(self._bits)])

    def _generate_auto_play_all_state(self, digit):
        if digit == 0:
            return [MasterMindBinary._ZERO_BIT]
        if digit == 1:
            return list(MasterMindBinary._ZERO_AND_ONE)  # reference protection

        prev_numbers = self._generate_auto_play_all_state(digit - 1)
        current_numbers = []
        for number in prev_numbers:
            current_numbers.append(number + MasterMindBinary._ZERO_BIT)
            current_numbers.append(number + MasterMindBinary._ONE_BIT)

        return current_numbers

    def _filter_state_with_same_guess(self, current_filter_item) -> bool:
        evaluation = self._evaluate_guess_core(current_filter_item, self._get_latest_guess())
        return evaluation == self._get_latest_feedback()

    def auto_play_guess(self):
        if self._auto_play_state['first_move']:
            self._auto_play_state['filtered_state'] = self._generate_auto_play_all_state(
                self._bits)
            self._all_bits_combination = list(self._auto_play_state['filtered_state'])
            self._auto_play_state['first_move'] = False
            self._auto_play_state['guess_value'] = random.choice(self._auto_play_state['filtered_state'])
            return self._auto_play_state['guess_value']

        # filtered states
        self._auto_play_state['filtered_state'] = list(
            filter(lambda x: self._filter_state_with_same_guess(x), self._auto_play_state['filtered_state']))

        self._auto_play_state['history_of_filtered_state'].append(self._auto_play_state['filtered_state'])

        self._auto_play_state['guess_value'] = random.choice(self._auto_play_state['filtered_state'])

        return self._auto_play_state['guess_value']

    def print_results(self):
        print("Computer Guess is {}".format(self._computer_guess))
        print("Your Guess and Feedbacks {}".format(self._guesses_feedbacks))

    def get_results_of_iterations(self):  # TODO maybe check the reference thing return
        return list(self._auto_play_state['history_of_filtered_state']), list(self._guesses_feedbacks), list(
            self._all_bits_combination)


if __name__ == "__main__":
    masterMind = MasterMindBinary(auto_play=True, show_computer_guess=True)
    masterMind.play_game()
    masterMind.print_results()
    print(masterMind.get_results_of_iterations())
