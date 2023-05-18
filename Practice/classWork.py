list = [5, 8, 3, 3, 5, 2, 5, 1, 14]

for num in list:

    if num % 2 == 0:
        print(num, " ")


def is_even(number):
    return number % 2 == 0


def fetch_even_numbers_from(numbers: list) -> list:
    result = []
    for number in numbers:
        if is_even(number): result.append(number)

    return result
