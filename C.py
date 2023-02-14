# аргументы командной строки (argparse)
# запрос к серверу
# конвертировать json от сервера в csv
# сортировка!

import csv

table = [['QQQ', 33, 6.4], ['AAA', 1, 6.7], ['QQQ', 3, 6.7], ['WWW', 8, 6.4]]
table.sort(key=lambda x: (-x[-1], x[0]), reverse=True)
# table = [{'name': 'QQQ', 'number': 3, 'value': 6.7},
#          {'name': 'W;W;W', 'number': 8, 'value': 6.4}]
titles = ['name', 'number', 'value']
with open("test.csv", "w") as f:
    d_writer = csv.DictWriter(f, fieldnames=titles, delimiter=';', quotechar='"',
                              quoting=csv.QUOTE_ALL, lineterminator='\n')
    d_writer.writeheader()
    for row in table:
        # row = {'name': row[0], 'number': row[1], 'value': row[2]}
        row = dict(zip(titles, row))
        d_writer.writerow(row)
    # d_writer.writerows(table)

