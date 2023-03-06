# TODO здесь писать код

file = open('zen.txt', 'r')
text_of_file = file.readlines()
for i in text_of_file[::-1]:
    print(i)

file.close()

# зачтено
