# что-то там про отражения Нестеров И.С.
from scipy import linalg
import numpy as np

n = int(input("Введите размерность матрицы A (одно число)\n"))

A = np.zeros((n, n))

print("Введите матрицу построчно, разделяя элементы пробелом")

for k in range(n):
    A[k] = list(map(float, input().split()))

A_copy = A.copy().astype(float)

print(f"Введите соответсвующие свободные члены системы, разделяя пробелом ({n} штук)")

b = np.array(list(map(float, input().split())))
b_copy = b.copy()
if linalg.det(A) == 0:
        print("Матрица вырожденная")
        exit()

for k in range(n - 1):
    p = np.array([A[i][k] for i in range(k, n)])

    p[0] += (1 if p[0] >= 0 else -1) * sum(A[k:, k] ** 2) ** 0.5

    A[k, k] -= 2 * (p @ A[k:, k]) * p[0] / (p @ p)
    A[k + 1:, k] = np.zeros(n - k - 1)

    for i in range(k + 1, n):
        A[k:, i] -= 2 * (p @ A[k:, i]) * p / (p @ p)

    b[k:] -= 2 * (p @ b[k:]) * p / (p @ p)
    print("\nНовая матрица A\n")
    for row in A:
        for i in row:
            print(f"{i:.2e}", end = " ")
        print()


x = np.zeros((n))
for i in range(n - 1, -1, -1):
    x[i] = b[i]
    for j in range(i + 1, n):
        x[i] -= A[i][j] * x[j]
    x[i] /= A[i][i]
    
print("\nНеизвестные x:\n", x)
ans = A_copy @ x
print("\nПроверка решения:\n", *[f"{abs(b_copy[i] - ans[i]):.2e}" for i in range(len(b))])