# -*- coding: utf-8 -*-

# Клиент для отправки запросов на бэкэнд
import json
import requests

URL = 'http://127.0.0.1:8000/read_log/'

offset = 0
while True:
    json_post = {"offset": str(offset)}
    req = requests.post(URL, json=json_post)
    data = json.loads(req.content)
    if data.get('ok'):
        total_size = data.get('total_size')
        offset = str(data.get('next_offset'))
        for mes in data.get('messages'):
            print mes, type(mes)
        if int(offset) == total_size:
            break
    else:
        print 'Ошибка', data.get('reason')
        break
