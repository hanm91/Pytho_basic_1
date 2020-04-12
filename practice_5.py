rev = float(input('Введите выручку '))
cost = float(input('Введите издержки '))
profit = rev-cost
if rev>cost:
    ror = profit/rev*100
    print ('Прибыль',round(profit,2))
    print('Рентабельность выручки',round(ror,2))
    work = int(input('Введите численность сотрудников '))
    share = profit/work
    print ('Доля прибыли на одного сотрудника', round(share,2))
elif rev==cost:
    print ('Прибыль равна выручке')
else:
    print('Убыток',round(profit,2)*(-1))

