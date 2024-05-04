from task5.NumPyService import NumPyService

def Menu5():
    print("Enter number of rows: ")
    rows = int(input()) #int checker
    print("Enter number of columns: ")
    columns = int(input()) #int checker
    npService = NumPyService(rows, columns)
    npService.GenerateMatrix()
    matrix = npService.GetMatrix()
    print("Matrix: ")
    print(matrix)
    print("Number of elements above mean: {}".format(npService.CountElementsAboveMean()))
    std_deviation1, std_deviation2 = npService.CalculateStandartDeviation()
    print("Standart deviation by numpy std: ", round(std_deviation1, 2))
    print("My standart deviation: ", round(std_deviation2, 2))
