# Метод окаймления
from scipy import linalg
import numpy as np

n = int(input("Введите размерность матрицы A (одно число)\n"))

A = np.zeros((n, n))

print("Введите матрицу построчно, разделяя элементы пробелом")

for i in range(n):
    A[i] = list(map(float, input().split()))

print(f"Введите соответсвующие свободные члены системы, разделяя пробелом ({n} штук)")

b = np.array(list(map(float, input().split())))

if linalg.det(A) == 0:
        print("Матрица вырожденная")
        exit()

A_rev = np.array([[1/A[0, 0]]])

for i in range(1, n):
    v_n = A[i, :i]
    u_n = A[:i, i]
    a_nn = A[i][i]

    a_n = a_nn - v_n @ A_rev @ u_n

    new_A_rev = np.zeros((i+1, i+1))
    P_n = A_rev + (A_rev @ np.outer(u_n, v_n) @ A_rev)/a_n
    r_n = - (A_rev @ u_n) / a_n
    q_n = - (v_n @ A_rev) / a_n

    new_A_rev[:i, :i] = P_n 
    new_A_rev[:i, i] = r_n
    new_A_rev[i, :i] = q_n
    new_A_rev[i][i] = 1 / a_n 

    A_rev = new_A_rev


print("Обратная матрица:")
for row in A_rev:
    for i in row:
        print(f"{i:.2e}", end=" ")
    print()

print("\nПроверка: A * A_rev")
for row in A @ A_rev:
    for i in row:
        print(f"{i:.2e}", end=" ")
    print()
         

print("\nНаходим неизвестные путем умножения обеих частей системы на обратную матрицу слева")
x = A_rev @ b
print(*[f"{i:.2e}" for i in x])

Ax = A @ x
print("\nПроверим решение A * x - b")
print(*[f"{abs(Ax[i] - b[i]):.2e}" for i in range(len(Ax))])