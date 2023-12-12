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
        
        self.player_white = Player('white', {'A': Worker('A', self.board,
                                                         'white', (3, 1)),
                                             'B': Worker('B', self.board,
                                                         'white', (1, 3))})
        self.player_blue = Player('blue', {'Y': Worker('Y', self.board,
                                                       'blue', (1, 1)),
                                           'Z': Worker('Z', self.board,
                                                       'blue', (3, 3))})

        self.curr_player = self.player_white
    
    def switch_player(self):
        """
        @brief: Takes turns and switches between the two players.
        @return: None
        """
        if self.curr_player == self.player_white:
            self.curr_player = self.player_blue
        else:
            self.curr_player = self.player_white
    
    def check_win(self):
        """
        @brief: Checks to see if the the worker for curr players are in a
                building with 3 levels.
        """
        for worker in self.curr_player.workers.values():
            row, col = worker.position
            if self.board.get_building_level(row, col) == 3:
                return True
        return False
    
    def check_move(self, worker_id, direction):
        """
        @brief: Checks to see if the curr_Player is able to move to surrounding
                buildings. 
        """
        curr_worker = self.curr_player.workers[worker_id]
        try:
            curr_worker.move(direction)
            return True
        except ValueError:
            return False
    
    def check_build(self, worker_id, direction):
        """
        @brief: Checks to see if the curr_Player is able to build in surrounding
                buildings. 
        """
        curr_worker = self.curr_player.workers[worker_id]
        try:
            curr_worker.build(direction)
            return True
        except ValueError:
            return False

def main():
    game = Santorini()
    game.board.display_board()

if __name__ == "__main__":
    main()