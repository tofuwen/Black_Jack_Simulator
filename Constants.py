class Constants:

    NUM_CARD_IN_SUIT = 13
    NUM_SUIT = 4

    def __setattr__(self, attr, value):
        if hasattr(self, attr):
            raise(ValueError, 'Attribute %s already has a value and so cannot be written to' % attr)
        self.__dict__[attr] = value
