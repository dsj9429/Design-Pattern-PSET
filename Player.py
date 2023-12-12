class Player:
    def __init__(self, player_id, workers):
        """
        @brief Makes a player with given ID
        @param player_id: ID for the given player.
        @return: None
        """
        self.player_id = player_id
        self.workers = workers