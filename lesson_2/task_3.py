"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных
в файле YAML-формата. Для этого:

    Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
    третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
     отсутствующим в кодировке ASCII (например, €);
    Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
     При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность
      работы с юникодом: allow_unicode = True;

    Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

"""
import yaml

MY_DICT_IN = {'key_1': ['привет', 'world'],
              'key_2': 100500,
              'key_3': {'number_1': '15€'}}

with open('task_3.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(MY_DICT_IN, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open("task_3.yaml", 'r', encoding='utf-8') as f:
    MY_DICT_OUT = yaml.load(f, Loader=yaml.SafeLoader)

print(MY_DICT_IN)
print(MY_DICT_OUT)
print(MY_DICT_IN == MY_DICT_OUT)
