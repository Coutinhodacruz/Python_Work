number = int(input("Enter a number: "))
if number % 2 == 0:
    print("this number is an even number")
else:
    print("the number is odd number")
if number % 4 == 0:
    print("is the multiple of 4\n")
else:
    print("is not multiple of 4\n")

num = int(input("Enter first number\n"))
checker = int(input("Enter second number\n"))
if num % checker == 0:
    print("Your first number is Divisible by 5")
else:
    print("your number is not Divisible by 5")


def total(list_value: list) -> list:
    goodness = []
    for i in range(0, len(list_value), 1):
        if list_value[i] < 5:
            print(list_value[i])
            goodness.append(list_value[i])
    return goodness


counter = [1, 4, 6, 3, 90, 67, 89, 5, 2]
print(total(counter))

count = int(input("Enter number "))


def total(list_value: list) -> list:
    for i in range(0, len(list_value), 1):
        if list_value[i] < count:
            print(list_value[i])
    return list_value


print(total(counter))


def total():
    user_input = int(input("Enter a number "))
    numbers = []
    for i in range(1, user_input):
        if user_input % i == 0:
            numbers.append(i)
    print(num)


total()
