temp2=0
rev=0
temp=0
num=int(input("enter the number"))
temp2=num
while(num>0):
    temp=num%10
    rev=rev*10+temp
    num=num//10
print(rev)
if (temp2==rev):
    print("palindrome")
else:
    print("not palindrome")
