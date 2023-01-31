import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', type=int, default=50)
parser.add_argument('--cars', type=int, default=50)
parser.add_argument('--movie', choices=['melodrama', 'football', 'other'], default='other')

margs = parser.parse_args()

if margs.barbie > 100 or margs.barbie < 0:
    margs.barbie = 50
print(margs.barbie)