import json


my_file = open('text_7.txt', 'r', encoding='utf-8')
firms = [line.split()[0] for line in my_file]
my_file.seek(0)
profit = [int(line.split()[2]) - int(line.split()[3]) for line in my_file]
count_firms = 0
for i in profit:
    if i >= 0:
        count_firms += 1
avg_profit = {'avg_profit': sum(i for i in profit if i >= 0) / count_firms}
my_dict = dict(zip(firms, profit))
new_list = [my_dict, avg_profit]
print(new_list)
with open('json_file.json', 'w', encoding='utf-8') as my_json_file:
    json.dump(new_list, my_json_file, indent=4, ensure_ascii=False)
my_file.close()
