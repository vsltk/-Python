# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
# который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [7, 5, 3, 3, 2]

new_el = int(input('Введите натуральное число: '))
# for ind, i in enumerate(my_list[::-1]):
#    # print(f"{ind},{i},{len(my_list)-ind}")
#         if new_el <= i:
#             my_list.insert(len(my_list)-ind, new_el)
#             print(my_list)
#         #    break
#         elif new_el > i:
#             my_list.insert(0, new_el)
#             print(my_list)
#         break
# print(my_list[::-1])
# for ind, i in enumerate(my_list):
#     if new_el > i:
#         my_list.insert(ind, new_el)
#     print(my_list)
for i in range(len(my_list)):
    if new_el > my_list[i]:
        my_list.insert(i, new_el)
        print(my_list)
        break
    elif new_el <= my_list[-1]:
        my_list.append(new_el)
        print(my_list)
        break
