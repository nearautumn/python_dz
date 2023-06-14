'''Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''

def new_progression(first_element: int, diff: int, count: int) -> list:
    result = [first_element]
    for i in range(1, count):
        result.append(first_element + i * diff)
    return result


start = int(input('Введите первый элемент прогрессии: '))
user_diff = int(input('Введите разность: '))
user_count = int(input('Введите количество элементов прогрессии: '))
print(new_progression(start, user_diff, user_count))