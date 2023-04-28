import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])


def mse(a, b, x, y):
    return np.sum(((a + b * x) - y) ** 2) / len(x)


def mse_a(a, b, x, y):
    return 2 * np.sum((a + b * x) - y) / len(x)


def mse_b(a, b, x, y):
    return 2 * np.sum(((a + b * x) - y) * x) / len(x)


alpha = 5e-05
a = 0.1
b = 0.1
n = 1000000

for i in range(n):
    a -= alpha * mse_a(a, b, zp, ks)
    b -= alpha * mse_b(a, b, zp, ks)
    if i % 50000 == 0:
        print(f'Итерация #{i}, a={a}, b={b}, mse={mse(a, b, zp, ks)}')

print(
    f'Среднеквадратичная ошибка mse {mse(444.1773, 2.62, zp, ks)} для модели с '
    f'интерсептером и a= 444.1773,b=2.62')
