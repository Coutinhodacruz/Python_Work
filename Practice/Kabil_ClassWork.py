# def count_elements(lst):
#     counts = {}
#     for element in lst:
#         counts[element] = counts.get(element, 0) + 1
#     return counts
#
#
# lst = [1, 2, 1, 3, 4, 2, 9, 6]
# result = {key: value for key, value in count_elements(lst).items() if value > 1}
# for key, value in result.items():
#     print(f'{{{key}: {value}}}')


def count_elements(lst):
    counts = {}
    for element in lst:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts


lst = [1, 2, 1, 3, 4, 2, 9, 6,3]
result = {}
for key, value in count_elements(lst).items():
    if value > 1:
        result[key] = value

for key, value in result.items():
    print(f'{{{key}: {value}}}')
