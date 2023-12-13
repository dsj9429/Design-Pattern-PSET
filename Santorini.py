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
        @brief Checks if a player has won
        @param None
        @return player_id if they have won, false otherwise
        """
        for player in [self.player_white, self.player_blue]:
            for worker in player.workers.values():
                row, col = worker.position
                if self.board.get_building_level(row, col) == 3:
                    return player.player_id
        return False
    
    def check_loss(self):
        """
        @brief: Checks if the current player loses because they're trapped
        @return: True if the current player loses, False otherwise.
        """
        valid_dir = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
        for worker in self.curr_player.workers.values():
            can_move = any(worker.can_move_in_direction(direction) for direction in valid_dir)
            can_build = any(worker.can_build_in_direction(direction) for direction in valid_dir)
            if can_move or can_build:
                return False
        return True

def main():
    game = Santorini()
    game.board.display_board()

if __name__ == "__main__":
    main()