l = [1, -3, -5, -2, 2, -6, 3, 5, -1, 8]
n = len(l)
res = [0] * n
all_ab_z = []
for i in range(0, n):
    if l[i] > 0:
        all_ab_z.append(i)
l_all = len(all_ab_z)

for i in range(0, n):
    lin = -1
    rin = n + 1
    if l[i] < 0:
        for j in range(0, l_all):
            if (lin < all_ab_z[j]) and (i > all_ab_z[j]):
                lin = all_ab_z[j]
            if (rin > all_ab_z[j]) and (i < all_ab_z[j]):
                rin = all_ab_z[j]
        res[i] = (l[lin] + l[rin]) / 2
    else:
        res[i] = l[i]
print(f"Изначальный массив: {l}, итоговый массив: {res}")