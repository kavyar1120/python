from datetime import  date
today=date.today()
month=today.month
if month in (2,3,4,5):
    print("summer")
elif month in(6,7,8,9):
    print("rainy")
else:
    print("winter")




