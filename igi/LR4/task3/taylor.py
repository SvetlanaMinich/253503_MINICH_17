import math

class Taylor:
    def __init__(self):
        self.sequence = []

    def calculate(self, x, eps):
        result = 0.0
        for i in range(500):
            fact = 1
            for mult in range(1, 2*i + 1):
                fact *= mult
            buf = ((-1)**i) * (x**(2*i)) / fact
            self.sequence.append(buf)
            result += buf
            if math.fabs(buf) <= eps:
                print(f"x = {x}, n = {i}, F(x) = {result}, Math F(x) = {round(math.cos(x), 2)}, eps = {eps}")
                return result
        return 0