# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
my_file = open('text_4.txt', 'r', encoding='utf-8')
new_file = open('text_4_translate.txt', 'w', encoding='utf-8')
for line in my_file:
    new_file.writelines([line.replace(line.split()[0], my_dict.get(line.split()[0]))])
my_file.close()
new_file.close()
