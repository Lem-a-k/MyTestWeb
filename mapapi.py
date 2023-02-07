import requests


def get_map(ll=None, spn=None, map_type="map", add_params=None):
    api_server = "http://static-maps.yandex.ru/1.x/"
    params = {'l': map_type}
    if ll is not None:
        params['ll'] = ll
    if spn is not None:
        params['spn'] = spn
    if add_params is not None:
        params.update(add_params)
    return requests.get(api_server, params)