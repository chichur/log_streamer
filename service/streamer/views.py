# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def read_log(request):
    if request.is_ajax:
        if request.method == 'POST':
            json_data = json.loads(request.body)
            offset = int(json_data.get('offset'))
            module_dir = os.path.dirname(__file__)
            log_file_path = os.path.join(module_dir, 'log_sample.json')
            size_chunk = 34  # размер порции сообщений которую считываем за выполнение запроса

            messages = []
            try:
                #  размеры offset, next_offset, total_size измеряются в байтаx
                total_size = os.path.getsize(log_file_path)
                with open(log_file_path) as f:
                    f.seek(offset)
                    for i in range(size_chunk):
                        if f.tell() < total_size:
                            mes = json.loads(f.readline())
                            messages.append(mes)
                        else:
                            break
                    next_offset = f.tell()
            except ValueError:
                data = {
                    'ok': False,
                    'reason': 'Cursor error'
                }
            except Exception as ex:
                data = {
                    'ok': False,
                    'reason': ex.__repr__()
                }
            else:
                data = {
                    'ok': True,
                    'next_offset': next_offset,
                    'total_size': total_size,
                    'messages': messages
                }

            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')
