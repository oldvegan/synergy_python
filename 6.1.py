print("Введите целое число:")
n = int(input())
count = 0
print("Теперь поочередно введите", n, "целых чисел:")
for i in range(n):
    a = int(input())
    if a == 0:
        count += 1
print("Вы ввели", count, "чисел равных нулю.")
