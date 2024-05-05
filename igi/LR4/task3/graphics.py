from task3.taylor import Taylor
import matplotlib.pyplot as plt
import numpy as np
import math

class Graphic:
    def __init__(self):
        self.MathF = []
        self.F = []
        
    def MakeGraphic(self):
        '''Making graphics with cos(x) and taylor's cos, saving in to task3/graph.png'''
        x = np.arange(-1, 1, 0.01)
        taylor = Taylor()
        for i in x:
            self.MathF.append(taylor.calculate(i, 0.01))
            self.F.append(math.cos(i))
        plt.plot(x, self.MathF, label='Approximation')
        plt.plot(x, self.F, label='math.cos(x)')  
        plt.xlabel('x')
        plt.ylabel('F(x)')
        plt.legend()
        plt.title('Approximation of math.cos(x)')
        plt.text(0,0.6,'Example Text')
        plt.annotate('Example Annotation', xy=(0, 0.7))
        plt.savefig('task3/graph.png')  