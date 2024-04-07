import math

def calculate(x, eps):
    for i in range(500):
        fact = 1
        for mult in range(1, 2*i + 1):
            fact *= mult
        buf = ((-1)**i) * (x**(2*i)) / fact
        result += buf
        if math.fabs(buf) <= eps:
            print(f"x = {x}, n = {i}, F(x) = {result}, Math F(x) = {round(math.cos(x), 2)}, eps = {eps}")
            return i
    return 0

def task_1():
    x = None
    eps = None
    result = 0.0
    while True:
        x = input("Enter x: ")
        try:
            x = float(x)
            eps = input("Enter eps: ")
            try:
                eps = float(eps)
                break
            except:
                print("ERROR, Enter float eps.")
        except:
            print("ERROR, Enter float x.")
    calculate(x, eps)