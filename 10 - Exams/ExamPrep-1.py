days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
plunder_collected = 0

for day in range(1, days+1):
    plunder_collected += daily_plunder
    if day % 3 == 0:
        plunder_collected += daily_plunder * 0.5
    if day % 5 == 0:
        plunder_collected *= 0.7

if plunder_collected >= expected_plunder:
    print(f'Ahoy! {plunder_collected:.2f} plunder gained.')
else:
    percent_collected = plunder_collected/expected_plunder*100
    print(f'Collected only {percent_collected:.2f}% of the plunder.')
