num1 =float(input("please enter your number: "))
operand =input("please input the operation symbol: ")
num2 =float(input("Your second number please: "))

if operand == "+":
	print(num1 + num2)
elif operand == "-":
	print("num1 - num2")
elif operand == "/":
	print(num1 / num2)
elif operand == "%":
	print(num1 % num2)
elif operand == "*":
	print(num1 * num2)
else:
	print("invalid operator")
