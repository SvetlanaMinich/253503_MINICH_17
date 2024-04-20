from task1.student import Student
from task1.serializeCSV import SerializeCSV
from task1.serializePickle import SerializePickle
from task1.dataservice import DataService

def Menu1():
    students = []
    students_num = input("Number of students: ")
    students_num = int(students_num)
    for i in range(students_num):
        name = input(f"Enter name of {i} student: ")
        day = input(f"Enter day of {i} student's birthday: ")
        month = input(f"Enter month of {i} student's birthday: ")
        year = input(f"Enter year of {i} student's birthday: ")
        stud = Student(name, day, month, year)
        students.append({"name" : stud.name, 
                       "birth_day" : stud.birth_day,
                       "birth_month" : stud.birth_month,
                       "birth_year" : stud.birth_year})       
    print("Writing students to .pickle file")
    serPickle = SerializePickle(students=students)
    serPickle.SaveToFile()
    print("Saved to pickle")
    print("Writing to .csv file")
    serCSV = SerializeCSV(students=students)
    serCSV.SaveToFile()
    print("Saved to csv")
    print("Reading from .pickle start:")
    students_reading = serPickle.LoadFromFile()
    for stud in students_reading:
        print(stud["name"])
    print("reading from .pickle end")
    print("Reading from .csv start:")
    students_reading = serCSV.LoadFromFile()
    for stud in students_reading:
        print(stud["name"])
    print("Reading from .csv file end")
    print("Sorted students by name:")
    dataService = DataService()
    students_sorted = dataService.SortData(students)
    for stud in students_sorted:
        print(stud["name"])
    searched_month = input("Enter month to search student: ")
    stud_by_month = dataService.SearchStudentByMonth(students, searched_month)
    for stud in stud_by_month:
        print(stud["name"])
