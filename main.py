from zipfile import ZipFile

with ZipFile('TestZip.zip') as my_zip:
    with my_zip.open('input.txt') as file:
        print(file.read().decode('utf-8'))