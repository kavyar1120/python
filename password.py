password=input("enter password:")

has_upper= False
has_lower= False
has_digit= False
has_special= False
special_characters="@#$%^&*()-_+"

for char in password:
    if char.isupper():
        has_upper=True
    elif char.islower():
        has_lower=True
    elif char.isdigit():
        has_digit=True
    elif char in special_characters:
        has_special=True
if len(password)<8:
    print("weak:password must be at least 8 characters")
elif not has_upper:
    print("weak: Missing an uppercase letter")
elif not has_lower:
    print("weak: Missing an lowercase letter")
elif not has_digit:
    print("weak: Missing a number")
elif not has_special:
    print("weak: Missing a special character")
else:
    print("strong:password meets all security requirements")
