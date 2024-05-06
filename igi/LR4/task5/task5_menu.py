from task5.NumPyService import NumPyService
from checking.intchecking import IntChecking

def Menu5():
    '''Task 5 menu'''
    print("Enter number of rows: ")
    rows = input()
    while not IntChecking(rows):
        print("Enter number of rows: ")
        rows = input()
    rows = int(rows)
    print("Enter number of columns: ")
    columns = input()
    while not IntChecking(columns):
        print("Enter number of columnss: ")
        columns = input()
    columns = int(columns)
    npService = NumPyService(rows, columns)
    npService.GenerateMatrix()
    matrix = npService.GetMatrix()
    print("Matrix: ")
    print(matrix)
    print("Number of elements above mean: {}".format(npService.CountElementsAboveMean()))
    std_deviation1, std_deviation2 = npService.CalculateStandartDeviation()
    print("Standart deviation by numpy std: ", round(std_deviation1, 2))
    print("My standart deviation: ", round(std_deviation2, 2))
