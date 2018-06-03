class Card(object):

    """Represent a single card drawn from a 52-card deck (without jokers)

    Attributes:
        suit: Spade, Heart, Diamond, Club
        number: 2 to 10, J = 11, Q = 12, K = 13, A = 14
        id: C2 = 0, C3 = 1, ... SA = 51
    """

    def __init__(self, id=None, suit='C', number=2):
        if id:
            self.id = id
            self.suit = 'C'
            self.number = 2
        else:
            self.suit = suit
            self.number = number
            self.id = 0