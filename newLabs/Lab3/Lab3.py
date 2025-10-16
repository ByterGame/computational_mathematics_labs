# Нестеров И.С. Лаба третья
# Метод Гаусса с оптимальным исключением
from copy import deepcopy
from scipy import linalg

def main():
    n = int(input("Введите размерность матрицы (одно число)\n"))
    matrix = []
    b = []
    print("Введите элементы матрицы построчно, разделяя их пробелом. Справа добавьте свободные члены матрицы для соответствующей строки.\n")

    for i in range(n):
        data = list(map(float, input().split()))
        matrix.append(data[:-1])
        b.append(data[-1])

    if linalg.det(matrix) == 0:
        print("Матрица вырожденная")
        return
    
    original_matrix = deepcopy(matrix)
    original_b = deepcopy(b)

    variable_order = list(range(n))

    for k in range(n):
        max_val = 0
        max_i = k
        max_j = k
        
        for i in range(k, n):
            for j in range(k, n):
                if abs(matrix[i][j]) > abs(max_val):
                    max_val = matrix[i][j]
                    max_i = i
                    max_j = j
        
        if max_i != k:
            matrix[k], matrix[max_i] = matrix[max_i], matrix[k]
            b[k], b[max_i] = b[max_i], b[k]
            print(f"Итерация {k+1}: перестановка строк {k+1} <-> {max_i+1}")
        
        if max_j != k:
            for i in range(n):
                matrix[i][k], matrix[i][max_j] = matrix[i][max_j], matrix[i][k]
            variable_order[k], variable_order[max_j] = variable_order[max_j], variable_order[k]
            print(f"Итерация {k+1}: перестановка столбцов {k+1} <-> {max_j+1}")
            print(f"Теперь порядок переменных: {[f'x{i+1}' for i in variable_order]}")

        for j in range(k):
            factor = matrix[k][j]
            for col in range(k, n):
                matrix[k][col] -= factor * matrix[j][col]
            b[k] -= factor * b[j]
            matrix[k][j] = 0.0

        pivot = matrix[k][k]
        for j in range(k, n):
            matrix[k][j] /= pivot
        b[k] /= pivot

        for i in range(k):
            factor = matrix[i][k]
            for j in range(k, n):
                matrix[i][j] -= factor * matrix[k][j]
            b[i] -= factor * b[k]
            matrix[i][k] = 0.0

        print(f"\nМатрица после итерации {k + 1}:")
        for row in range(n):
            for col in range(n):
                print(f"{matrix[row][col]:10.6f}", end=" ")
            print(f"| {b[row]:10.6f}")
        print()

    x_temp = b.copy()
    
    x = [0] * n
    for i in range(n):
        x[variable_order[i]] = x_temp[i]

    print("\nРешение системы (в исходном порядке переменных):")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.6f}")

    print("\nПроверка решения:")
    for i in range(n):
        result = 0
        for j in range(n):
            result += original_matrix[i][j] * x[j]
        error = abs(result - original_b[i])
        print(f"Уравнение {i+1}: {result:.6f} = {original_b[i]:.6f} (ошибка: {error:.2e})")


main()
