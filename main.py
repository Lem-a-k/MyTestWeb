import sys

from geocoder import get_ll_span
from mapapi_PG import show_map

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])

ll, span = get_ll_span(toponym_to_find)

show_map(ll, span, map_type='sat')