"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
 Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в неизвестной
 кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.
"""

import locale

resurs_string = ['сетевое программирование', 'сокет', 'декоратор']

with open('resurs.txt', 'w+') as f:
    for i in resurs_string:
        f.write(i + '\n')

file_coding = locale.getpreferredencoding()

with open('resurs.txt', 'r', encoding=file_coding) as f:
    for file_string in f.readlines():
        print(file_string)
