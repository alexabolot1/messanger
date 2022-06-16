"""
5. Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com и преобразовывает результат
 из байтовового типа данных в строковый без ошибок для любой кодировки операционной системы.
"""

import chardet
import subprocess
import platform

param = '-n' if platform.system().lower() == 'windows' else '-c'
args_for_youtube = ['ping', param, '2', 'youtube.com']
args_for_yandex = ['ping', param, '2', 'yandex.ru']
process_for_youtube = subprocess.Popen(args_for_youtube, stdout=subprocess.PIPE)
process_for_yandex = subprocess.Popen(args_for_yandex, stdout=subprocess.PIPE)
processes = [process_for_youtube, process_for_yandex]
for process in processes:
    for line in process.stdout:
        result = chardet.detect(line)
        print('result = ', result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
