class Board:
    def __init__(self, worker_positions):
        """
        @brief Sets up the board, sets initial worker positions, hold the amount
               of building levels still available for each block
        @param None
        @return None
        """
        self.grid = [[0 for _ in range(5)] for _ in range(5)]
        self.worker_positions = worker_positions

    def get_building_level(self, row, col):
        """
        @brief Obtains the level of the given building
        @param row representing the row of position for the building
        @param col representing the column of the position for the building
        @return The level of the building being checked
        """
        return self.grid[row][col]

    def display_board(self):
        """
        @brief Displays the board.
        @param None
        @return None
        """
        print("+--+--+--+--+--+")
        for row in range(5):
            print("|", end="")
            for col in range(5):
                if (row, col) in self.worker_positions.values():
                    # Prints out worker_id for each worker
                    worker_id = [k for k, v in self.worker_positions.items() if v == (row, col)][0]
                    print(f"{self.grid[row][col]}{worker_id}", end="")
                else:
                    # Prints out blankspace if there is not a worker here
                    print(f"{self.grid[row][col]}", end=" ")

                print("|", end="")

            print("\n" + "+--+--+--+--+--+")
    
    def update_worker_position(self, worker_id, new_position):
        """
        @brief Updates the position of the worker on the board
        @param worker_id: ID of the worker to be updated
        @param new_position: The new position/building of the worker
        @return: None
        """
        self.worker_positions[worker_id] = new_position
    
    def is_position_occupied(self, position):
        """
        @brief Check if a position on board is occupiede by a worker
        @param position: The position being checked
        @return: True if the position is occupied, false otherwise
        """
        return position in self.worker_positions.values()

    def get_height(self, position):
        """
        @brief Obtains the height of the given cell
        @param row: The row of the cell
        @param col: The column of the cell
        @return: The height of the cell
        """
        row, col = position
        return self.grid[row][col]

    def get_distance(self, position1, position2):
        """
        @brief Calculates the Manhattan distance between two positions on the board
        @param position1: The first position (row, col)
        @param position2: The second position (row, col)
        @return: The Manhattan distance between the two positions
        """
        row1, col1 = position1
        row2, col2 = position2
        return abs(row1 - row2) + abs(col1 - col2)
    