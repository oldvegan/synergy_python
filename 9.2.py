print(f"Введите через пробел числа первого списка:")
list1 = set(map(int, input().split()))
print(f"Введите через пробел числа второго списка:")
list2 = set(map(int, input().split()))
list3 = list1.intersection(list2)
print(f"Введено {len(list3)} чисел, содержащихся как в 1, так и во 2 списках")

