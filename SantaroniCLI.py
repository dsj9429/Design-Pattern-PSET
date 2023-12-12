"""Main interface for the Bank application."""
import sys
import copy
import random
import logging
from exceptions import *

from decimal import Decimal, setcontext, BasicContext, InvalidOperation
from datetime import datetime
from santorini import Santorini
from board import Board

logging.basicConfig(filename='santorini.log', format='%(asctime)s|%(levelname)s|%(message)s', datefmt='%Y-%m-%d %I:%M:%S', encoding='utf-8', level=logging.DEBUG)
# context with ROUND_HALF_UP
setcontext(BasicContext)

class SantoriniCLI:
    """Driver class for a command-line REPL interface to the Bank application"""

    def __init__(self):
        self.game = Santorini()
        # self._selected_account = None

    def display_prompt(self):
        """Display the menu and respond to choices."""

        while True:
            # displays board
            self.display_board()
            colors = ["white, (AB)", "blue, (YZ)"]
            turn = 1
            
            # while game is not over, print number of turns and player 
            while self.game.check_win() == False: # need to write out check_win first
                # if turn number is odd, start off with white
                if turn % 2 == 1:
                    print(f"Turn {turn}, {colors[0]}\n")
                else: 
                    print(f"Turn {turn}, {colors[1]}\n")
            while True:        
                try: 
                    worker_selected = input("Select a worker to move\n")
                except InvalidWorker:
                    print("Not a valid worker")
                except OpponentPiece: 
                    print("That is not your worker")
                
            while True: 
                try: 
                    dir_move = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")
                except InvalidDirError:
                    print("Not a valid direction")
                except MoveError as error: 
                    print(f"Cannot move {error.direction}")
                    
            while True: 
                try: 
                    dir_build = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")
                except InvalidDirError:
                    print("Not a valid direction")
                except BuildError as error:
                    print(f"Cannot move {error.direction}")
                
      
    def _quit(self):
        sys.exit(0)

if __name__ == "__main__":
    try: 
        SantoriniCLI().run()
    except Exception as e:
        print("Sorry! Something unexpected happened. Check the logs or contact the developer for assistance.")
        logging.error("%s: '%s'", type(e).__name__, str(e))