def count_capital_words(word):
    count = 0
    words = word.split()

    for word in words:
        if word[0].isupper():
            count += 1

    return count


sentence = "Life Is Good My Help Is In You Have Mercy On Me Oh Lord"
capital_word_count = count_capital_words(sentence)
print(capital_word_count)
