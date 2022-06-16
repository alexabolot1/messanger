"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
 В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения
 параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра
  поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list,
   os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например,
   main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС»,
    «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
    (также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных
 в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""

import csv
import chardet
import re


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for i in range(1, 4):
        with open(f'info_{i}.txt', 'rb') as file_obj:
            data_bytes = file_obj.read()
            result = chardet.detect(data_bytes)
            data = data_bytes.decode(result['encoding'])

        os_prod_list.append(re.compile(r'Изготовитель системы:\s*\S*').findall(data)[0].split()[2])
        os_name_list.append(re.compile(r'Windows\s\S*').findall(data)[0])
        os_code_list.append(re.compile(r'Код продукта:\s*\S*').findall(data)[0].split()[2])
        os_type_list.append(re.compile(r'Тип системы:\s*\S*').findall(data)[0].split()[2])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    data_file = [os_prod_list, os_name_list, os_code_list, os_type_list]

    for i in range(len(data_file[0])):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
    return main_data


print(get_data())


def write_to_csv(file_name):
    main_data = get_data()
    with open(file_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in main_data:
            writer.writerow(row)


write_to_csv('data.csv')
