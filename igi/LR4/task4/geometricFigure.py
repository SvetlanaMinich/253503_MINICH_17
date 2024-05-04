from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    @abstractmethod
    def CalculateS(self):
        pass 