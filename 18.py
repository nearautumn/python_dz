'''Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X'''

n = int(input('Введите размер списка: '))
ls = [int(input('Введите число: ')) for i in range(n)]

print(*ls)

x = int(input('Введите число Х: '))
diff = abs(x - ls[0])
result = ls[0]

for i in ls[1:]:
    if abs(x - i) < diff:
        diff = abs(x - i)
        result = i

print(result)