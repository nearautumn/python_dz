'''
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X
'''

n = int(input('Введите размер списка: '))
ls = [int(input('Введите число: ')) for i in range(n)]

print(*ls)

x = int(input('Введите искомое число: '))

count = 0
for i in ls:
    if i == x:
        count += 1

print(f'Встречается {count} раз(а)')