import pytest
from season import check_month

@pytest.mark.parametrize("month,expected", [
    (1, "Зима"), (2, "Зима"), (12, "Зима"),
    (3, "Весна"), (4, "Весна"), (5, "Весна"),
    (6, "Лето"), (7, "Лето"), (8, "Лето"),
    (9, "Осень"), (10, "Осень"), (11, "Осень"),
    (0, "Некорректный номер месяца"),
    (13, "Некорректный номер месяца"),
    (-5, "Некорректный номер месяца"),
    (99, "Некорректный номер месяца")
])
def test_season(month, expected):
    assert check_month(month) == expected