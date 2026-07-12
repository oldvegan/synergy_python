import random

def matrix(x, y):
    tmp = [[random.randint(-100, 100) for i in range(x)] for j in range(y)]
    return tmp

tmp1 = matrix(2, 3)
tmp2 = matrix(2, 3)

tmp3= [[ tmp1[i][j] + tmp2[i][j] for j in range(len(tmp1[0]))] for i in range(len(tmp1))]

print(tmp1)
print(tmp2)
print(tmp3)