m1=int(input("enter your marks:"))

def marks(m1):
    if (m1 >= 35 and m1 < 50):
        print("pass")
    elif (m1 >= 50 and m1 < 60):
        print("second class")
    elif (m1 >= 60 and m1 < 70):
        print("first class")
    elif (m1 >= 70 and m1 < 100):
        print("Distinction")
    else:
        print("fail")

marks(m1)