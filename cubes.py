import os
from time import sleep
from random import randint
from optparse import OptionParser, Values

from draw import *


def parse_option() -> Values:
    parser = OptionParser()
    parser.add_option(
        '-n', '--number', dest='number', help='Number of cubes',
        type=int, default=6
    )
    parser.add_option(
        '-d', '--delay', dest='delay', help='Delay (s)',
        type=int, default=15
    )
    options, args = parser.parse_args()
    return options


def generate_vector(number_cubes):
    return [
        randint(1, 6) for i in range(number_cubes)
    ]


def clean_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    options = parse_option()
    number_cubes = options.number
    if not (0 < number_cubes < 7):
        raise ValueError('Number of cubes must be [1, 6]')

    delay = options.delay
    if not (5 <= delay <= 30):
        raise ValueError('Number of cubes must be [10, 30]')

    combination = 1
    while True:
        print(f'{" " * 10 * number_cubes}COMBINATION: {combination}')
        vector = generate_vector(number_cubes)
        for i in range(number_cubes):
            draw_cubes(vector[:i + 1])
        sleep(delay)
        combination += 1
        clean_console()


if __name__ == '__main__':
    main()
