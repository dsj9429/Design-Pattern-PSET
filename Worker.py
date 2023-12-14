from board import Board
from exceptions import MoveError, BuildError, TrappedWorker

class Worker:
    def __init__(self, worker_id, board, player, position):
        """
        @brief Initializes a worker with an ID, player, and position.
        @param worker_id: The ID identifying the worder (A, B, Y, or Z)
        @param player: Player object that has this worker
        @param position: Position of the worker as a tuple of (row, col)
        """
        self.worker_id = worker_id
        self.board = board
        self.player = player
        self.position = position
    
    def can_move_in_direction(self, direction):
        """
        @brief Checks if the worker can move in a given direction.
        @param direction: The direction to be checked.
        @return True if the worker can move in the specified direction
        """
        row, col = self.position
        
        # Checks if direction is not out of the board and is below level 4
        if direction == 'n' and row - 1 > -1:
            return not self.board.is_position_occupied((row - 1, col)) and self.board.get_building_level(row - 1, col) < 4
        elif direction == 'ne' and row - 1 > -1 and col + 1 < 5:
            return not self.board.is_position_occupied((row - 1, col + 1)) and self.board.get_building_level(row - 1, col + 1) < 4
        elif direction == 'e' and col + 1 < 5:
            return not self.board.is_position_occupied((row, col + 1)) and self.board.get_building_level(row, col + 1) < 4
        elif direction == 'se' and row + 1 < 5 and col + 1 < 5:
            return not self.board.is_position_occupied((row + 1, col + 1)) and self.board.get_building_level(row + 1, col + 1) < 4
        elif direction == 's' and row + 1 < 5:
            return not self.board.is_position_occupied((row + 1, col)) and self.board.get_building_level(row + 1, col) < 4
        elif direction == 'sw' and row + 1 < 5 and col - 1 > -1:
            return not self.board.is_position_occupied((row + 1, col - 1)) and self.board.get_building_level(row + 1, col - 1) < 4
        elif direction == 'w' and col - 1 > -1:
            return not self.board.is_position_occupied((row, col - 1)) and self.board.get_building_level(row, col - 1) < 4
        elif direction == 'nw' and row - 1 > -1 and col - 1 > -1:
            return not self.board.is_position_occupied((row - 1, col - 1)) and self.board.get_building_level(row - 1, col - 1) < 4
        else:
            return False
    
    def can_build_in_direction(self, direction):
        """
        @brief Checks if the worker can build in a given direction
        @param direction: The direction to be checked
        @return True if the worker can build in the specified direction
        """
        row, col = self.position
        target_position = None

        # Checks if direction is not out of the board and is below level 4
        if direction == 'n' and row - 1 > -1:
            target_position = (row - 1, col)
        elif direction == 'ne' and row - 1 > -1 and col + 1 < 5:
            target_position = (row - 1, col + 1)
        elif direction == 'e' and col + 1 < 5:
            target_position = (row, col + 1)
        elif direction == 'se' and row + 1 < 5 and col + 1 < 5:
            target_position = (row + 1, col + 1)
        elif direction == 's' and row + 1 < 5:
            target_position = (row + 1, col)
        elif direction == 'sw' and row + 1 < 5 and col - 1 > -1:
            target_position = (row + 1, col - 1)
        elif direction == 'w' and col - 1 > -1:
            target_position = (row, col - 1)
        elif direction == 'nw' and row - 1 > -1 and col - 1 > -1:
            target_position = (row - 1, col - 1)

        if target_position is None:
            return False

        return (
            not self.board.is_position_occupied(target_position)
            and self.board.get_building_level(*target_position) < 4
        )

    def get_possible_moves(self):
        """
        @brief Get a list of possible moves for the worker
        @return: A list of possible moves (directions) for the worker
        """
        valid_dir = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
        return [dir for dir in valid_dir if self.can_move_in_direction(dir)]

    def get_possible_builds(self):
        """
        @brief Get a list of possible build directions for the worker
        @return: A list of possible build directions for the worker
        """
        valid_dir = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
        return [dir for dir in valid_dir if self.can_build_in_direction(dir)]

    def move(self, direction):
            """
            @brief Moves specified worker according to Santorini rules
            @param worker_id representing the worker to be moved
            @param new_row representing the row of the new position
            @param new_col representing the column of the new position
            @return None
            """
            valid_dir = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
            if not any(self.can_move_in_direction(dir) for dir in valid_dir):
                raise TrappedWorker()
            
            row, col = self.position
            new_position = None
            
            if direction == 'n' and row - 1 > -1:
                new_position = (row - 1, col)
            elif direction == 'ne' and row - 1 > -1 and col + 1 < 5:
                new_position = (row - 1, col + 1)
            elif direction == 'e' and col + 1 < 5:
                new_position = (row, col + 1)
            elif direction == 'se' and row + 1 < 5 and col + 1 < 5:
                new_position = (row + 1, col + 1)
            elif direction == 's' and row + 1 < 5:
                new_position = (row + 1, col)
            elif direction == 'sw' and row + 1 < 5 and col - 1 > -1:
                new_position = (row + 1, col - 1)
            elif direction == 'w' and col - 1 > -1:
                new_position = (row, col - 1)
            elif direction == 'nw' and row - 1 > -1 and col -1 > -1:
                new_position = (row - 1, col - 1)
            else:
                raise MoveError(direction)
            
            if self.board.is_position_occupied(new_position):
                raise MoveError(direction)
            
            if self.board.get_building_level(*new_position) == 4:
                raise MoveError(direction)
            
            self.position = new_position
            self.board.update_worker_position(self.worker_id, self.position)

    def build(self, direction):
            """
            @brief Adds a level to the building at the given position.
            @param row representing row of the position to the building
            @param col representing column of the position to the building
            @return None
            """
            row, col = self.position
            target_position = None

            # Checking to see if build direction is a position within the board
            if direction == 'n' and row - 1 > -1:
                target_position = (row - 1, col)
            elif direction == 'ne' and row - 1 > -1 and col + 1 < 5:
                target_position = (row - 1, col + 1)
            elif direction == 'e' and col + 1 < 5:
                target_position = (row, col + 1)
            elif direction == 'se' and row + 1 < 5 and col + 1 < 5:
                target_position = (row + 1, col + 1)
            elif direction == 's' and row + 1 < 5:
                target_position = (row + 1, col)
            elif direction == 'sw' and row + 1 < 5 and col - 1 > -1:
                target_position = (row + 1, col - 1)
            elif direction == 'w' and col - 1 > -1:
                target_position = (row, col - 1)
            elif direction == 'nw' and row - 1 > -1 and col -1 > -1:
                target_position = (row - 1, col - 1)
            else:
                raise BuildError(direction)

            # Checking to see if position is occupied
            if self.board.is_position_occupied(target_position):
                raise BuildError(direction)

            # Checking to see if position is already level 4
            if self.board.get_building_level(*target_position) == 4:
                raise BuildError(direction)

            # Else build at the position
            self.board.grid[target_position[0]][target_position[1]] += 1
