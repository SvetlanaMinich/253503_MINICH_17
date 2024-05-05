class FigureColour:
    def __init__(self, colour = "black"):
        self.__colour = colour

    @property
    def colour(self):
        '''Colour property'''
        return self.__colour
    
    @colour.setter
    def set_colour(self, colour):
        '''Colour setter'''
        self.__colour = colour