
text = input("Text: ")
word_to_be_counted = {}

words = text.split(' ')
for word in words:
    frequency = word_to_be_counted.get(word, 0)
    word_to_be_counted[word] = frequency + 1


words = list(word_to_be_counted)
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_be_counted[word]))
