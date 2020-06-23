needed_xp = float(input())
battles_count = int(input())
total_xp = 0
total_battles = 0
tank_unlocked = False


for battle in range(1, battles_count+1):
    battle_xp = float(input())
    total_xp += battle_xp
    if battle % 3 == 0:
        total_xp += 0.15 * battle_xp
    if battle % 5 == 0:
        total_xp -= 0.1 * battle_xp

    if total_xp >= needed_xp:
        total_battles = battle
        tank_unlocked = True
        break

if tank_unlocked:
    print(f"Player successfully collected his needed experience for {total_battles} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_xp - total_xp:.2f} more needed.")
