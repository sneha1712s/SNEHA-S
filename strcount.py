def count_words(string):
    words = string.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq


string =str(input("enter"))
word_frequency = count_words(string)
print(word_frequency)