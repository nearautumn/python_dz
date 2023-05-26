# Задача 2: Найдите сумму цифр трехзначного числа.

n = (input('Введите трехзначное число: '))
first = int(n[0])
second = int(n[1])
third = int(n[2])

print (f"{n} -> {first + second + third} ({first} + {second} + {third})")
