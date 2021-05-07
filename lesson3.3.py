# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(var_1, var_2, var_3):
    my_list = [var_1, var_2, var_3]
    try:
        sum_max = sum(my_list) - min(my_list)
        return sum_max
    except ValueError:
        return 'Функция работает только с цифрами!'


print(my_func(50,60,1))