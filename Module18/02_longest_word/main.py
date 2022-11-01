# TODO здесь писать код

text = input("Введите строку: ")

max_word = max([len(word) for word in text.split()])
print(max_word)

print('Самое длинное слово: ', 'Длина этого слова: ',{max_word})

# ***********************
sentense = "какое-либо предложение"
words = dict()
for word in sentense.split(" "):
      words[len(word)] = word

biggestWord = words[max(words)]
print(biggestWord)


# print(" ".join(text.split()))