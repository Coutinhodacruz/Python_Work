def sort_strings(arr):
    number = len(arr)
    for i in range(number):

        for word in range(0, number - i - 1):

            if arr[word] > arr[word + 1]:
                arr[word], arr[word + 1] = arr[word + 1], arr[word]


my_array = ["orange", "apple", "banana", "pear", "goat", "dog", "crayfish", "zebra", "yam", "queen", "egg", "fish","host", "jug", "kross", "ice", "lyon"]
sort_strings(my_array)
print(my_array)


def reverse_strings(array):
    n = len(array)
    for i in range(n):

        for j in range(0, n - i - 1):

            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


your_array = ["orange", "apple", "banana", "pear", "goat", "dog", "crayfish", "zebra", "yam", "queen", "egg", "fish","host", "jug", "kross", "ice", "lyon"]
reverse_strings(your_array)
print(your_array)
