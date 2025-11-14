# Нестеров И.С. поиск LU разложения для матрицы

n = int(input("Введите размерность матрицы A (одно число)\n"))

A = [[] * n for _ in range(n)]

print("Введите матрицу построчно, разделяя элементы пробелом")
for i in range(n):
    A[i] = list(map(float, input().split()))

print("Введите вектор свободных членов, разделяя элементы пробелом\n")
b = list(map(float, input().split()))

x = [0] * n
y = [0] * n

U = [[0] * n for _ in range(n)]
L = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i <= j:
            if i == j:
                L[i][i] = 1
            U[i][j] = A[i][j] - sum([L[i][k] * U[k][j] for k in range(i)])
        else:
            L[i][j] = (A[i][j] - sum([L[i][k] * U[k][j] for k in range(j)])) / U[j][j]

print("\n", "=" * 6, "Полученная матрица L", "=" * 25, "\n", sep="")
for row in L:
    for el in row:
        print(f"{el:.2e}", end=" ")
    print()

print("\n", "=" * 6, "Полученная матрица U", "=" * 25, "\n", sep="")
for row in U:
    for el in row:
        print(f"{el:.2e}", end=" ")
    print()

check_A = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        check_A[i][j] += sum(L[i][k] * U[k][j] for k in range(n))

print("\n", "=" * 6, "Результат перемножения LU", "=" * 25, "\n", sep="")

for row in check_A:
    for el in row:
        print(f"{el:.2f}", end=" ")
    print()


for i in range(n):
    y[i] = (b[i] - sum([L[i][k] * y[k] for k in range(i)]))


for i in range(n-1, -1, -1):
    x[i] = (y[i] - sum([U[i][k] * x[k] for k in range(i + 1, n)])) / U[i][i]

print("\n", "=" * 6, "Проверка решения", "=" * 25, "\n", sep="")

for i in range(n):
    res = sum([A[i][j] * x[j] for j in range(n)])
    print(f"Найденное значение = {res:.2e}; Ошибка вычисления: {abs(b[i] - res):.2e}")