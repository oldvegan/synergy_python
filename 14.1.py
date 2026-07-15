my_list = [0, 1, 2]

def result(l, n=0):
    if n >= len(l):
        return print(f"Конец списка")
    print(l[n])
    result(l, n+1)
    
result(my_list)
