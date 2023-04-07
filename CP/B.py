# argparse
# csv - чтение
# json - вывод
import argparse

parser = argparse.ArgumentParser()
parser.add_argument()  # файл, перечисляемое */+,
                       # значения по умолчанию, флажок
args = parser.parse_args()

import csv

with open(args.file) as csv_file:
    csv.reader()  # delimiter
    csv.DictReader()
    # строковые не забыть преобразовать
# "перекладывание" в словарик/список

import json

with open(args.out_file, 'w') as json_file:
    json.dump('result', json_file, indent=True)  # в файл
# json.dumps()  # в строку
