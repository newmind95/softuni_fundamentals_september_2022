team_a = [f'A-{football_number}' for football_number in range(1, 12)]
team_b = [f'B-{football_number}' for football_number in range(1, 12)]

cards_list = input().split()
terminated = False

for every_card in cards_list:

    if every_card in team_a:
        team_a.remove(every_card)

    if every_card in team_b:
        team_b.remove(every_card)

    if (len(team_a) < 7) or (len(team_b) < 7):
        terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if terminated:
    print('Game was terminated')
