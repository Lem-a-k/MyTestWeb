import os
import random

import pygame

from mapapi import get_map
from business import find_business, find_businesses

MAP_FILE = "map.png"

pt_colors = ['wt', 'do', 'db', 'bl']


class RequestException(Exception):
    pass


class SaveFileException(Exception):
    pass


def get_and_save_image(coordinates, map_type='map', add_params=None):
    response = get_map(coordinates, map_type, add_params=add_params)

    if not response:
        raise RequestException(f"Http статус: {response.status_code} ({response.reason})\n{response.url}")

    map_file = MAP_FILE
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        raise SaveFileException(f'Ошибка записи временного файла: {ex}')


def main():
    coordinates = "37.617779,55.755246"
    # '37.530874,55.703006'  # '46.010245,51.538828'  # '151.21529330927066,-33.85653004033911'
    spn = "0.01,0.01"

    pts = []
    answers = find_businesses(coordinates, spn, "магазин", results=10)
    m1_min, m1_max, m2_min, m2_max = None, None, None, None
    for answer in answers:
        coords = answer['geometry']['coordinates']
        pts.append(','.join(map(str, coords)))
        if m1_min is None or m1_min > coords[0]:
            m1_min = coords[0]
        if m1_max is None or m1_max < coords[0]:
            m1_max = coords[0]
        if m2_min is None or m2_min > coords[1]:
            m2_min = coords[1]
        if m2_max is None or m2_max < coords[1]:
            m2_max = coords[1]
    spn_values = abs(m1_max - m1_min) / 2 + 0.001, abs(m2_max - m2_min) / 2 + 0.001
    print(spn_values)
    print(pts)
    z = 13
    add_params = {'spn': ','.join(map(str, spn_values)),
                  'pt': "~".join(f"{pt},pm{random.choice(pt_colors)}l1" for pt in pts)}
    print(add_params)

    try:
        get_and_save_image(coordinates, map_type='sat', add_params=add_params)
    except (RequestException, SaveFileException) as e:
        print(e)
        exit(0)

    pygame.init()
    screen = pygame.display.set_mode((600, 450))

    clock = pygame.time.Clock()
    fps = 60
    running = True

    screen.blit(pygame.image.load(MAP_FILE), (0, 0))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_PAGEUP, pygame.K_KP_PLUS, pygame.K_PAGEDOWN, pygame.K_KP_MINUS):
                    if event.key in (pygame.K_PAGEUP, pygame.K_KP_PLUS):
                        print('+')
                        change = 1
                    else:
                        print('-')
                        change = -1
                    tmp_z = z + change
                    while 1 <= tmp_z <= 25:
                        try:
                            add_params['z'] = tmp_z
                            get_and_save_image(coordinates, map_type='sat', add_params=add_params)
                        except (RequestException, SaveFileException):
                            tmp_z += change
                        else:
                            z = tmp_z
                            break
                    print(z)
                    screen.blit(pygame.image.load(MAP_FILE), (0, 0))
                    pygame.display.flip()
        # pygame.display.flip()

        clock.tick(fps)

    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove(MAP_FILE)


if __name__ == '__main__':
    main()
