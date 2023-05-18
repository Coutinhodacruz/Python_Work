# def hcf_multiply_list(*numbers):
#     factors = []
#     for num in numbers:
#         num_factors = []
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 num_factors.append(i)
#         factors.append(set(num_factors))
#     hcf_set = set.intersection(*factors)
#     hcf = max(hcf_set)
#     hcf_list = []
#     for num in numbers:
#         if num % hcf == 0:
#             hcf_list.append(int(num / hcf))
#     return hcf_list
#
#
# number = hcf_multiply_list(30, 42)
# print(number)


#
#
# def hcf_prime_factors(*numbers):
#     factors = []
#     for num in numbers:
#         num_factors = []
#         i = 2
#         while i * i <= num:
#             if num % i:
#                 i += 1
#             else:
#                 num /= i
#                 num_factors.append(i)
#         if num > 1:
#             num_factors.append(num)
#         factors.append(set(num_factors))
#     hcf_set = set.intersection(*factors)
#     hcf_factors = list(hcf_set)
#     return hcf_factors
#
#
# number = hcf_prime_factors(30, 42)
# print(number)

first_number = 3000
second_number = 1000


def find_hcf(number_one, number_two):
    new_list = []

    for i in range(2, number_two):
        while number_one % i == 0 and number_two % i == 0:
            number_one = number_one // i
            number_two = number_two // i
            new_list.append(i)
    return new_list


print(find_hcf(first_number, second_number))
