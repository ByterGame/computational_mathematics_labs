# Простая итерация, релаксация
import numpy as np

###############################################################
################## Метод простой итерации #####################
###############################################################
eps = 1e-6
n = int(input("Введите размерность матрицы (одно число n)\n"))

matrix = []

print("Введите матрицу построчно (n строк из n чисел, разделенных пробелом)\n")

for _ in range(n):
    matrix.append(list(map(float, input().split())))

print("Введите свободные члены системы (строка из n чисел, разделенных пробелом)\n")
b = list(map(int, input().split()))

# Начальное приближение
x = [0] * n
# иксы после первого шага
x_new = [b[i]/matrix[i][i] for i in range(n)]


def norm(x, y):
    """Функция для подсчета Евклидовой нормы разности векторов x и y"""
    res = 0
    if len(x) != len(y):
        print("Длины векторов при подсчете нормы не совпадают!")
        return -1
    for i in range(len(x)):
        res += (x[i] - y[i]) ** 2
    return res**0.5

norma = norm(x, x_new)
iter_cnt = 1
while norma >= eps:
    iter_cnt += 1
    for i in range(n):
        x[i] = b[i]/matrix[i][i] + sum([(-matrix[i][j]/matrix[i][i] if i != j else 0) * x[j] for j in range(n)])
    norma = norm(x_new, x)
    x_new = x.copy()
print(x_new)

# Думал буду все писать просто циклами, но чет произведение стало лень, мб потом перепишу
matrix = np.array(matrix)
x = np.array(x_new)
print(matrix@x)
print("Количество итераций:", iter_cnt)


###############################################################
##################### Метод релаксации ########################
###############################################################

x = [0] * n
x_new = [0] * n
w = 1

cnt_iter_rec = 0
norma = eps + 1

while norma >= eps:
    cnt_iter_rec += 1
    x_prev = x.copy()

    for i in range(n):
        sum1 = sum(matrix[i][j] * x_new[j] for j in range(i))
        sum2 = sum(matrix[i][j] * x_prev[j] for j in range(i+1, n))
        x_new[i] = (1 - w) * x_prev[i] + (w / matrix[i][i]) * (b[i] - sum1 - sum2)
    
    norma = norm(x_prev, x_new)
    x = x_new.copy()  

matrix_np = np.array(matrix)
x_np = np.array(x)
print("Проверка (A*x):", matrix_np @ x_np)
print("Количество итераций:", cnt_iter_rec)
