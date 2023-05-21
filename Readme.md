# MasterMind

This the is MasterMind Project , optimized to run the binary case.

## How to Start the Game

* Download `pipenv` by running `pip install --user pipenv`
* `cd` go to the project directory
* Create Virtual env `pipenv`
* Run the file `python ./main.py`

## How to play the game

You have two options to play the game

* is that you are the player
* Or you can sit and watch the computer do its thing

For now if you want the autoplay mode when the computer does all the guesses for you
`masterMind = MasterMindBinary(auto_play=True)`

if you want to cheat and see the computer generated number choose
`masterMind = MasterMindBinary(show_computer_guess=True)`

Default game parameter of the game is guessing binary number of `4` bits , with `10` guesses To change the option
`masterMind = MasterMindBinary(bits=int, number_of_guesses=int)`

In the future you will be able to toggle those parameters with the shell flags 


`masterMind.play_game()` is the one that kicks off the algorithm
`masterMind.print_results()` is where you see your result 

but steps by step algorithm has logs , it will be configurable in the future.

