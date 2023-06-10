'''Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)'''

def new_list() ->list:
    lenght = int(input('Введите длину списка: '))
    result_list = [int(input('Введите число: ')) for i in range(lenght)]
    return result_list

def in_range_indexes(user_list: list, user_min: int, user_max: int) -> list:
    result = []
    for i in range(len(user_list)):
        if user_list[i] >= user_min and user_list[i] <= user_max:
            result.append(i)
    return result


list_1 = new_list()

min = int(input('Введите минимум: '))
max = int(input('Введите максимум: '))

print('Индексы чисел, входящих в диапазон:', *in_range_indexes(list_1, min, max))