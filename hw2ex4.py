matr = [[2, 3], [1, 5], [3, 2]]
vec = [2, 5]
m_len = len(matr)
pm_len = len(matr[0])

res = []
for i in range(0, m_len):
    j = 0
    s = 0
    for j in range(0, pm_len):
        s = s + matr[i][j] * vec[j]
    res.append(s)
print(f"Результат умножения матрицы {matr} на вектор {vec}: ", res)