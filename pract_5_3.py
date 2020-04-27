data_1 = {'Иванов': 1000, 'Петров': 100, 'Путин': 1090, 'Смит': 200, 'Ломов': 1050, 'Сидоров': 250}
try:
    with open('test_5_3.txt', 'w', encoding= 'utf-8') as my_file:
        for last_name, salary in data_1.items():
            my_file.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка!")

summa = 0
count = 0
last_name = []
with open('test_5_3.txt', 'r', encoding= 'utf-8') as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            last_name.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Оклад менее 200 тыс.: {last_name}")
print(f"Средняя величина дохода: {result}")
