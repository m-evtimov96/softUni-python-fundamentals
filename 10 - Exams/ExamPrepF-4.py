skill = input()

while True:
    input_line = input()
    if input_line == "For Azeroth":
        break
    input_line = input_line.split()
    command = input_line[0]

    if command == "GladiatorStance":
        skill = skill.upper()
        print(skill)
    elif command == "DefensiveStance":
        skill = skill.lower()
        print(skill)
    elif command == "Dispel":
        index = int(input_line[1])
        letter = input_line[2]
        if index < len(skill):
            skill = list(skill)
            skill[index] = letter
            skill = "".join(skill)
            print("Success!")
        else:
            print("Dispel too weak.")

    elif command == "Target":
        target_type = input_line[1]
        if target_type == "Change":
            old_substring = input_line[2]
            new_substring = input_line[3]
            skill = skill.replace(old_substring, new_substring)
            print(skill)
        elif target_type == "Remove":
            to_remove = input_line[2]
            skill = skill.replace(to_remove, '')
            print(skill)
        else:
            print("Command doesn't exist!")
    else:
        print("Command doesn't exist!")
