from task1.serializer import Serializer
import pickle

class SerializePickle(Serializer):
    def SaveToFile(self):
        with open("task1.pickle","wb") as file:
            pickle.dump(self.students, file)
    
    def LoadFromFile(self):
        with open("task1.pickle","rb") as file:
            students_from_file = pickle.load(file)
        return  students_from_file 