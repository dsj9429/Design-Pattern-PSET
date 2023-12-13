"""Main interface for the Bank application."""
import sys
import argparse
import copy
import random
import logging
from exceptions import *

from santorini import Santorini
from player import RandomPlayer, HeuristicPlayer

class SantoriniCLI:
    """Driver class for a command-line interface to the Santorini application"""

    def __init__(self, white, blue, undo, score):
        self.play_again = True
        self.white = white
        self.blue = blue
        self.undo = undo
        self.score = score
    
    # def create_player(self, player_type, player_id):
    #     if player_type == 'human':
    #         return HumanPlayer(player_id, {})
    #     elif player_type == 'random':
    #         return RandomPlayer(player_id, {})
    #     elif player_type == 'heuristic':
    #         return RandomPlayer(player_id, {})

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

            # Runs the game as long as there are no winners or losers
            while True:
                # Save the state before making a move for undo/redo
                self.game.curr_player.save_state()

                self.game.board.display_board()
                print(f"Turn: {self.game.turn}, {self.game.curr_player.player_id} ({''.join(self.game.curr_player.workers.keys())})")
                
                # Check for a win
                if self.game.check_win():
                    print(f"{self.game.check_win()} has won")
                    break
                
                # Check for a loss
                if self.game.check_loss():
                    self.game.switch_player()
                    print(f"{self.game.curr_player.player_id} has won")
                    break
                
                ##### This block should be in a make_move() for HumanPlayer####
                # Used to check for invalid directions
                valid_directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
                
                # Check for invalid worker inputs
                while True:
                    try:
                        worker_id = input("Select a worker to move\n")
                        if worker_id not in self.game.curr_player.workers.keys():
                            # If worker is opponent's worker, raise error
                            if any(worker_id in player.workers.keys() for player in [self.game.player_white, self.game.player_blue]):
                                raise OpponentPiece()
                            # If worker is not anyone's worker, raise error
                            else:
                                raise InvalidWorker()
                        
                        # If all workers of this player can't move, raise error
                        if not any(self.game.curr_player.workers[worker_id].can_move_in_direction(direction) for direction in valid_directions):
                            raise TrappedWorker()
                        break
                    except InvalidWorker:
                        print("Not a valid worker")
                    except OpponentPiece:
                        print("That is not your worker")
                    except TrappedWorker:
                        print("That worker cannot move")
                
                # Check invalid moves
                while True:
                    try:
                        move_direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")
                        if move_direction not in valid_directions:
                            raise InvalidDirError()
                        self.game.curr_player.workers[worker_id].move(move_direction)
                        break
                    except InvalidDirError:
                        print("Not a valid direction")
                    except MoveError as e:
                        print(f"Cannot move {e.direction}")
                
                # Check invalid build
                while True:
                    try:
                        build_direction = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")
                        if build_direction not in valid_directions:
                            raise InvalidDirError()
                        self.game.curr_player.workers[worker_id].build(build_direction)
                        break
                    except InvalidDirError:
                        print("Not a valid direction")
                    except BuildError as e:
                        print(f"Cannot build {e.direction}")
                
                print(f"{worker_id},{move_direction},{build_direction}")
                
                ##### This block should be in a make_move() for HumanPlayer####

                # Switch player for the next turn
                self.game.turn += 1
                self.game.switch_player()
                    
            again = input("Play again\n")
            self.play_again = again == 'yes'
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Santorini Game')
    parser.add_argument('white', default='human')
    parser.add_argument('blue', default='human')
    parser.add_argument('undo', default='off')
    parser.add_argument('score', default='off')

    args = parser.parse_args()
    # try:
    SantoriniCLI(args.white, args.blue, args.undo, args.score).run()
    # except Exception as e:
    # logging.error("%s: '%s'", type(e).__name__, str(e))