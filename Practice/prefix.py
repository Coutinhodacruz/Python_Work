def print_prefix_occurrence(word):
    prefix_count = {}

    for word in word:
        for i in range(len(word)):
            prefix = word[:i + 1]
            if prefix in prefix_count:
                prefix_count[prefix] += 1
            else:
                prefix_count[prefix] = 1

    for prefix, count in prefix_count.items():
        if count > 1:
            print(f"{prefix}: {count}")



arr = ["flower", "flour", "flight"]
print_prefix_occurrence(arr)
