# def multiplication_table(n):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             print(i * j, end='\t')
#         print()
#
# print(f"{index} X {secondIndex} = {index * secondIndex}", end='\t\t')
# multiplication_table(12)


def multiplication_table(number):
    for index in range(1, number + 1):
        for secondIndex in range(1, number + 1):
            result = index * secondIndex
            equation = f"{secondIndex} * {index} = {result}"
            print(equation, end='\t\t')
        print()


multiplication_table(12)
