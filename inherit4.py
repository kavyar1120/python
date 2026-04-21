class dept:
    def showdepartment():
        print("CS dept")
class student:
    def showname():
        print("Indu")
class exam(dept,student):
    def examname():
        print("Python")

e1=exam
e1.showdepartment()
e1.showname()
e1.examname()