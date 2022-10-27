# TODO здесь писать код

text = input('Введите строку: ')
h_list =  [index for index, character in enumerate(text) if character == 'h']
print('Развёрнутая последовательность между первым и последним h: ', text[(h_list[-1] - 1):h_list[0]:-1])