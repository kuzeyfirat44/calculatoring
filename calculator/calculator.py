num1 = int(input("Give Me A Number."))
num2 = int(input("Give Me Another Number."))
cal1 = input("Give Me A Calculation. ( + , - , * , / )")
if cal1 == "+":
    print(num1 + num2)
elif cal1 == "-":
    print(num1 - num2)
elif cal1 == "*":
    print(num1 * num2)
elif cal1 == "/":
    if num2 == 0:
        print("You can't divide by zero.")
    else:
        print(num1 / num2)
        