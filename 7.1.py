print(f"Введите строку:")
s = input()
count = 0
for i in range(len(s)):
   if (s[i] == s[-1-i]):
      count += 1
if (count == len(s)):
   print(f"Yes")
else:
   print(f"No")