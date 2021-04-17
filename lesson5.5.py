# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
my_file = open('text_5.txt', 'w+', encoding='utf-8')
user_data = input('Введите числа через пробел и нажмите Enter: ')
print(user_data, file=my_file)
my_file.seek(0)
list_of_lists = []
for lines in my_file:
    lines = lines.split()
    list_of_lists.append(lines)
list_of_lists = sum(list_of_lists, [])
m_sum = 0
for n in list_of_lists:
    m_sum += int(n)
print(f"Сумма чисел равна {m_sum}, работа программы завершена!")

my_file.close()