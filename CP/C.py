# чтение из json
# запрос к серверу
# datetime
# https://docs.python.org/3/library/datetime.html
import json

with open('') as json_file:
    d = json.load(json_file)
    _ = d
    # получение параметров для запроса и последующей обработки

import requests

# вспосмнть про параметры
response = requests.get(f"http://{_}:{_}").json()

from datetime import datetime
d = datetime.strptime("21/11/06", "%d/%m/%y")
print(d.strftime("%d %m %y"))

# timedelta

#  вывод в консоль
