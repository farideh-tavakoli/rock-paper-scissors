"""
Aythor: Farideh Tavakoli
Date Created: 10/12/2024
Description: Rock Paper Scissors game.
"""

import random 
from typing import List

class RockPaperScissors:
    """Main class for Rock Paper Scissors game.
    """ 
    def __init__(self, name: str):
        self.choices: List[str] = ['rock', 'paper', 'scissors']
        self.name: str = name
    
    def get_player_choice(self):
        player_choice: str = input(f'Choose among ({self.choices}): ')
        if player_choice.lower() in self.choices:
            return player_choice.lower()
        else:
            print("Invalid Input. Please Try Again.")
            return self.get_player_choice()

    def get_computer_choice(self):
        """Get computer choice randomly from choices: Rock, Paper, Scissor."""
        return random.choice(self.choices)
    
    def decide_winner(self, player_choice: str, computer_choice: str) -> str:
        """Decide the winner based on user and computer choices. 

        :param player_choice: Choice of the player
        :param computer_choice: Choice of the computer
        :return: The result of the game. Who is the winner?
        """
        if player_choice == computer_choice:
            return "It's a Tie!"
        winning_combinations = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]

        for winning_comb in winning_combinations:
            if (player_choice == winning_comb[0]) and (computer_choice == winning_comb[1]):
                return "Congrats! You Won!"
        
        return "Oh no! The Computer Won!"

    def play(self):
        """Play the game.
        - Get player choice.
        - Get computer choice.
        - Decide the winner.
        - Print the result.
        """
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f'Player choice: {player_choice} and Computer Choice: {computer_choice}')
        print(self.decide_winner(player_choice, computer_choice))


if __name__ == '__main__':
    game = RockPaperScissors('Fari')

    while True:
        game.play()
        play_again = input('To play again press any keys/ To leave the game press q/Q: ')
        if play_again.lower() == 'q':
            break