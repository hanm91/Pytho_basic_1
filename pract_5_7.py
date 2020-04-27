import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('test_5_7.txt', 'r', encoding= 'utf-8') as file:
    for line in file:
        name, firm, revenue, costs = line.split()
        profit[name] = int(revenue) - int(costs)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:}')
    else:
        print(f'Прибыли нет')
    pr = {'Средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('test_5_7.json', 'w', encoding= 'utf-8') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
