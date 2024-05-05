from task1.mixin import PrintableMixin

class Student(PrintableMixin):
    def __init__(self, name, birth_day, birth_month, birth_year):
        self.name = name
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year

    def __str__(self): #magic method
        return self.name
