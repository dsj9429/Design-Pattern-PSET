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
    """Returns an error with the direction if user moves to a direction on an occupied space."""

    def __init__(self, direction):
        self.direction = direction


class BuildError(Exception):
    def __init__(self, direction):
        self.direction = direction