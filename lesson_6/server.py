import socket
import sys
import argparse
import json
import logging
from errors import IncorrectDataRecivedError
from lesson_5.common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, DEFAULT_PORT, MAX_CONNECTIONS, ERROR
from lesson_5.common.utils import get_message, send_message
from decos import log

# Инициализация логирования сервера.
LOGGER = logging.getLogger('server')


@log
def process_client_message(message):
    LOGGER.debug(f'Разбор сообщения от клиента : {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and \
            USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


@log
def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    return parser


def main():
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p

    # проверка получения корретного номера порта для работы сервера.
    if not 1023 < listen_port < 65536:
        LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта '
                        f'{listen_port}. Допустимы адреса с 1024 до 65535.')
        sys.exit(1)
    LOGGER.info(f'Запущен сервер, порт для подключений: {listen_port}, '
                f'адрес с которого принимаются подключения: {listen_address}. '
                f'Если адрес не указан, принимаются соединения с любых адресов.')
    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        LOGGER.info(f'Установлено соедение с ПК {client_address}')
        try:
            message_from_client = get_message(client)
            LOGGER.debug(f'Получено сообщение {message_from_client}')
            response = process_client_message(message_from_client)
            LOGGER.info(f'Сформирован ответ клиенту {response}')
            send_message(client, response)
            LOGGER.debug(f'Соединение с клиентом {client_address} закрывается.')
            client.close()
        except json.JSONDecodeError:
            LOGGER.error(f'Не удалось декодировать Json строку, полученную от '
                         f'клиента {client_address}. Соединение закрывается.')
            client.close()
        except IncorrectDataRecivedError:
            LOGGER.error(f'От клиента {client_address} приняты некорректные данные. '
                         f'Соединение закрывается.')
            client.close()


if __name__ == '__main__':
    main()
