from task3.taylor import Taylor
import statistics

class AdditionalParametres(Taylor):        

    def CalculateArithmeticMean(self):
        '''Calculating mean value'''
        return statistics.mean(self.sequence)
    
    def CalculateMedian(self):
        '''Calculating median value'''
        return statistics.median(self.sequence)
    
    def CalculateMode(self):
        '''Calculating mode value'''
        return statistics.mode(self.sequence)
    
    def CalculateVariance(self):
        '''Calculating variance value'''
        return statistics.variance(self.sequence)
    
    def CalculateStandartDeviation(self):
        '''Calculating standart deviation value'''
        return statistics.stdev(self.sequence)
        