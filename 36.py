'''Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.'''

def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1, num_rows + 1):
        numbers = []
        for y in range(1, num_columns + 1):
            num = operation(x, y)
            numbers.append(num)
        print(*map(str, numbers))

print_operation_table(lambda a,b: a*b)