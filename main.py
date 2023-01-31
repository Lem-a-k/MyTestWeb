import os
import math

BASE, UNITS = 1024, 'Б'
POWERS = ['', 'К', 'М', 'Г']


def human_read_format(size):
    power = int(math.floor(math.log(size, BASE) if size else 0))
    w = size / BASE ** power
    return f'{round(w)}{POWERS[power] + UNITS}'


def get_files_sizes():
    lines = []
    for item in os.listdir():  # path=os.getcwd()
        if os.path.isfile(item):
            lines.append(f'{item} {human_read_format(os.path.getsize(item))}')
    return '\n'.join(lines)


if __name__ == '__main__':
    print(get_files_sizes())
