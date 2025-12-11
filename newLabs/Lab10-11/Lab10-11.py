# Метод вращения с преградами + метод Ричардсона. Нестеров И.С.

import numpy as np

A = np.array([[2, 1, 1],
              [1, 2.5, 1],
              [1, 1, 3]])

A_copy = A.copy()

obstacles = [10**(-i) for i in range(10)]

if abs(np.linalg.det(A)) < 10e-9:
    print("Матрица вырожденная")
    exit()
    
def find_max_el_ind(matrix):
    matrix_copy = matrix.copy()
    np.fill_diagonal(matrix_copy, 0)
    flat_idx = np.argmax(np.abs(matrix_copy)) 
    i, j = np.unravel_index(flat_idx, matrix.shape)
    return i, j


for obst in obstacles:

    i, j = find_max_el_ind(A)
    max_el = A[i][j]

    while abs(max_el) >= obst and abs(max_el) > 10e-9 and i != j:
        d = ((A[i][i] - A[j][j])**2 + 4 * A[i][j]**2)**0.5
        c = ((1 + abs(A[i][i] - A[j][j])/d)/2)**0.5
        s = (1 if (A[i][j] * (A[i][i] - A[j][j])) >= 0 else -1) * ((1 - abs(A[i][i] - A[j][j])/d)/2)**0.5
        n = A.shape[0]
        temp = A.copy()
        
        for k in range(n):
            if k != i and k != j:
                temp[k, i] = c * A[k, i] + s * A[k, j]
                temp[i, k] = temp[k, i]  
                
                temp[k, j] = -s * A[k, i] + c * A[k, j]
                temp[j, k] = temp[k, j]

        temp[i, i] = c**2 * A[i, i] + 2 * c * s * A[i, j] + s**2 * A[j, j]
        temp[j, j] = s**2 * A[i, i] - 2 * c * s * A[i, j] + c**2 * A[j, j]
        
        temp[i, j] = 0.0
        temp[j, i] = 0.0
        
        A = temp
        i, j = find_max_el_ind(A)
        max_el = A[i][j]

eigenvalues = np.diag(A)
print("Полученные собственные числа:\n", eigenvalues)
A = A_copy


b = np.array([2, 4, 11])
x = np.array([0, 0, 0])
ev_min = min(eigenvalues)
ev_max = max(eigenvalues)

eta = ev_min / ev_max
ro = (1 - eta)/(1 + eta)
tau_0 = 2 / (ev_min + ev_max)
n = 20
nu = np.cos(-np.pi/(2 * n))
tau_k = tau_0/(1 + ro * nu)
new_x = (b - A@x) * tau_k + x

while np.linalg.norm(x - new_x) > 10e-8:
    for k in range(1, n + 1):
        x = new_x.copy()
        nu = np.cos((2 * k - 1) * np.pi/(2 * n))
        tau_k = tau_0/(1 + ro * nu)
        new_x = (b - A@x) * tau_k + x

print("Полученные неизвестные:\n", new_x)
my_b = A@new_x
temp = [f"{i:.2e}" for i in my_b]
print("Полученный ответ A * x:\n", temp)
errors = b - my_b
errors = [f"{abs(i):.2e}" for i in errors]
print("Ошибка:\n", errors)