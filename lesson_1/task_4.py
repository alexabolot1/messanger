"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
 и выполнить обратное преобразование (используя методы encode и decode).
"""

WORD_LIST = ['разработка', 'администрирование', 'protocol', 'standard']

for word in WORD_LIST:
    word_bytes = word.encode('utf-8')
    print(word_bytes, type(word_bytes))
    word_str = word_bytes.decode('utf-8')
    print(word_str, type(word_str))
    print('-' * 100)
