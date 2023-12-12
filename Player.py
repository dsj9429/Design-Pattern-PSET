from worker import Worker

class Player:
    def __init__(self, player_id, workers):
        """
        @brief Makes a player with given ID
        @param player_id: ID for the given player.
        @param workers: A dictionary containing player's workers their positions
        @return: None
        """
        self.player_id = player_id
        self.workers = workers

    def undo:
        """
        @brief Undo a turn and returns state to the last round.
        @return: None
        """
        pass
    
    def redo:
        """
        @brief Redo a turn and changes state to the next round.
        @return: None
        """
        pass

class HumanPlayer(Player):
    def make_move(self, worker_id, move_direction, build_direction):
        """
        @brief Objects for real players to move and build
        @param worker_id: ID of the worker to move/build
        @param move_direction: Direction to move the worker
        @param build_direction: Direction to build a level
        @return: None
        """
        pass

class HeuristicPlayer(Player):
    def make_move(self):
        """
        @brief Implements the heuristic player
        @return: None
        """
        pass

class RandomPlayer(Player):
    def make_move(self):
        """
        @brief Implements the Random moves player
        @return: None
        """
        pass