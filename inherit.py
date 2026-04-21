class dept:
    def show():
        print("from department")
class staff(dept):
    def display():
        print("from staff")

d1=dept
d1.show()
d2=staff
d2.show()
d2.display()
