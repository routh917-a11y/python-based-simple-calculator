a = float(input("Enter the first number: "))  # this is for the values input 
b = float(input("Enter the second number: "))

print("Select operation:")     # this is for the operation list that can be cal. can able to do !
print("1) Addition (+)")
print("2) Subtraction (-)")
print("3) Multiplication (*)")
print("4) Division (/)")
print("5) Modulus (%)")
print("6) Remainder(//)")

choice = int(input("enter the operation request num :")) # this is the place were we can input our choice for operation

if choice == 1:        # this is the conditions by which our calculation is get proceed !!
    print(a+b)

elif choice == 2:
     print(a-b)

elif choice == 3:
     print(a*b)

elif choice == 4:
     print(a/b)
     if b == 0:
        print("error: the value is undefined")

elif choice == 5:
    print(a%b)    

elif choice == 6:
    print(a//b)

else: print("invalid request , try another one !!")    # the ultimate weapon