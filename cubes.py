from optparse import OptionParser, Values

from draw import *


def parse_option() -> Values:
    parser = OptionParser()
    parser.add_option(
        '-n', '--number', dest='number', help='Number of cubes',
        type=int, default=6
    )
    options, args = parser.parse_args()
    return options


def main():
    options = parse_option()
    number_cubes = options.number
    if not (0 < number_cubes < 7):
        raise ValueError('Number of cubes must be [1, 6]')

    print(draw_head())
    print(draw_stage(5, 1))
    print(draw_middle_row())
    print(draw_stage(5, 2))
    print(draw_middle_row())
    print(draw_stage(5, 3))
    print(draw_footer())


if __name__ == '__main__':
    main()
