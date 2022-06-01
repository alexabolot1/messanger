"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""

WORD_LIST = ['attribute', 'класс', 'функция', 'type']
bytes_list = []

for word in WORD_LIST:
    try:
        bytes_list.append(eval(f"b'{word}'"))
    except SyntaxError as error:
        print(f"Слово '{word}' невозможно записать в байтовом типе  - {error.msg}")

print(f'Слова, успешно записанные в байтовом типе - {bytes_list}')

"""
Синтаксическая ошибка при попытке запустить код - 'SyntaxError: bytes can only contain ASCII literal characters.',
так как кирилица не относится к кодировке ASCII
"""
