print(f"Введите число:")
n = int(input())
tmp = []
for i in range(n):
    
    tmp.append(int(input()))
tmp.reverse()
print(f"Перевернутый массив: {tmp}")