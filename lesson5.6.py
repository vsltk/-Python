my_file = open('text_6.txt', 'r', encoding='utf-8')
my_dict = {}
for line in my_file:
    lesson, count_lesson = line.split(':')
    lesson_sum = sum(map(int, ''.join([i for i in count_lesson if i == ' ' or i in '1234567890']).split()))
    my_dict[lesson] = lesson_sum
print(f"{my_dict}")
my_file.close()
