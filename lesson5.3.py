# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
my_file = open('text_3.txt', 'r', encoding='utf-8')
list_of_lists = my_file.read()
lines = list_of_lists.split()
my_values = [float(lines[i]) for i in range(1, len(lines), 2)]
my_keys = [lines[i] for i in range(0, len(lines), 2)]
my_dict = dict(zip(my_keys, my_values))
print(' '.join(('Сотрудники получающие меньше 20 000 руб.:', *(value for value in my_dict if my_dict[value] < 20000))))
print(f"Средний доход сотрудников: {sum(my_values) / len(my_values)}")
my_file.close()
