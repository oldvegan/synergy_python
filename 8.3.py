print(f"Введите грузоподъемность лодки:")
m = int(input())
print(f"Введите количество рыбаков:")
n = int(input())
weight = []
boat = 0
for i in range(n):
    print(f"Введите вес {i+1} рыбака:")
    weight.append(int(input()))
weight.sort()
i=0
while (i < n):
    if weight[i]+ weight[n-1] <= m:
        boat += 1
        n -= 1
        i += 1
    else:
        boat += 1
        n -= 1
print(f"Необходимое количество лодок: {boat}")    