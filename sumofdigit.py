number=int(input("Enter a number"))
temp_num=number
sum_of_digits=0

while(temp_num>0):
    digit=temp_num%10
    sum_of_digits=sum_of_digits+digit
    ts=sum_of_digits+digit
    temp_num//=10
print("The sum is",sum_of_digits)