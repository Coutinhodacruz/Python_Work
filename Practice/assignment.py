num = [2, 6, 9, 7, 41, 4]


# No 1
def function(count):
    assume = num[0]
    for i in range(1, len(count)):
        if num[i] > assume:
            assume = count[i]
    return assume


print(function(num))


def largest_number(list_value: list) -> int:
    temp = list_value[0]

    for i in range(len(list_value)):
        if list_value[i] > temp: temp = list_value[i]

        return temp


list_value = [33, 5, 78, 56, 2]

print(largest_number(list_value))


def digit_to_list_converter(numb: list) -> list:
    list_of_numb = []

    for i in numb:
        list_of_numb.append(int(i))
    return list_of_numb


print(digit_to_list_converter(list_value))


def list_concate(list_one: list, list_two: list) -> list:
    return list_one + list_two


print(list_concate(list_value, list_value))


def reverse_list(list_rev: list) -> list:
    list_co = []
    for i in range(len(list_rev), 0):
        list_co.append(i)
        return list_co


print(reverse_list(list_value))


def over_load(*word):
    return word


print(over_load("hi", 56, list_value, 6.7))

list_number = [30, 40, 50, 60, 70]


def list_total(list_one: list) -> int:
    total = 0
    for i in range(0, len(list_one), 1):
        total += list_one[i]
        return total


print(list_total(list_number))
