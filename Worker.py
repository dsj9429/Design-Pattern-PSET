from board import Board

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

    def move(self, direction):
            """
            @brief Moves specified worker according to Santorini rules
            @param worker_id representing the worker to be moved
            @param new_row representing the row of the new position
            @param new_col representing the column of the new position
            @return None
            """
            valid_directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
            
            if direction not in valid_directions:
                raise ValueError("Not a valid direction")

            row, col = self.position
            
            if direction == 'n' and row - 1 > -1:
                self.position = (row - 1, col)
            elif direction == 'ne' and row - 1 > -1 and col + 1 < 5:
                self.position = (row - 1, col + 1)
            elif direction == 'e' and col + 1 < 5:
                self.position = (row, col + 1)
            elif direction == 'se' and row + 1 < 5 and col + 1 < 5:
                self.position = (row + 1, col + 1)
            elif direction == 's' and row + 1 < 5:
                self.position = (row + 1, col)
            elif direction == 'sw' and row + 1 < 5 and col - 1 > -1:
                self.position = (row + 1, col - 1)
            elif direction == 'w' and col - 1 > -1:
                self.position = (row, col - 1)
            elif direction == 'nw' and row - 1 > -1 and col -1 > -1:
                self.position = (row - 1, col - 1)
            else:
                raise ValueError(f"Cannot move {direction}")

    def build(self, direction):
            """
            @brief Adds a level to the building at the given position.
            @param row representing row of the position to the building
            @param col representing column of the position to the building
            @return None
            """
            valid_directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
            
            if direction not in valid_directions:
                raise ValueError("Not a valid direction")

            row, col = self.position
            
            if direction == 'n' and row - 1 > -1:
                self.board.grid[row - 1][col] += 1
            elif direction == 'ne' and row - 1 > -1 and col + 1 < 5:
                self.board.grid[row - 1][col + 1] += 1
            elif direction == 'e' and col + 1 < 5:
                self.board.grid[row][col + 1] += 1
            elif direction == 'se' and row + 1 < 5 and col + 1 < 5:
                self.board.grid[row + 1][col + 1] += 1
            elif direction == 's' and row + 1 < 5:
                self.board.grid[row + 1][col] += 1
            elif direction == 'sw' and row + 1 < 5 and col - 1 > -1:
                self.board.grid[row + 1][col - 1] += 1
            elif direction == 'w' and col - 1 > -1:
                self.board.grid[row][col - 1] += 1
            elif direction == 'nw' and row - 1 > -1 and col -1 > -1:
                self.board.grid[row - 1][col - 1] += 1
            else:
                raise ValueError(f"Cannot build {direction}")
