cities = {}

while True:
    input_line = input()
    if input_line == "Sail":
        break
    input_line = input_line.split("||")
    city = input_line[0]
    population = int(input_line[1])
    gold = int(input_line[2])
    if city in cities.keys():
        cities[city][0] += population
        cities[city][1] += gold
    else:
        cities[city] = [population, gold]

while True:
    action = input()
    if action == "End":
        break
    action = action.split("=>")
    event = action[0]

    if event == "Plunder":
        city = action[1]
        people = int(action[2])
        gold = int(action[3])

        cities[city][0] -= people
        cities[city][1] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city][0] <= 0 or cities[city][1] <= 0:
            cities.pop(city)
            print(f"{city} has been wiped off the map!")

    elif event == "Prosper":
        city = action[1]
        gold = int(action[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city][1]} gold.")

if cities:
    sorted_cities = sorted(cities.items(), key=lambda kvp: (-kvp[1][1], kvp[0]))
    print(f"Ahoy, Captain! There are {len(sorted_cities)} wealthy settlements to go to:")
    for city in sorted_cities:
        print(f"{city[0]} -> Population: {city[1][0]} citizens, Gold: {city[1][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
