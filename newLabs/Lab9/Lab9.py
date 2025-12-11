# Градиентный спуск
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
x = np.zeros(n)

iter = 0
while True:
    iter += 1
    r = b - A@x
    alpha = np.dot(r, r) / np.dot(A@r, r)
    new_x = x + alpha * r
    if np.linalg.norm(new_x - x) <= 1e-6:
        x = new_x
        break
    x = new_x

print(x)
print(A@x)
print(iter)