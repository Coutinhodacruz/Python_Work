def is_palindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True


word = "mum"
print(is_palindrome(word))
print(word)
