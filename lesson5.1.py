# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

my_file = open('new_file.txt', 'w')
while True:
    user_data = input('Введите данные для записи в файл, каждый ввод будет записан построчно. '
                      'Для завершения программы, нажмите Enter без ввода данных: ')
    if user_data == '':
        break
    else:
        print(user_data, file=my_file)
my_file.close()


