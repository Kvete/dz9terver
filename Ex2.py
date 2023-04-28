
import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

def mse_(b, x, y):
    return np.sum((b*x-y)**2)/len(x)

def b_mse(b, x, y):
    return 2/len(x)*np.sum((b*x-y)*x)


alpha = 1e-06
b = 0.1
n = 1500
for i in range(n):
    b -= alpha * b_mse(b,zp,ks)
    if i % 100 ==0:
        print(f'Итерация = {i}, коэффициент b = {b}, mse = {mse_(b, zp,ks)}')

print(f'Среднеквадратичная ошибка mse {mse_(5.8898,zp,ks)} модели без интерсепта при коэффициенте 5.8898')