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
        self.dome_amt = 18
        self.level1_amt = 22
        self.level2_amt = 18
        self.level3_amt = 14

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
                    worker_id = [k for k, v in self.worker_positions.items() if v == (row, col)][0]
                    print(f"{self.grid[row][col]}{worker_id}", end="")
                else:
                    print(f"{self.grid[row][col]}", end=" ")

                print("|", end="")

            print("\n" + "+--+--+--+--+--+")
            
def main():  
    game_board = Board()
    game_board.display_board()

if __name__ == "__main__":
    main()
