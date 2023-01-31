import argparse

# prefix_chars='+/' для аргументов в стиле windows
parser = argparse.ArgumentParser()

parser.add_argument('x', type=int)
parser.add_argument('args', nargs='*')  # '+'

parser.add_argument('-l', '--left')

parser.add_argument('-i', '--input', type=argparse.FileType('r'))
parser.add_argument('--log', type=argparse.FileType('a'))

# обязательный
parser.add_argument('-r', '--required', required=True)

# значение по умолчанию
parser.add_argument('--base', default=2, type=int)

# флаги
parser.add_argument('-up', '--up_case', action='store_true')

# варианты
parser.add_argument("--product", choices=['car', 'milk', 'apple'], default='milk')

# сохранить под другим именем
parser.add_argument('--dd-mm-yyyy', dest='date')

# другие действия, например, задать значение другой переменной
parser.add_argument('--no-name', action='store_const', const="no", dest='name')

my_args = parser.parse_args()

# неполный парсинг
# known_args, other_args = parser.parse_known_args()
print(my_args)
print(my_args.x)
print(my_args.required)

