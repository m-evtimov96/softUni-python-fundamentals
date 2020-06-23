raw_rey = input()

while True:
    input_line = input()
    if input_line == "Generate":
        print(f"Your activation key is: {raw_rey}")
        break
    input_line = input_line.split(">>>")
    command = input_line[0]

    if command == "Contains":
        substring = input_line[1]
        if substring in raw_rey:
            print(f"{raw_rey} contains {substring}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        flip_type = input_line[1]
        start = int(input_line[2])
        end = int(input_line[3])
        substring = raw_rey[start:end]
        if flip_type == "Upper":
            raw_rey = raw_rey.replace(substring, substring.upper())
        elif flip_type == "Lower":
            raw_rey = raw_rey.replace(substring, substring.lower())
        print(raw_rey)
    elif command == "Slice":
        start = int(input_line[1])
        end = int(input_line[2])
        raw_rey = raw_rey[:start] + raw_rey[end:]
        print(raw_rey)
