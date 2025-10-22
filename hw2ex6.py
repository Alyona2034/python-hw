dat = [2, 6, 4, 3, 1]
c = [1, -2, 3]
a = len(dat)
b = len(c)
res_l = a - b + 1
res = []
for i in range(0, res_l):
    j = 0
    s = 0
    for j in range(0, b):
        s = s + dat[i + j] * c[j]
    res.append(s)
print(f"Результат сверточной фильтрации массива {dat} с ядром свертки {c}: {res}")