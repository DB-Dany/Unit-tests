import pytest
from reverse import check_reverse

@pytest.mark.parametrize("input_str,expected", [
    ('!dlroW olleH', 'hello world!'),
    ('AvadaKedavraaaaA!', '!aaaaarvadekadava'),
    ('хаЗерс хишав ХИТЭ в ясларбозар от-ценокан Я', 'я наконец-то разобрался в этих ваших срезах'),
    ('', ''),
    ('a', 'a'),
    ('ABC', 'cba'),
    ('123', '321'),
    ('Hello World', 'dlrow olleh'),
])
def test_reverse(input_str, expected):
    assert check_reverse(input_str) == expected