file_test = open('test_5_2.txt', 'r', encoding= 'utf-8')
content = file_test.read()
print(f'Содержимое файла: \n{content}')

file_test = open('test_5_2.txt', 'r', encoding= 'utf-8')
content = file_test.readlines()
print(f'Количество строк в файле:\n {len(content)}')

file_test = open('test_5_2.txt', 'r', encoding= 'utf-8')
content = file_test.readlines()
for i in range(len(content)):
    print(f'Количество слов на {i+1}-ой строке: \n {len(content[i].split())}')

file_test = open('test_5_2.txt', 'r', encoding= 'utf-8')
content = file_test.read()
content = content.split()
print(f'Общее количество слов:\n {len(content)}')

file_test.close()