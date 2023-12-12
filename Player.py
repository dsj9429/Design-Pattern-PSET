from worker import Worker

class Player:
    def __init__(self, player_id, workers):
        """
        @brief Makes a player with given ID
        @param player_id: ID for the given player.
        @param workers: A dictionary containing player's workers and positions
        @return: None
        """
        self.player_id = player_id
        self.workers = workers
        self.turn_stack = []
        self.redo_stack = []

    def save_state(self):
        """
        @brief Saves the current state to the turn stack.
        @return: None
        """
        self.turn_stack.append(self.workers.copy())
    
    def undo(self):
        """
        @brief Undo a turn and returns state to the last round.
        @return: None
        """
        if len(self.turn_stack) > 1:
            self.redo_stack.append(self.turn_stack.pop())
            self.workers = self.turn_stack[-1]

    def redo(self):
        """
        @brief Redo a turn and changes state to the next round.
        @return: None
        """
        if self.redo_stack:
            self.turn_stack.append(self.redo_stack.pop())
            self.workers = self.turn_stack[-1]

class HumanPlayer(Player):
    def make_move(self, worker_id, move_direction, build_direction):
        """
        @brief Objects for real players to move and build
        @param worker_id: ID of the worker to move/build
        @param move_direction: Direction to move the worker
        @param build_direction: Direction to build a level
        @return: None
        """
        self.save_state()

class HeuristicPlayer(Player):
    def make_move(self):
        """
        @brief Implements the heuristic player
        @return: None
        """
        self.save_state()

class RandomPlayer(Player):
    def make_move(self):
        """
        @brief Implements the Random moves player
        @return: None
        """
        self.save_state()