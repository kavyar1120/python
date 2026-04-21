class solve:
    def product(a,b):
        print(a*b)
    def si(p,t,r):
        si=p*t*r//100
        print(si)
    def big(a,b):
        if a>b:
            print(a)
        else:
            print(b)
    def area(pi,r):
        area=pi*r*r
        print(area)
s1=solve
a=int(input("enter first number"))
b=int(input("enter second number"))
s1.product(a,b)
p=int(input("enter price"))
t=int(input("enter time"))
r=int(input("enter rate of interest"))
s1.si(p,t,r)
s1.big(4,5)
s1.area(3.14,5)
