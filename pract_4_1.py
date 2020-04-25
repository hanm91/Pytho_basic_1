from sys import argv

_, time, production, bonus = argv

time = float(time)
production = floa(production)
bonus = floa(bonus)

res = time * production + bonus


print(f'Заработная плата сотрудника составляет {res}')


