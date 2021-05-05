import random


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for row in self.matrix:
            res += f"{' '.join([str(l) for l in row])}\n"
        return res

    def __add__(self, other):
        new_matrix = [[] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(new_matrix)


m_1 = Matrix([[random.randint(0, 10) for _ in range(3)], [random.randint(0, 10) for _ in range(3)]])
m_2 = Matrix([[random.randint(0, 10) for _ in range(3)], [random.randint(0, 10) for _ in range(3)]])

print(f"1 матрица:\n{m_1}")
print(f"2 матрица:\n{m_2}")
m_3 = m_1 + m_2
print(f"Сумма 1 и 2 матрицы:\n{m_3}")
