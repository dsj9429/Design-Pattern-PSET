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

    # def display_prompt(self):
    #     """Display the menu and respond to choices."""

    #     while True:
    #         # displays board
    #         self.display_board()
    #         colors = ["white, (AB)", "blue, (YZ)"]
    #         turn = 1
            
    #         # while game is not over, print number of turns and player 
    #         while self.game.check_win() == False: # need to write out check_win first
    #             # if turn number is odd, start off with white
    #             if turn % 2 == 1:
    #                 print(f"Turn {turn}, {colors[0]}\n")
    #             else: 
    #                 print(f"Turn {turn}, {colors[1]}\n")
    #         while True:        
    #             try: 
    #                 worker_selected = input("Select a worker to move\n")
    #             except InvalidWorker:
    #                 print("Not a valid worker")
    #             except OpponentPiece: 
    #                 print("That is not your worker")
                
    #         while True: 
    #             try: 
    #                 dir_move = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")
    #             except InvalidDirError:
    #                 print("Not a valid direction")
    #             except MoveError as error: 
    #                 print(f"Cannot move {error.direction}")
                    
    #         while True: 
    #             try: 
    #                 dir_build = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")
    #             except InvalidDirError:
    #                 print("Not a valid direction")
    #             except BuildError as error:
    #                 print(f"Cannot move {error.direction}")

    def run(self):
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
                if self.game.check_move(worker_id, move_direction) and self.game.check_build(worker_id, build_direction):
                    # Save the state before making a move for undo/redo
                    self.game.curr_player.save_state()
                    
                    # Make the move and build
                    self.game.curr_player.workers[worker_id].move(move_direction)
                    self.game.curr_player.workers[worker_id].build(build_direction)

                    # Check for a win
                    if self.game.check_win():
                        self.print_board()
                        print(f"{self.game.curr_player} has won")
                        break

                    # Switch player for the next turn
                    self.game.turn += 1
                    self.game.switch_player()
                    
                    print(f"{worker_id},{move_direction},{build_direction}\n")
                else:
                    print("Invalid move. Please try again.\n")
                    
            again = input("Play again\n")
            self.play_again = again == 'yes'

if __name__ == "__main__":
    try: 
        SantoriniCLI().run()
    except Exception as e:
        logging.error("%s: '%s'", type(e).__name__, str(e))