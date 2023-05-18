def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(results):
    print("Target found", results)


numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
result = recursive_binary_search(numbers, 22)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
