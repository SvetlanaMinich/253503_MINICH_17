from task4.geometricFigure import GeometricFigure
from task4.colour import FigureColour
import matplotlib.pyplot as plt
import numpy as np
import math

#equilateral one
class Triangle(GeometricFigure):

    def __init__(self, radius, colour): 
        self.__radius = radius #dynamic attribute
        self.__colour = FigureColour(colour)
        super().__init__("Triangle")

    def __str__(self): #magic method
        return super().__name

    @property
    def radius(self):
        '''Radius property'''
        return self.__radius
    
    @radius.getter
    def get_radius(self):
        '''Radius getter'''
        return self.__radius

    def CalculateS(self):
        '''Calculating area'''
        return (self.__radius ** 2) * 3 * math.sqrt(3) / 4
    
    def CalculateA(self):
        '''Calculating triangle side'''
        return self.__radius * math.sqrt(3)
    
    def GetInfo(self):
        '''Getting info about figure'''
        return "Figure triangle: \nSide: {}\nColour: {}\nArea: {}".format(self.CalculateA(), self.__colour.colour, self.CalculateS())
    
    def DrawTriangle(self):
        '''Drawing triangle'''
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
        