while True:
    print("---MENU---")
    print("1.say Hello!")
    print("2.say Goodbye")
    print("3.Quit")
    choice=input("Enter your choice:")
    if choice==1:
        print("Hello")
    elif choice==2:
        print("Goodbye for now")
    elif choice==3:
        print("Existing Program")
        break
    else:
        print("Invalid Choice.Please try again")
print("Program has ended")