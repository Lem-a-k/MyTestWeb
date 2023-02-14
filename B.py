# чтение json'а
# конструирование и отправка запроса (requests)
# вывод вещественного с точностью


# для тренировки решим get 2 + 2
# import requests
#
# server = input()
# port = input()
# a = input()
# b = input()
#
# # request = f'{server}:{port}?a={a}&b={b}'
# # response = requests.get(request)
#
# params = {'a': a, 'b': b}
# response = requests.get(f'{server}:{port}', params=params)
#
# # print(response.url)
# json_response = response.json()
# print(*sorted(json_response['result']))
# print(json_response['check'])
#
# # если сервер дан без протокола server='127.0.0.1'
# request = f'http://{server}:{port}?a={a}&b={b}'
# response = requests.get(f'http://{server}:{port}', params=params)
#
# если параметры надо прочитать из json-файла

import json

file_name = input()
with open(file_name, encoding='utf-8') as in_json:
    d = json.load(in_json)

# дальше см. выше

result = {'a': [1, 8, 5, 3, 2.3, 3], 'b': [0, 0, 6, 4], 'm': [8, 1.01, 12, 3, 3], 'z': []}
# среднее арифм./геометрич., формула будет
# максимальное среднее арифметическое
res = max(sum(v)/len(v) for v in result.values() if v)
# точность
print(f'{res:.5f}')
print(round(res, 5))
