print("Введите минимальную сумму инвестиций:")
summa = int(input())
print("Введите количество денег у Майкла:")
mike = int(input())
print("Введите количество денег у Ивана:")
ivan = int(input())
if mike >= summa :
    if ivan >= summa :
        print("2")
    else:
        print("Mike")
elif ivan >= summa :
    print("Ivan")
elif (mike + ivan) >= summa :
    print("1")
else:
    print("0")