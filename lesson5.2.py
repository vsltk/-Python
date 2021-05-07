# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
# lines = 0
# my_file = open('new_file.txt', 'r', encoding='utf-8')
# for line in my_file:
#     lines += 1
# my_file.seek(0)
# data = my_file.read()
# words = data.split()
# print(f"Количество строк в файле: {lines},\nКоличество слов в файле: {len(words)}.")
lines = 0
my_file = open('new_file.txt', 'r', encoding='utf-8')
for line in my_file:
    lines += 1
print(f"Количество строк в файле: {lines}")
my_file.seek(0)
list_of_lists = []
for line in my_file:
    line = line.split()
    list_of_lists.append(line)
for ind, el in enumerate(list_of_lists, 1):
    print(f"Количество слов в строке № {ind}: {len(el)}")
my_file.close()
