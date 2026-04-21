a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a+b>c and b+c>a and c+a>b:
      if a==b==c:
            print("equilateral")
      elif a==b or a==c or b==c:
            print("isosceles")
      else:
            print("scalene")
else:
    print("illegal")

