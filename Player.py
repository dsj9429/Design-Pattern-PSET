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

class HeuristicPlayer(Player):
    def make_move(self):
        """
        @brief Implements the heuristic player
        @return: None
        """
        self.save_state()

class RandomPlayer(Player):
    def make_move(self):
        valid_dir = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
        
        # Chooses a random worker of this player
        worker_id = random.choice(list(self.workers.keys()))

        # Keeps choosing move and build direction as long as it's invalid
        while True:
            # Choose the move and build direction
            move_direction = random.choice(valid_dir)
            build_direction = random.choice(valid_dir)

            # If the move and build is valid, break the loop
            if (
                self.workers[worker_id].can_move_in_direction(move_direction)
                and self.workers[worker_id].can_build_in_direction(build_direction)
            ):
                break
        self.save_state()
        self.workers[worker_id].move(move_direction)
        self.workers[worker_id].build(build_direction)

        print(f"{worker_id},{move_direction},{build_direction}")