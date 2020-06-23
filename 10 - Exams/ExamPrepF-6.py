heroes = {}

while True:
    input_line = input()
    if input_line == "End":
        break
    command_line = input_line.split()
    command = command_line[0]
    name = command_line[1]

    if command == "Enroll":
        if name not in heroes.keys():
            heroes[name] = []
        else:
            print(f"{name} is already enrolled.")
    elif command == "Learn":
        spell = command_line[2]
        if name not in heroes.keys():
            print(f"{name} doesn't exist.")
        else:
            if spell in heroes[name]:
                print(f"{name} has already learnt {spell}.")
            else:
                heroes[name].append(spell)
    elif command == "Unlearn":
        spell = command_line[2]
        if name not in heroes.keys():
            print(f"{name} doesn't exist.")
        else:
            if spell not in heroes[name]:
                print(f"{name} doesn't know {spell}.")
            else:
                heroes[name].remove(spell)
sorted_heroes = sorted(heroes.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

print("Heroes:")
for hero, spells in sorted_heroes:
    print(f"== {hero}: ", end="")
    print(", ".join(spells))
