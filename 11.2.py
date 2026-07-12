import collections

pets = {1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"},
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"},
        }}

def create():
    last = collections.deque(pets, maxlen=1)[0]
    last += 1
    name = input(f"Введите  Имя питомца: ")
    species = input(f"Введите  Вид питомца: ")
    age = int(input(f"Введите  Возраст питомца: "))
    owner = input(f"Введите  Имя Владельца: ")
    pets[last] = {name: {"Вид питомца":species, "Возраст питомца": age, "Имя владельца": owner}}

def update():
    number = int(input("Введите номер питомца, которого будем менять: "))
    if number in pets.keys():
        name = input(f"Введите актуальное Имя питомца: ")
        species = input(f"Введите актуальный Вид питомца: ")
        age = int(input(f"Введите актуальный Возраст питомца: "))
        owner = input(f"Введите актуальное Имя Владельца: ")
        pets[number] = {name: {"Вид питомца":species, "Возраст питомца": age, "Имя владельца": owner}}
    else:
        print(f"Такого номера не существует")

def delete():
    number = int(input("Введите номер питомца, которого будем удалять: "))
    if number in pets.keys():
       del pets[number]
    else:
        print(f"Такого номера не существует")

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
    if 11 <= age <= 19:
        return "лет"
    elif 2 <= age % 10 <= 4:
        return "года"
    elif age % 10 == 1:
        return "год"
    else:
        return "лет"

def pets_list():
    for i in pets:
        print(pets[i])

def read():
    id = int(input("Введите номер питомца: "))
    if id in pets.keys():
        pet_name = list(get_pet(id).keys())[0]
        pet_species = get_pet(id)[pet_name]["Вид питомца"]
        pet_age = get_pet(id)[pet_name]["Возраст питомца"]
        pet_owner = get_pet(id)[pet_name]["Имя владельца"]
        print(f"Это {pet_species} по кличке {pet_name}. Возраст питомца: {pet_age} {get_suffix(pet_age)}. Имя владельца: {pet_owner}")
    else:
        print(f"Такого номера не существует.")

recommand = "start"
while command != 'stop':
    command = input("Введите команду: ")
    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "stop":
        print(f"Выход из программы")    
    else:
        print(f"Введена некорректная команда")