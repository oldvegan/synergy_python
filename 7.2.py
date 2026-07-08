print(f"введите строку с пробелами подряд внутри:")
s = input()
new = " ".join(s.split())
print(f"Измененная строка: {new}")