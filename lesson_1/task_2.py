"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
 а не ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы
  encode, decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных.
"""

WORD_LIST = ['class', 'function', 'method']
bytes_list = []

for word in WORD_LIST:
    bytes_list.append(eval(f"b'{word}'"))

for item in bytes_list:
    print(f'содержимое переменной: {item}')
    print(f'тип переменной: {type(item)}')
    print(f'длина переменной: {len(item)}')
    print('-' * 100)
