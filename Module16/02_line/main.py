# TODO здесь писать код

high_1 = []      # 160 см до 176 см с шагом 2,
high_2 = []   # во втором классе — от 162 см до 180 см с шагом 3

for i in range(160, 178, 2):
    high_1.append(i)
for i in range(162, 183, 3):
    high_2.append(i)

high_1.extend(high_2)
high_1.sort()
print('Отсортированный список учеников: ', high_1)