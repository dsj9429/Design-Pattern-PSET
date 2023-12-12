"""Main interface for the Bank application."""
import sys
import copy
import random
import logging
from exceptions import *

from santorini import Santorini

class SantoriniCLI:
    """Driver class for a command-line interface to the Santorini application"""

    def __init__(self):
        self.play_again = True

    def run(self):
        """
        @brief Run the entire game by prompting the user for inputs.
        @param None
        @return None
        """
        while self.play_again:
            self.game = Santorini()
            self.game.turn = 1

            while True:
                self.game.board.display_board()
                print(f"Turn: {self.game.turn}, {self.game.curr_player.player_id} ({''.join(self.game.curr_player.workers.keys())})")
                
                worker_id = input("Select a worker to move\n")
                move_direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw):\n")
                build_direction = input("Select a direction to build (n, ne, e, se, s, sw, w, nw):\n")

                # Check if the move is a valid move
                # if self.game.check_move(worker_id, move_direction) and self.game.check_build(worker_id, build_direction):
                # Save the state before making a move for undo/redo
                self.game.curr_player.save_state()
                
                # Make the move and build
                self.game.curr_player.workers[worker_id].move(move_direction)
                self.game.curr_player.workers[worker_id].build(build_direction)

                # Check for a win
                if self.game.check_win():
                    self.game.board.display_board()
                    print(f"{self.game.curr_player} has won")
                    break

                # Switch player for the next turn
                self.game.turn += 1
                self.game.switch_player()
                
                print(f"{worker_id},{move_direction},{build_direction}\n")
                # else:
                #     print("Invalid move. Please try again.\n")
                    
            again = input("Play again\n")
            self.play_again = again == 'yes'

if __name__ == "__main__":

    SantoriniCLI().run()

    logging.error("%s: '%s'", type(e).__name__, str(e))