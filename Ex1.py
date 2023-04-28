import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
mult = []
for i in range(len(zp)):
    mult.append(zp[i] * ks[i])
zp2 = []
for i in range(len(zp)):
    zp2.append(zp[i] ** 2)
b1 = (np.mean(mult) - np.mean(zp) * np.mean(ks)) / (
            np.mean(zp2) - np.mean(zp) ** 2)
print(b1)
b0 = np.mean(ks) - b1 * np.mean(zp)
y_pred = []
for el in zp:
    y_pred.append(el * b1 + b0)
print(y_pred)

b1=(len(zp)*np.sum(mult)-np.sum(zp)*np.sum(ks))/(len(zp)*np.sum(zp2)-np.sum(zp)**2)
print(b1)
