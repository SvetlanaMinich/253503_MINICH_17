from task3.graphics import Graphic
from task3.adittionalParam import AdditionalParametres

def Menu3():
    print("Additional parametres: ")
    param = AdditionalParametres()
    param.calculate(20, 0.001)
    mean = param.CalculateArithmeticMean()
    median = param.CalculateMedian()
    mode = param.CalculateMode()
    variance = param.CalculateVariance()
    deviation = param.CalculateStandartDeviation()
    print(f"Arithmetic mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standart deviation: {deviation}")
    graphic = Graphic()
    graphic.MakeGraphic()
