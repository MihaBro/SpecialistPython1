# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

# TODO: your code here
cow = int(input('Введите количество коров: '))
cow_index = cow % 10
if cow_index  == 1:
    print ("На лугу пасется", cow, "корова")
elif 1 < cow_index < 5:
    print("На лугу пасется", cow, "коровы")
else:
    print("На лугу пасется", cow, "коров")
