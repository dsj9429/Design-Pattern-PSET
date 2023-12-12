from board import Board
from player import Player
from worker import Worker

class Santorini:
    def __init__(self):
        """
        @brief: Initializes the Santorini game.
        """        
        initial_positions = {'A': (3, 1), 'B': (1, 3), 'Y': (1, 1), 'Z': (3, 3)}

        self.board = Board(initial_positions)
        
        self.player_white = Player('White', {'A': Worker('A', self.board,
                                                         'White', (3, 1)),
                                             'B': Worker('B', self.board,
                                                         'White', (1, 3))})
        self.player_blue = Player('Blue', {'Y': Worker('Y', self.board,
                                                       'Blue', (1, 1)),
                                           'Z': Worker('Z', self.board,
                                                       'Blue', (3, 3))})

        self.curr_player = self.player_white
    
    def switch_player(self):
        """
        @brief: Takes turns and switches between the two players.
        @return: None
        """
        self.curr_player = 'Blue' if self.curr_player == 'White' else 'White'
    
    def check_win(self):
        """
        @brief: Checks to see if the the worker for curr players are in a
                building with 3 levels.
        """
        pass
    
    def check_move(self):
        """
        @brief: Checks to see if the curr_Player is able to move to surrounding
                buildings. 
        """
        pass
    
    def check_build(self):
        """
        @brief: Checks to see if the curr_Player is able to build in surrounding
                buildings. 
        """
        pass

def main():
    game = Santorini()
    game.board.display_board()

if __name__ == "__main__":
    main()