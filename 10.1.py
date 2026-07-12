pets = {}

name = input(f"Введите  Имя питомца:")
species = input(f"Введите  Вид питомца:")
age = int(input(f"Введите  Возраст питомца:"))
owner = input(f"Введите  Имя Владельца:")

pets[name] = {"Вид питомца":species, "Возраст питомца": age, "Имя Владельца": owner}

for i in pets.keys():
    pet_name = i
    ending = "лет"
    pet_species = list(pets[i].values())[0]
    pet_age = list(pets[i].values())[1]
    pet_owner = list(pets[i].values())[2]
    if 11 <= pet_age <= 19:
        ending = "лет"
    elif 2 <= (pet_age % 10) <= 4:
        ending = "года"
    elif (pet_age % 10) == 1:
        ending = "год"
    else:
        ending = "лет"

print(f"Это {pet_species} по кличке {pet_name}. Возраст питомца: {pet_age} {ending}. Имя владельца: {pet_owner}")