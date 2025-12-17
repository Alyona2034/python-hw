rtoy = [[0.299, 0.587, 0.114], [0.5959, -0.2746, -0.3213], [0.2115, -0.5227, 0.3112]]
ytor = [[1, 0.956, 0.619], [1, -0.272, -0.647], [1, -1.106, 1.703]]

def conv(vec):
    x = vec[0]
    s = vec[1]
    z = vec[2]
    t = vec[3]
    if t == 0:
        y, i, q = [rtoy[0][0]*x + rtoy[0][1]*s + rtoy[0][2]*z,
                   rtoy[1][0]*x + rtoy[1][1]*s + rtoy[1][2]*z,
                   rtoy[2][0]*x + rtoy[2][1]*s + rtoy[2][2]*z]
        return [y, i, q]
    else:
        r, g, b = [ytor[0][0] * x + ytor[0][1] * s + ytor[0][2] * z,
                   ytor[1][0] * x + ytor[1][1] * s + ytor[1][2] * z,
                   ytor[2][0] * x + ytor[2][1] * s + ytor[2][2] * z]
        return [r, g, b]

vec0 = [0.5, 0.6, 0.1, 0]
vec1 = conv(vec0)
print(vec1)