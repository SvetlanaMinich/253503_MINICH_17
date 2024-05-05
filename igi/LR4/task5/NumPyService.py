import numpy as np
import random

class NumPyService:
    def __init__(self,rows,columns):
        self.__rows = rows
        self.__columns = columns
        self.__matrix = np.zeros(rows*columns)

    def GenerateMatrix(self):
        '''Generating matrix with random'''
        self.__matrix = np.random.randint(0, 10, size=(self.__rows, self.__columns))

    def GetMatrix(self):
        '''Getting matrix'''
        return self.__matrix
    
    def CountElementsAboveMean(self):
        '''Counting matrix elements above mean one'''
        mean = np.mean(self.__matrix)
        count = np.sum(self.__matrix > mean)
        return count
    
    def CalculateStandartDeviation(self):
        '''Two types calculating standart deviation'''
        std_dev1 = np.std(self.__matrix)
        mean_value = np.mean(self.__matrix)
        deviations = self.__matrix - mean_value
        squared_deviations = deviations ** 2
        variance = np.mean(squared_deviations)
        std_dev2 = np.sqrt(variance)
        return std_dev1, std_dev2