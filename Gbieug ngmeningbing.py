print("This program takes input from user and display's its multiplication table for you  ")
num1=int(input("enter any integer: "))
num2 = int("1")
while (num2<13):
    answer = num2 * num1
    print(str(num2)+ "x" + str(num2) + "=" , str(answer))
    num2 =num2 + 1
else:
    print("Thank you")



