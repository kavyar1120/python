weight=float(input("enter your weight in kg:"))
height=float(input("enter your height in meters:"))

bmi=weight/(height**2)

print("your bmi is:",bmi)

if bmi<18.5:
    print("you are underweight")
elif bmi>=18.5 and bmi<25:
    print("you are normal weight")
elif bmi>=25 and bmi<30:
    print("you are overweight")
else:
    print("you are obese")