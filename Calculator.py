#CALCULATOR
print("BASIC CALCULATOR")
print("MAIN MENU ")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
num1=int(input("enter first number"));
num2=int(input("enter second number"));
operation=int(input("enter the operation to be performed"));
if operation==1:
    print("ADDITION")
    sum=num1+num2
    print("Sum:",sum)
elif operation==2:
    print("SUBTRACTION")
    diff=num1-num2
    print("Difference:",diff)
elif operation==3:
    print("MULTUIPLICATION")
    mul=num1*num2
    print("Product:",mul)
elif operation==4:
    print("DIVISION")
    div=num1/num2
    print("Division:",div)
else:
   print("Invaild opeartion no such opertion exist")
