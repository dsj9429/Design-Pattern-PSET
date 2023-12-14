import random

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

    def calculate_height_score(self, board):
        """
        @brief Calculates sum of heights for a player's workers
        @param board: Current board of the game
        @return: An integer for the height_score
        """
        height_score = sum(board.get_height(worker.position)
                           for worker in self.workers.values())
        return height_score

    def calculate_distance_score(self, board, opponent_workers):
        distance_score = 8 - sum(
            min(board.get_distance(worker.position, opponent.position)
                for opponent in opponent_workers)
            for worker in self.workers.values()
            )
        return distance_score

    def calculate_center_score(self):
        center_values = {
            (0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 0,
            (1, 0): 0, (1, 1): 1, (1, 2): 1, (1, 3): 1, (1, 4): 0,
            (2, 0): 0, (2, 1): 1, (2, 2): 2, (2, 3): 1, (2, 4): 0,
            (3, 0): 0, (3, 1): 1, (3, 2): 1, (3, 3): 1, (3, 4): 0,
            (4, 0): 0, (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0
        }

        center_score = sum(center_values[worker.position]
                           for worker in self.workers.values())
        return center_score

    def calculate_score(self, opponent_workers):
        """
        @brief Calculates score based on heuristics described on the spec
        @param: move: A tuple representing the move (worker_id, move_direction,
                      build_direction)
        @return: An integer showing the total of 3 * height_score,
                 2 * center_score, and 1 * distance_score
        """
        board = list(self.workers.values())[0].board

        height_score = self.calculate_height_score(board)
        center_score = self.calculate_center_score()
        distance_score = self.calculate_distance_score(board, opponent_workers)

        return (height_score, center_score, distance_score)

    def display_move(self, worker_id, move_direction, build_direction,
                     score_flag, opponent_workers):
        score = self.calculate_score(opponent_workers)

        if score_flag:
            print(f"{worker_id},{move_direction},{build_direction} {score}")
        else:
            print(f"{worker_id},{move_direction},{build_direction}")

class HumanPlayer(Player):
    def make_move(self):
        """
        @brief Implement human player
        @return: None
        """
        pass

class HeuristicPlayer(Player):
    def get_available_moves(self):
        """
        @brief Get all available moves for the player
        @return: A list of available moves, where each move is a tuple
                (worker_id, move_direction, build_direction)
        """
        available_moves = []

        for worker_id, worker in self.workers.items():
            for move_direction in worker.get_possible_moves():
                move = (worker_id, move_direction)
                available_moves.append(move)

        return available_moves

    def make_move(self, score_flag, opponent_workers):
        """
        @brief Implements the heuristic player move maker
        @param: None
        @return: None
        """
        available_moves = self.get_available_moves()

        if not available_moves:
            return

        best_move = None
        best_score = float('-inf')

        for move in available_moves:
            worker_id, move_direction = move
            
            if not self.workers[worker_id].can_move_in_direction(move_direction):
                continue

            # Calculate move scores for each move
            c1, c2, c3 = 3, 2, 1
            height, center, distance = self.calculate_score(opponent_workers)
            move_score = c1 * height + c2 * center + c3 * distance

            # Update the best possible move
            if move_score > best_score:
                best_move = move
                best_score = move_score

        if best_move:
            worker_id, move_direction = best_move
        
            try:
                self.workers[worker_id].move(move_direction)
            except Exception as e:
                pass

            valid_dir = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']

            while True:
                build_direction = random.choice(valid_dir)

                try:
                    self.workers[worker_id].can_build_in_direction(build_direction)
                    self.workers[worker_id].build(build_direction)
                    break
                except Exception:
                    pass

        self.display_move(worker_id, move_direction, build_direction,
                          score_flag, opponent_workers)

class RandomPlayer(Player):
    def make_move(self, score_flag, opponent_workers):
        """
        @brief: An iteration of the move for a random ai player
        @param: None
        @return: None
        """
        valid_dir = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
        workers = self.workers
        
        # Chooses a random worker of this player
        worker_id = random.choice(list(workers.keys()))

        move_direction = None
        build_direction = None

        # Keeps choosing move and build direction as long as it's invalid
        while True:
            # Choose the move and build direction
            move_direction = random.choice(valid_dir)

            # If the move and build is valid, break the loop
            try:
                workers[worker_id].can_move_in_direction(move_direction)
                workers[worker_id].move(move_direction)

                build_direction = random.choice(valid_dir)

                try:
                    workers[worker_id].can_build_in_direction(build_direction)
                    workers[worker_id].build(build_direction)
                    break
                except Exception:
                    pass
            except Exception:
                pass

        self.display_move(worker_id, move_direction, build_direction,
                          score_flag, opponent_workers)