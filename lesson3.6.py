# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func():
    my_word = input('Введите слово из маленьких латинских букв: ')
    if my_word.islower():
        for n in my_word:
            if 97 <= ord(n) <= 122:
                my_word = my_word.title()
            return my_word
    else:
        return 'Функция принимает только слова из маленьких латинских букв!'


print(int_func())
