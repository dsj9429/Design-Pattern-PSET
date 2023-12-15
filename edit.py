import copy
from board import Board

class Edit:
    
    def __init__(self):
        self.board_hist = []
        self._length = 0
        self._undo_counter = 0

    def record_move(self, game):
        """
        @brief: Creates a copy of the current board and worker positions
        @param game: an instance of Santorini
        @return: None
        """
        old_board = game.get_board()
        new_board = copy.deepcopy(old_board)
        self.board_hist.append((new_board, game.get_worker_positions()))
        self._length += 1
        self._undo_counter += 1

    def undo_move(self):
        """
        @brief: Undo a move and saves it to board_hist
        @param: None
        @return: A deepcopy of the previous board
        """
        if self._undo_counter > 1:
            self._undo_counter -= 1
            board, worker_positions = self.board_hist[self._undo_counter - 1]
            return copy.deepcopy((board, worker_positions))
        
        return copy.deepcopy(self.board_hist[0])

    def redo_move(self):
        """
        @brief: Redo a move and saves it to board_hist
        @param: None
        @Return: A deepcopy of the previous board
        """
        if self._undo_counter < self._length:
            self._undo_counter += 1
            board, worker_positions = self.board_hist[self._undo_counter - 1]
            return copy.deepcopy((board, worker_positions))

        return copy.deepcopy(self.board_hist[self._length - 1])

    def next_move(self):
        """
        @brief: Get's next move, deleting later items in the history
        @param: None
        @return: A deepcopy of the current board
        """
        del self.board_hist[self._undo_counter : self._length]
        self._length = self._undo_counter
        return copy.deepcopy(self.board_hist[self._length - 1])

    def get_move_num(self):
        """
        @brief: Returns the undo counter
        @param: None
        @return: Undo counter
        """
        return self._undo_counter