"""Enumerates all the user-defined or customized exception classes."""

class InvalidWorker(Exception):
    """Returns an error if user enters invalid worker name."""
    pass


class OpponentPiece(Exception):
    """Returns an error when an opponent's piece is selected."""
    pass


class InvalidDirError(Exception):
    """Returns an error if user enters an invalid direction."""
    pass


class MoveError(Exception):
    """
    Returns an error with the direction if user moves to a direction on an
    occupied space or is outside the board.
    """

    def __init__(self, direction):
        self.direction = direction


class BuildError(Exception):
    """
    Returns an error with the direction if user builds on a direction on an
    occupied space, has 4 levels already, or is outside the board.
    """
    def __init__(self, direction):
        self.direction = direction

class TrappedWorker(Exception):
    """
    Returns an error if this specific worker cannot move but other worker can.
    """
    pass