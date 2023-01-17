"""
    Create a player with a name and surname which are coming from GUI.
"""
class Player:
    def __init__(self):
        """
            Create a player list
        :return: None
        """
        self.players = []

    def add_player(self,ns):
        """
            Append ns to list created in upper function.
        :param : ns
        :return : None
        """
        self.players.append(ns)

    