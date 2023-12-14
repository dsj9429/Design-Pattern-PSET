import copy
from board import Board

class Edit:
    
    def __init__(self):
        self.board_hist = []
        self._length = 0
        self._undo_counter = 0

    def record_move(self, game):
        old_board = game.get_board()
        new_board = copy.deepcopy(old_board)
        self.board_hist.append(new_board)
        self._length += 1
        self._undo_counter += 1

    def undo_move(self):
        if self._undo_counter > 1:
            self._undo_counter -= 1
            return copy.deepcopy(self.board_hist[self._undo_counter - 1])

        return copy.deepcopy(self.board_hist[0])

    def redo_move(self):
        if self._undo_counter != self._length:
            self._undo_counter += 1
            return copy.deepcopy(self.board_hist[self._undo_counter - 1])

        return copy.deepcopy(self.board_hist[self._length - 1])

    def next_move(self):
        del self.board_hist[self._undo_counter : self._length]
        self._length = self._undo_counter
        return copy.deepcopy(self.board_hist[self._length - 1])

    def get_move_num(self):
        return self._undo_counter