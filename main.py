import requests
import pygame

def print_error(request_text, response):
    print("Ошибка выполнения запроса:")
    print(request_text)
    print(f"Http статус: {response.status_code} ({response.reason})")
    exit()

apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
place = 'Саратов'
geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={place}&format=json"
response = requests.get(geocoder_request)
if response:
    # Запрос успешно выполнен, печатаем полученные данные.
    # print(response.content)
    result = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    coordinates = result['Point']['pos']
    print(coordinates)

    map_request = f"http://static-maps.yandex.ru/1.x/?ll={','.join(coordinates.split())}&spn=0.005,0.005&l=sat"
    response = requests.get(map_request)

    if not response:
        print_error(map_request, response)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

else:
    print_error(geocoder_request, response)
