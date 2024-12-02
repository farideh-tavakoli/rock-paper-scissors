import random 

class RockPaperScissors:
    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.name = name
    
    def get_player_choice(self):
        player_choice = input(f'Choose among ({self.choices}): ')
        if player_choice.lower() in self.choices:
            return player_choice.lower()
        else:
            print("Invalid Input. Please Try Again.")
            return self.get_player_choice()

    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def decide_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a Tie!"
        winning_combinations = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]

        for winning_comb in winning_combinations:
            if (player_choice == winning_comb[0]) and (computer_choice == winning_comb[1]):
                return "Congrats! You Won!"
        
        return "Oh no! The Computer Won!"

    def play(self):
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