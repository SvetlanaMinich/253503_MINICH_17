from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    __name = " " #static attribute
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def CalculateS(self):
        pass 