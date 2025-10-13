MIN_COUNT        = 0
MAX_COUNT        = 100
ROWS_COUNT       = 5
COLS_COUNT       = 6

DOT              = "."
SPACE            = " "
ALPHABET         = "abcdefghijklmnopqrstuvwxyz"

MIN_DATA_LEN     = 1
MAX_DATA_LEN     = 20

WRONG_NUMBER_MSG = 'Ожидалось число, а получено "{0}"'

WRONG_DATA_LEN_ERROR_MSG = (
    f'Слово "{{0}}" должно содержать минимум {MIN_DATA_LEN} символ'
    f' и максимум {MAX_DATA_LEN} символов'
)

WRONG_DATA_FORMAT_ERROR_MSG = (
    f'Слово "{{0}}" должно состоять только'
    ' из маленьких латинских символов'
)

WRONG_RANGE_MSG = (
    f'Количество не соответствует требованиям: '
    f'{MIN_COUNT} <= "{{0}}" <= {MAX_COUNT}'
)
