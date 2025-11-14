# Нестеров И.С. Метод квадратного корня

n = int(input("Введите размерность матрицы A (одно число)\n"))

A = [[] * n for _ in range(n)]

print("Введите матрицу построчно, разделяя элементы пробелом")

for i in range(n):
    A[i] = list(map(float, input().split()))

print("Введите вектор свободных членов, разделяя элементы пробелом\n")
b = list(map(float, input().split()))

x = [0] * n
y = [0] * n

S = [[0] * n for _ in range(n)]

S[0][0] = A[0][0]**0.5

for j in range(1, n):
    S[0][j] = A[0][j] / S[0][0]

for i in range(1, n):
    S[i][i] = (A[i][i] - sum([S[k][i]**2 for k in range(i)]))**0.5
    for j in range(i + 1, n):
        S[i][j] = (A[i][j] - sum([S[k][i] * S[k][j] for k in range(i)]))/S[i][i]

print("\n", "=" * 6, "Полученная матрица S", "=" * 25, "\n", sep="")

for row in S:
    for el in row:
        print(f"{el:.2e}", end=" ")
    print()

check_A = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        check_A[i][j] = sum([S[k][i] * S[k][j] for k in range(n)])

print("\n", "=" * 6, "Результат перемножения S'S", "=" * 25, "\n", sep="")

for row in check_A:
    for el in row:
        print(f"{el:.2f}", end=" ")
    print()

for i in range(n):
    y[i] = (b[i] - sum([S[k][i] * y[k] for k in range(i)])) / S[i][i]

for i in range(n-1, -1, -1):
    x[i] = (y[i] - sum([S[i][k] * x[k] for k in range(i + 1, n)])) / S[i][i]

print("\n", "=" * 6, "Проверка решения", "=" * 25, "\n", sep="")

for i in range(n):
    res = sum([A[i][j] * x[j] for j in range(n)])
    print(f"Найденное значение = {res:.2e}; Ошибка вычисления: {abs(b[i] - res):.2e}")
