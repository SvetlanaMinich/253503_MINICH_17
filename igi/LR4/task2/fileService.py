import zipfile

class FileService:
    def __init__(self):
        self.text_file_path = "task2/task2_text.txt"
        self.result_file_path = "task2/task2_result.txt"
        self.zip_path = "task2/MyArchive.zip"

    def GetTextFromFile(self):
        with open(self.text_file_path, "r") as file:
            text = file.read()
        return text
    
    def WriteInfoToResultFile(self, str_to_write):
        with open(self.result_file_path, "a") as file:
            file.write(str_to_write + '\n')

    def CreateResultZipArchive(self):
        with zipfile.ZipFile(self.zip_path,"w") as myarchive:
            myarchive.write(self.result_file_path)

    def CheckInfoAboutZipArchive(self):
        with zipfile.ZipFile(self.zip_path, "r") as myarchive:
            file_info = myarchive.getinfo("task2_result.txt")
        return file_info