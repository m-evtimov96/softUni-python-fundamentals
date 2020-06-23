def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


key_materials = {
    "fragments": 0,
    "shards": 0,
    "motes": 0
}

legendary_items = {
    "fragments": "Valanyr",
    "shards": "Shadowmourne",
    "motes": "Dragonwrath"
}

junk = {}
legendary_item = ""

while legendary_item == "":
    input_line = input().lower().split()
    for thing in range(0, len(input_line), 2):
        amount = int(input_line[thing])
        material = input_line[thing + 1]

        if material in key_materials:
            key_materials[material] += amount

            if key_materials[material] >= 250:
                legendary_item = material
                key_materials[material] -= 250
                break
        else:
            junk.setdefault(material, 0)
            junk[material] += amount

key_materials = dict(sorted(key_materials.items(), key=lambda el: (-el[1], el[0])))
junk = dict(sorted(junk.items()))
print(f"{legendary_items[legendary_item]} obtained!")
print_dict(key_materials, "{}: {}")
print_dict(junk, "{}: {}")
