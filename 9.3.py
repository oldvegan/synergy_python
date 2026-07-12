print(f"Введите  последовательность чисел через пробел:")
list1 = list(map(int, input().split()))
set1 = set()
print(f"Проверка повторяемости чисел:")
for i in list1:
    if (i in set1):
        print(f"{i} - YES")
    else:
        print(f"{i} - NO")
    set1.add(i)

