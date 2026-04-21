class dept:
    def showdepartment():
        print("CS dept")
class student(dept):
    def showstudent():
        print("BCA")
class staff(dept):
    def stafname():
        print("Guru")

s1=student
s1.showdepartment()
s1.showstudent()
s2=staff
s2.showdepartment()
s2.stafname()
