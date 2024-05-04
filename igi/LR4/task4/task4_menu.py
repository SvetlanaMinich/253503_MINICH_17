from task4.triangle import Triangle
from task4.colour import FigureColour

def Menu4():
    print("Enter Radius value for circle: ")
    radius = int(input()) #add checking
    print("Enter color letter (R - red, Y - yellow, G - green): ")
    colour = input()
    if colour != "R" and colour != "Y" and colour != "G":
        colour = "black"
    elif colour == "R":
        colour = "red"
    elif colour == "Y":
        colour = "yellow"
    else:
        colour = "green"
    figure = Triangle(radius, colour)
    figure.DrawTriangle()