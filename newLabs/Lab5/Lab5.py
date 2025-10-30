# Нестеров И.С. Метод квадратного корня

n = int(input("Введите размерность матрицы A (одно число)\n"))

A = [[] * n for _ in range(n)]

print("Введите матрицу построчно, разделяя элементы пробелом")

for i in range(n):
    A[i] = list(map(float, input().split()))

S = [[0] * n for _ in range(n)]

S[0][0] = A[0][0]**0.5

for j in range(1, n):
    S[0][j] = A[0][j] / S[0][0]

for i in range(1, n):
    S[i][i] = (A[i][i] - sum([S[k][i]**2 for k in range(i)]))**0.5
    for j in range(i + 1, n):
        S[i][j] = (A[i][j] - sum([S[k][i] * S[k][j] for k in range(i)]))/S[i][i]

for row in S:
    for el in row:
        print(f"{el:.2e}", end=" ")
    print()

check_A = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        check_A[i][j] = sum([S[k][i] * S[k][j] for k in range(n)])

for row in check_A:
    for el in row:
        print(f"{el:.2f}", end=" ")
    print()