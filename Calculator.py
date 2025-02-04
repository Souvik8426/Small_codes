print('''Enter 1 for addition
Enter  2 for multiplication
Enter 3 for dvision
Enter 4 for Substraction''')
option=int(input("enter the option form 1 to 4: "))
a=int(input("Enter the number: "))
b=int(input("Enter the seccond number:"))
if 1 <= option <= 4:
    if option==1:
        print(a+b)
    elif option==2:
        print(a*b)
    elif option==3:
        if b == 0:
            print("Undefined")
        else:
            print(a/b)
    elif option==4:
        print(a-b)
else:
    print('''The number is out of range
kindly enter a number between 1 and 4''')