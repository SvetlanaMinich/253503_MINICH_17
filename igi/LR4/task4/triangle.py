from task4.geometricFigure import GeometricFigure
from task4.colour import FigureColour
import matplotlib.pyplot as plt
import numpy as np
import math

#equilateral one
class Triangle(GeometricFigure):
    __name = "Triangle"

    def __init__(self, radius, colour):
        self.__radius = radius
        self.__colour = FigureColour(colour)

    def GetName(self):
        return self.__name

    def CalculateS(self):
        return (self.__radius ** 2) * 3 * math.sqrt(3) / 4
    
    def CalculateA(self):
        return self.__radius * math.sqrt(3)
    
    def GetInfo(self):
        return "Figure triangle: \nSide: {}\nColour: {}\nArea: {}".format(self.CalculateA(), self.__colour.colour, self.CalculateS())
    
    def DrawTriangle(self):
        circle = plt.Circle((0,0), self.__radius, color = self.__colour.colour, fill = False)
        plt.gca().add_patch(circle)
        angles = np.linspace(0, 2 * np.pi, 4)
        x = self.__radius * np.cos(angles)
        y = self.__radius * np.sin(angles)
        plt.plot(x, y, self.__colour.colour)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(self.GetInfo())
        plt.grid(True)
        plt.savefig('figure.png')
        plt.show()
        