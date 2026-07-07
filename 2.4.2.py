print("Введите целое пятизначное число:")
number = int(input())
12345
one= number % 10
two= (number // 10) % 10
three= (number // 100) % 10
four= (number // 1000) %10
five= number // 10000
print( ((two ** one) * three) / (five - four))