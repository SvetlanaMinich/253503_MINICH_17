from operator import itemgetter

class DataService:
    def SortData(self, students_list):
        return sorted(students_list, key=itemgetter('name'))
    
    def SearchStudentByMonth(self, students_list, _month):
        students_result = []
        for student in students_list:
            if student["birth_month"] == _month:
                students_result.append(student)
        return students_result