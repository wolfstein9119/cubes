ANGEL_LEFT_TOP = '┌'
ANGEL_RIGHT_TOP = '┐'
ANGEL_LEFT_BOTTOM = '└'
ANGEL_RIGHT_BOTTOM = '┘'
HR = '─'
BR = '│'
STAGE_LEFT = '├'
STAGE_RIGHT = '┤'
COLUMN_TOP = '┬'
COLUMN_BOTTOM = '┴'
CROSS = '┼'
PAINTED_CELL = '▒'

ROW_LENGTH = 7

STAGES = {
    1: {
        1: [0, 0, 0],
        2: [0, 1, 0],
        3: [0, 0, 0],
    },
    2: {
        1: [1, 0, 0],
        2: [0, 0, 0],
        3: [0, 0, 1],
    },
    3: {
        1: [1, 0, 0],
        2: [0, 1, 0],
        3: [0, 0, 1],
    },
    4: {
        1: [1, 0, 1],
        2: [0, 0, 0],
        3: [1, 0, 1],
    },
    5: {
        1: [1, 0, 1],
        2: [0, 1, 0],
        3: [1, 0, 1],
    },
    6: {
        1: [1, 0, 1],
        2: [1, 0, 1],
        3: [1, 0, 1],
    },
}


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


RESOLVER = {
    1: BColors.FAIL,
    2: BColors.FAIL,
    3: BColors.FAIL,
    4: BColors.FAIL,
    5: BColors.OKGREEN,
    6: BColors.OKGREEN
}


def check_value(value: int):
    assert 1 <= value <= 6, 'value must be [1, 6]'


def check_stage(stage: int):
    assert 1 <= stage <= 3, 'value must be [1, 3]'


def draw_head() -> str:
    return f'{ANGEL_LEFT_TOP}{HR}{COLUMN_TOP}{HR}{COLUMN_TOP}{HR}{ANGEL_RIGHT_TOP}'


def draw_middle_row() -> str:
    return f'{STAGE_LEFT}{HR}{CROSS}{HR}{CROSS}{HR}{STAGE_RIGHT}'


def draw_footer() -> str:
    return f'{ANGEL_LEFT_BOTTOM}{HR}{COLUMN_BOTTOM}{HR}{COLUMN_BOTTOM}{HR}{ANGEL_RIGHT_BOTTOM}'


def draw_stage(value: int, stage: int) -> str:
    check_value(value)
    check_stage(stage)
    row = BR.join(
        [PAINTED_CELL if STAGES[value][stage][i] else ' ' for i in range(3)]
    )
    return f'{BR}{row}{BR}'


def draw_cube(values: list, resolver=RESOLVER):
    SEPARATOR = '   '
    count_cubes = len(values)

    middle_row = [
        f'{resolver.get(i, "")}{draw_middle_row()}{BColors.ENDC}' for i in values
    ]
    MIDDLE_ROW = SEPARATOR.join(middle_row)

    headers = [
        f'{resolver.get(i, "")}{draw_head()}{BColors.ENDC}' for i in values
    ]
    print(SEPARATOR.join(headers))

    stage1 = [
        f'{resolver.get(i, "")}{draw_stage(i, 1)}{BColors.ENDC}' for i in values
    ]
    print(SEPARATOR.join(stage1))

    print(MIDDLE_ROW)

    stage2 = [
        f'{resolver.get(i, "")}{draw_stage(i, 2)}{BColors.ENDC}' for i in values
    ]
    print(SEPARATOR.join(stage2))

    print(MIDDLE_ROW)

    stage3 = [
        f'{resolver.get(i, "")}{draw_stage(i, 3)}{BColors.ENDC}' for i in values
    ]
    print(SEPARATOR.join(stage3))

    footers = [
        f'{resolver.get(i, "")}{draw_footer()}{BColors.ENDC}' for i in values
    ]
    print(SEPARATOR.join(footers))
