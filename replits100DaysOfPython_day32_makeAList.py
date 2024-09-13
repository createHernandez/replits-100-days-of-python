import random #randint()

greetings_list = ["Bonjour", "Salut", "Hola", "Que tal", "Zdravstvuyte", "Privet", "Nin hao", "Ni hao", "Salve", "Ciao", "Ola", "Oi"]

random_index = random.randint(0, len(greetings_list))

print(f"{greetings_list[random_index]}")