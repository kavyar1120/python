class dept:
    def showdepartment():
        print("CS dept")

class student(dept):
    def showstudent():
        print("BCA")

class exam(student):
    def java():
        print("IA test")

e1=exam
e1.showdepartment()
e1.showstudent()
e1.java()
