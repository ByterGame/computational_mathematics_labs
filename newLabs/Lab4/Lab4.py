# Нестеров И.С. поиск LU разложения для матрицы

n = int(input("Введите размерность матрицы A (одно число)\n"))

A = [[] * n for _ in range(n)]

print("Введите матрицу построчно, разделяя элементы пробелом")
for i in range(n):
    A[i] = list(map(float, input().split()))

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

check_A = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        check_A[i][j] += sum(L[i][k] * U[k][j] for k in range(n))

for row in check_A:
    for el in row:
        print(f"{el:.2f}", end=" ")
    print()