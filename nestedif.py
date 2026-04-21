age=int(input("enter your age"))
if age>=18:
    print("you are an adult")
    if age>=65:
        print("you are also a senior citizen")
    else:
        print("you are not a senior citizen")
else:
    print("you are a minor")
    if age>=13:
        print("you are a teenager")
    else:
        print("you are a child")
