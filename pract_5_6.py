dict_1 = {}
with open('test_5_6.txt', 'r', encoding= 'utf-8') as f_obj:
    for line in f_obj:
        tmp_list = line.split(":")
        numbers_string = tmp_list[1].replace("(", " ").replace(")", " ")
        tmp_numbers_list = [int(s) for s in numbers_string.split() if s.isdigit()]
        dict_1[tmp_list[0]] = sum(tmp_numbers_list)
print(dict_1)

