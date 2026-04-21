rev=0
temp=0
num=int(input("enter the number"))
while num>0:
    temp=num%10
    rev=rev*10+temp
    num=num//10
print(rev)