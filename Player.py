class Player(object):

    """Represent a player

    Attributes:
        cards: cards that the player is holding
        chips: chips that the player is holding
    """

    def __init__(self, chips):
        self.cards = []
        self.chips = chips
