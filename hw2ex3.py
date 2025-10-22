import random

fv = []
sv = []
size_v = input("Введите размеры векторов: ")
size_v = int(size_v)
scal = input("Введите скаляр: ")
scal = int(scal)
for i in range(1, size_v + 1):
    fv.append(random.randint(-10, 10))
    sv.append(random.randint(-10, 10))
print("Векторы: ", fv, sv)

sum_v = []
for i in range(0, size_v):
    sum_v.append(fv[i]+sv[i])
print("Сумма векторов: ", sum_v)

mult_v = []
for i in range(0, size_v):
    mult_v.append(fv[i]*sv[i])
print("Умножение векторов: ", mult_v)

norm_fv = 0
norm_sv = 0
for i in range(0, size_v):
    norm_fv = norm_fv + fv[i] * fv[i]
    norm_sv = norm_sv + sv[i] * sv[i]
norm_fv = norm_fv ** 0.5
norm_sv = norm_sv ** 0.5
print(f"Норма первого вектора: {norm_fv}, норма второго вектора: {norm_sv}")

mult_sc = []
if norm_fv > norm_sv:
    for i in range(0, size_v):
        mult_sc.append(fv[i]*scal)
    print("Умножение на скаляр первого вектора: ", mult_sc)
else:
    for i in range(0, size_v):
        mult_sc.append(sv[i]*scal)
    print("Умножение на скаляр второго вектора: ", mult_sc)