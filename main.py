import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', type=int, default=50)
parser.add_argument('--cars', type=int, default=50)
parser.add_argument('--movie', choices=['melodrama', 'football', 'other'], default='other')

margs = parser.parse_args()

if margs.barbie > 100 or margs.barbie < 0:
    margs.barbie = 50

if margs.cars > 100 or margs.cars < 0:
    margs.cars = 50

margs.movie = (0 if margs.movie == 'melodrama'
               else (100 if margs.movie == 'football' else 50))
boy = int((100 - margs.barbie + margs.cars + margs.movie) / 3)
girl = 100 - boy

print(f"""boy: {boy}
girl: {girl}
""")

