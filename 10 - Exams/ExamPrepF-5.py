import re
num = int(input())

pattern = r"\|[A-Z]{4,}\|:#[A-Za-z]+ [A-Za-z]+#"

for _ in range(num):
    boss = input()
    if re.fullmatch(pattern, boss):
        boss = boss.split("|:#")
        name = boss[0][1:]
        tittle = boss[1][:-1]
        print(f"{name}, The {tittle}")
        print(f">> Strength: {len(name)}")
        print(f">> Armour: {len(tittle)}")
    else:
        print("Access denied!")
