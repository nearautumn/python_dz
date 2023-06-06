'''Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии'''



def exponent(number: int, degree: int) -> int:
    if degree <= 0:
        return 1
    result = number * exponent(number, degree - 1)
    return result


user_number, user_degree = int(input('Введите число: ')), int(input('Введите степень: '))
print(exponent(user_number, user_degree))