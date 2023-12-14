"""Main interface for the Bank application."""
import sys
import argparse
import copy
import logging
from exceptions import *

from santorini import Santorini
from player import HumanPlayer, RandomPlayer, HeuristicPlayer
from worker import Worker
from edit import Edit

class SantoriniCLI:
    """Driver class for a command-line interface to the Santorini application"""

    def __init__(self, white, blue, undo, score):
        self.play_again = True
        self.white = white
        self.blue = blue
        self.undo = undo
        self.score = score
        self.edit = Edit() if undo == 'on' else None
    
    def create_player(self, player_type, player_id):
        """
        @brief Creates different types of players based on player input
        @param player_type: Input can be human, random, or heuristic
        @param player_id: white or blue player
        @return: The type of player initialized
        """
        if player_type == 'human':
            if player_id == 'white':
                return HumanPlayer('white', {'A': Worker('A',
                                                         self.game.board,
                                                         'white', (3, 1)),
                                            'B': Worker('B',
                                                        self.game.board,
                                                        'white', (1, 3))})
            elif player_id == 'blue':
                return HumanPlayer('blue', {'Y': Worker('Y',
                                                        self.game.board,
                                                        'blue', (1, 1)),
                                            'Z': Worker('Z',
                                                        self.game.board,
                                                        'blue', (3, 3))})
        elif player_type == 'random':
            if player_id == 'white':
                return RandomPlayer('white', {'A': Worker('A',
                                                          self.game.board,
                                                          'white', (3, 1)),
                                            'B': Worker('B',
                                                        self.game.board,
                                                        'white', (1, 3))})
            elif player_id == 'blue':
                return RandomPlayer('blue', {'Y': Worker('Y', 
                                                         self.game.board,
                                                         'blue', (1, 1)),
                                            'Z': Worker('Z',
                                                        self.game.board,
                                                        'blue', (3, 3))})
        elif player_type == 'heuristic':
            if player_id == 'white':
                return HeuristicPlayer('white', {'A': Worker('A',
                                                             self.game.board,
                                                             'white', (3, 1)),
                                                'B': Worker('B',
                                                            self.game.board,
                                                            'white', (1, 3))})
            elif player_id == 'blue':
                return HeuristicPlayer('blue', {'Y': Worker('Y',
                                                            self.game.board,
                                                            'blue', (1, 1)),
                                                'Z': Worker('Z',
                                                            self.game.board,
                                                            'blue', (3, 3))})
    def display_turn(self):
        """
        @brief: Print's out the turn order, player, their workers, and score
        @param: None
        @return: None
        """
        turn = self.game.turn
        id = self.game.curr_player.player_id
        workers = self.game.curr_player.workers.keys()
        print(f"Turn: {turn}, {id} ({''.join(workers)})")

    def handle_edit(self):
        """
        @brief: Displays the board based on undo/redo/next options
        @param: None
        @return: None
        """
        if self.edit:
            while True:
                user_input = input("undo, redo, or next\n")
                if user_input == 'undo':
                    if self.game.turn > 1:
                        self.game.board = self.edit.undo_move()
                        self.game.turn -= 1
                        self.game.switch_player()
                    self.game.board.display_board()
                    self.display_turn()
                elif user_input == 'redo':
                    if self.game.turn < self.edit._length:
                        self.game.board = self.edit.redo_move()
                        self.game.turn += 1
                        self.game.switch_player()
                    self.game.board.display_board()
                    self.display_turn()
                elif user_input == 'next':
                    break
                else:
                    raise Exception

    def human_move(self):
        # Used to check for invalid directions
        valid_directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
        
        # Check for invalid worker inputs
        while True:
            worker_id = input("Select a worker to move\n")
            if (self.game.check_worker(worker_id,
                                       valid_directions)):
                break
        
        # Check invalid moves
        while True:
            move_direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")
            if (self.game.check_move(worker_id,
                                     move_direction,
                                     valid_directions)):
                break

        # Check invalid build
        while True:
            build_direction = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")
            if (self.game.check_build(worker_id,
                                      build_direction,
                                      valid_directions)):
                break
        
        print(f"{worker_id},{move_direction},{build_direction}")

    def run(self):
        """
        @brief Run the entire game by prompting the user for inputs.
        @param None
        @return None
        """
        # As long as client wants to play again, run the program
        while self.play_again:
            self.game = Santorini()
            self.game.turn = 1

            players = [self.create_player(self.white, 'white'),
                       self.create_player(self.blue, 'blue')]
            
            self.game.player_white = players[0]
            self.game.player_blue = players[1]
            self.game.curr_player = players[0]

            # Runs the game as long as there are no winners or losers
            while True:
                # Save the state before making a move for undo/redo
                if self.edit:
                    self.edit.record_move(self.game)

                self.game.board.display_board()
                self.display_turn()

                # Shows edit options
                self.handle_edit()

                # Check for a win
                if self.game.check_win():
                    print(f"{self.game.check_win()} has won")
                    break
                
                # Check for a loss
                if self.game.check_loss():
                    self.game.switch_player()
                    print(f"{self.game.curr_player.player_id} has won")
                    break

                # Implement move based on player type
                if isinstance(self.game.curr_player, HumanPlayer):
                    self.human_move()
                elif isinstance(self.game.curr_player, RandomPlayer):
                    self.game.curr_player.make_move()
                elif isinstance(self.game.curr_player, HeuristicPlayer):
                    self.game.curr_player.make_move()

                # Switch player for the next turn
                self.game.turn += 1
                self.game.switch_player()
                    
            again = input("Play again\n")
            self.play_again = again == 'yes'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Santorini Game')
    parser.add_argument('white', nargs='?', default='human')
    parser.add_argument('blue', nargs='?', default='human')
    parser.add_argument('undo', nargs='?', default='off')
    parser.add_argument('score', nargs='?', default='off')

    args = parser.parse_args()
    # try:
    SantoriniCLI(args.white, args.blue, args.undo, args.score).run()
    # except Exception as e:
    # logging.error("%s: '%s'", type(e).__name__, str(e))