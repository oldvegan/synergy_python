print("Введите слово из маленьких латинских букв")
word=input()
fowel = 0
consonants = 0
a = 0
e = 0
i = 0
o = 0
u = 0
for letter in word:
    if (letter == "a") or (letter == "e") or (letter == "i") or (letter == "o") or (letter == "u"):
        fowel += 1
        if letter == "a":
            a += 1
        elif letter == "e":
            e += 1
        elif letter == "i":
            i += 1
        elif letter == "o":
            o += 1
        elif letter == "u":
            u += 1
    else:
        consonants += 1
print("Глассных:" ,fowel , "Солассных:", consonants)
if a != 0:
    print("a:", a)
else:
    print("a: FALSE")
if e != 0:
    print("e:", e)
else:
    print("e: FALSE")
if i != 0:
    print("i:", i)
else:
    print("i: FALSE")
if o != 0:
    print("o:", o)
else:
    print("o: FALSE")
if u != 0:
    print("u:", u)
else:
    print("u: FALSE")