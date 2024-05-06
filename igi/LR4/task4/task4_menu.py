from task4.triangle import Triangle
from checking.intchecking import IntChecking

def Menu4():
    '''Task 4 menu'''
    print("Enter Radius value for circle: ")
    radius = input() #add checking
    while not IntChecking(radius):
        print("Enter int value ")
        radius = input()
    radius = int(radius)
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