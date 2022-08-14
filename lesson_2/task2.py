"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(data, type(data))

    with open('orders.json', 'w', encoding='utf-8') as f:
        orders_list = data['orders']
        order_item = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        orders_list.append(order_item)
        json.dump(data, f, indent=4, ensure_ascii=False)


write_order_to_json('мяч', 2, 1000, 'alex', '22.05.2022')
write_order_to_json('кроссовки', 1, 5000, 'maria', '11.05.2022')
