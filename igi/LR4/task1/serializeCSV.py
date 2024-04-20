from task1.serializer import Serializer
from task1.student import Student
import csv

class SerializeCSV(Serializer):
    def SaveToFile(self):
        with open("task1.csv","w",newline="") as file:
            columns = ["name", "birth_day", "birth_month", "birth_year"]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerows(self.students)
    
    def LoadFromFile(self):
        students_result = []
        with open("task1.csv","r",newline="") as file:
            reader = csv.DictReader(file, fieldnames=["name", "birth_day", "birth_month", "birth_year"])
            for row in reader:
                student = Student(row["name"], row["birth_day"], row["birth_month"], row["birth_year"])
                students_result.append({"name" : student.name, 
                                        "birth_day" : student.birth_day,
                                        "birth_month" : student.birth_month,
                                        "birth_year" : student.birth_year})
        return students_result
