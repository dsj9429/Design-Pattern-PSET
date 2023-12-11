class Board:
    def __init__(self):
        """
        @brief Sets up the board with initial worker positions
        @param None
        @return None
        """
        self.grid = [[0 for _ in range(5)] for _ in range(5)]
        self.worker_positions = {'A': (3, 1), 'B': (1, 3),
                                 'Y': (1, 1), 'Z': (3, 3)}

    def move_worker(self, worker_id, new_row, new_col):
        """
        @brief Moves specified worker according to Santorini rules
        @param worker_id representing the worker to be moved
               new_row representing the row of the new position
               new_col representing the column of the new position
        @return None
        """
        self.worker_positions[worker_id] = (new_row, new_col)

    def get_building_level(self, row, col):
        """
        @brief Obtains the level of the given building
        @param row representing the row of position for the building
               col representing the column of the position for the building
        @return The level of the building being checked
        """
        return self.grid[row][col]

    def build(self, row, col):
        """
        @brief Adds a level to the building at the given position.
        @param row representing row of the position to the building
               col representing column of the position to the building
        @return None
        """
        self.grid[row][col] += 1

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
                    worker_id = [k for k, v in self.worker_positions.items() if v == (row, col)][0]
                    print(f"{self.grid[row][col]}{worker_id}", end="")
                else:
                    print(f"{self.grid[row][col]}", end=" ")

                print("|", end="")

            print("\n" + "+--+--+--+--+--+")
