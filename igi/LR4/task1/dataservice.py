from operator import itemgetter

class DataService:
    def SortData(self, students_list):
        '''Sorting list by name'''
        return sorted(students_list, key=itemgetter('name'))
    
    def SearchStudentByMonth(self, students_list, _month):
        '''Search student in list by birth month'''
        students_result = []
        for student in students_list:
            if student["birth_month"] == _month:
                students_result.append(student)
        return students_result