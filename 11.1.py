def factorial(n):
    f=1
    for i in range(1, n+1):
        f *= i
        
    return f
list1 = []
a = int(input(f"Введите целое натуральное число: "))
for i in  range(factorial(a), 0, -1):
    list1.append(factorial(i))
print(f"Список факториалов от {factorial(a)} до 1: {list1}")