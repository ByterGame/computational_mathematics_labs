# Нестеров И.С. Лаба вторая, вариант второй
from copy import deepcopy
from scipy import linalg
def main():
    n = int(input("Введите размерность матрицы (одно число)\n"))
    matrix = []
    b = []
    print("Введите элементы матрицы построчно, разделяя их пробелом. Справа добавьте свободные члены матрицы для соответсвующий строки.\n")

    for i in range(n):
        data = list(map(float, input().split()))
        matrix.append(data[:-1])
        b.append(data[-1])

    if linalg.det(matrix) == 0:
        print("Матрица вырожденная")
        return
    
    original_matrix = deepcopy(matrix)
    original_b = deepcopy(b)

    for iter in range(n - 1):
        max_col_ind = iter
        max_col_el = matrix[iter][iter]
        for row in range(iter, n):
            if max_col_el < matrix[row][iter]:
                max_col_ind = row
                max_col_el = matrix[max_col_ind][iter]  
        
        matrix[iter], matrix[max_col_ind] = matrix[max_col_ind], matrix[iter]
        b[iter], b[max_col_ind] = b[max_col_ind], b[iter]
        # Теперь в строке iter у нас максимальный элемент в столбце и он находится на диагонали
        for row in range(iter + 1, n):
            factor = matrix[row][iter] / matrix[iter][iter]
            for col in range(iter + 1, n):
                matrix[row][col] -= factor * matrix[iter][col]
            b[row] -= factor * b[iter]
            matrix[row][iter] = 0

        print(f"\nИтерация {iter + 1}")
        for row in matrix:
            for num in row:
                print(f"{num:.3f}", end=" ")
            print()

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]

    print("\nРешение системы:")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.6f}")

    print("\nПроверка решения:")
    for i in range(n):
        result = 0
        for j in range(n):
            result += original_matrix[i][j] * x[j]
        print(f"Уравнение {i+1}: {result} = {original_b[i]}")

main()