class FigureColour:
    def __init__(self, colour = "black"):
        self.__colour = colour

    @property
    def colour(self):
        return self.__colour
    
    @colour.setter
    def set_colour(self, colour):
        self.__colour = colour