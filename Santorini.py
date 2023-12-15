from board import Board
from player import Player
from worker import Worker
from exceptions import *

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

    def get_board(self):
        """
        @brief: Get the current state of the board
        @return: The current board
        """
        return self.board

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
        @brief Checks if a player has won.
        @param None
        @return player_id if they have won, false otherwise
        """
        # Checks both players
        for player in [self.player_white, self.player_blue]:
            # Checks all workers of this player
            for worker in player.workers.values():
                row, col = worker.position
                # Returns id of player if that player is in a level 3 building
                if self.board.get_building_level(row, col) == 3:
                    return player.player_id
        return False
    
    def check_loss(self):
        """
        @brief: Checks if the current player loses because they're trapped
        @return: True if the current player loses, False otherwise.
        """
        valid_dir = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
        
        # If worker cannot move or buildin any direction, return false
        for worker in self.curr_player.workers.values():
            can_move = any(worker.can_move_in_direction(direction)
                           for direction in valid_dir)
            can_build = any(worker.can_build_in_direction(direction)
                            for direction in valid_dir)
            if can_move or can_build:
                return False
        return True

    def check_worker(self, worker_id, valid_directions):
        """
        @brief: Check if worker is valid worker
        @param worker_id: worker to be checked
        @param valid_directions: list of valid directions
        @return: True if worker is valid, false otherwise
        """
        try:
            if worker_id not in self.curr_player.workers.keys():
                # If worker is opponent's worker, raise error
                if any(worker_id in player.workers.keys()
                       for player in [self.player_white, self.player_blue]):
                    raise OpponentPiece()
                # If worker is not anyone's worker, raise error
                else:
                    raise InvalidWorker()
            
            # If all workers of this player can't move, raise error
            if not any(self.curr_player.workers[worker_id].can_move_in_direction(direction)
                       for direction in valid_directions):
                raise TrappedWorker()
            return True
        except InvalidWorker:
            print("Not a valid worker")
            return False
        except OpponentPiece:
            print("That is not your worker")
            return False
        except TrappedWorker:
            print("That worker cannot move")
            return False
    
    def check_build(self, worker_id, build_direction, valid_directions):
        """
        @brief: Checks if player can build in that direction
        @param build_direction: The direction to be checked
        @param valid_directions: List of valid directions
        @return: True if there is no error in the build
        """
        try:
            if build_direction not in valid_directions:
                raise InvalidDirError()
            self.curr_player.workers[worker_id].build(build_direction)
            return True
        except InvalidDirError:
            print("Not a valid direction")
            return False
        except BuildError as e:
            print(f"Cannot build {e.direction}")
            return False

    def check_move(self, worker_id, move_direction, valid_directions):
        """
        @brief: Checks if player can move in that direction
        @param move_direction: The direction to be moved
        @param valid_directions: List of valid directions
        @return: True if there is no error in the build
        """
        try:
            if move_direction not in valid_directions:
                raise InvalidDirError()
            self.curr_player.workers[worker_id].move(move_direction)
            return True
        except InvalidDirError:
            print("Not a valid direction")
            return False
        except MoveError as e:
            print(f"Cannot move {e.direction}")
            return False

    def set_worker_positions(self, worker_positions):
        """
        @brief: Set the positions of the workers on the board.
        @param worker_positions: Dictionary mapping worker IDs to positions.
        @return: None
        """
        for worker_id, position in worker_positions.items():
            if worker_id in self.player_blue.workers.keys():
                self.player_blue.workers[worker_id].set_position(position)
            if worker_id in self.player_white.workers.keys():
                self.player_white.workers[worker_id].set_position(position)

    def get_worker_positions(self):
        """
        @brief: Get the positions of the workers on the board.
        @return: Dictionary mapping worker IDs to positions.
        """
        worker_positions = {}
        for worker_id, worker in self.curr_player.workers.items():
            worker_positions[worker_id] = worker.position
        return worker_positions
    
    def set_board(self, board):
        """
        @brief: Set the board to a new board.
        @param board: The new board.
        @return: None
        """
        self.board = board
        self.player_blue.set_board(board)
        self.player_white.set_board(board)
        