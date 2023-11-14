def add(x,y):
    return x + y
def substract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def devide(x,y):
    return x / y
def div_2(x,y):
    return x // y
def div_3(x,y):
    return x % y
def power(x,y):
    return pow(x,y)


print("Please choose an operator:")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. %")
print("6. //")
print("7. **")

choice = input("Please enter your choice 1/2/3/4/5/6/7: ")

value_1 = int(input("Please enter the first number: "))
value_2 = int(input("Please enter the second number: "))

if choice == '1':
    print(value_1, "+", value_2, "=", add(value_1,value_2))
elif choice == '2':
    print(value_1, "-", value_2, "=", substract(value_1,value_2))
elif choice == '3':
    print(value_1, "*", value_2, "=", multiply(value_1, value_2))
elif choice == '4':
    print(value_1, "/", value_2, "=", devide(value_1, value_2))
elif choice == '5':
    print(value_1, "%", value_2, "=", div_2(value_1, value_2))
elif choice == '6':
    print(value_1, "//", value_2, "=", div_3(value_1,value_2))
elif choice == '7':
    print(value_1, "**", value_2, "=", power(value_1,value_2))
else:
    print('You have not typed a valid operator, please run the program again.')
