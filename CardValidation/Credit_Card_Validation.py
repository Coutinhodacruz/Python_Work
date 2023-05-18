starting_numbers = ["4", "5", "37", "6"]
single_digits = []


def isvalid(number):
    if number[0] not in starting_numbers:
        return False
    elif not len(number) >= 13 and not len(number) <= 16:
        return False
    else:
        sum = sum_of_double_even_index(number) + sum_of_double_odd_index(number)
        if sum % 10 == 0:
            return True
        else:
            return False


def sum_of_double_even_index(number):
    sum = 0
    for i in reversed(range(len(number))):
        if i % 2 == 0:
            val = int(number[i]) * 2
            single_digits.append(int(get_digit(val)))
    # Add all digits together

    for i in range(len(number)):
        sum += int(number[i])
    return sum


def sum_of_double_odd_index(number):
    sum = 0
    for i in reversed(range(len(number))):
        if i % 2 != 0:
            sum += int(number[i])
    return sum


def get_digit(number):
    number = str(number)
    if get_size(number) == 2:
        x = number[0]
        y = number[1]
        return int(x) + int(y)
    else:
        return number


def get_size(d):
    return len(d)


# ***Start***

card = input("Enter card number: ")

if isvalid(card):
    print("Card is valid")
else:
    print("Card is Invalid")
