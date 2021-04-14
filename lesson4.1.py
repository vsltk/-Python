from sys import argv

name, hours, payment, bonus = argv
payments = int(hours) * int(payment) + int(bonus)
print(f"Заработная плата сотрудника: {payments}")





