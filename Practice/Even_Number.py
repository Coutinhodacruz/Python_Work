# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# # print(is_even(4))
# print(is_even(7))


def highest_even(numbers):
    max_even = None
    for number in numbers:
        if number % 2 == 0:
            if max_even is None or number > max_even:
                max_even = number
    return max_even


numbers = [22, 70, 42, 49, 6, 11, 10]
result = highest_even(numbers)
print(result)
