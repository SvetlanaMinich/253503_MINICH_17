from task3.taylor import Taylor
import statistics

class AdditionalParametres(Taylor):        

    def CalculateArithmeticMean(self):
        return statistics.mean(self.sequence)
    
    def CalculateMedian(self):
        return statistics.median(self.sequence)
    
    def CalculateMode(self):
        return statistics.mode(self.sequence)
    
    def CalculateVariance(self):
        return statistics.variance(self.sequence)
    
    def CalculateStandartDeviation(self):
        return statistics.stdev(self.sequence)
        