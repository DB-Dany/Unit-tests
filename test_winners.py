import pytest
from winners import solve

@pytest.mark.parametrize("receipts,expected_result,expected_count", [
    ([123, 145, 346, 246, 235, 166, 112, 351, 436], [346, 166, 436], 3),
    ([123, 145], [], 0),
    ([1, 2, 3], [3], 1),
    ([1, 2, 3, 4, 5, 6], [3, 6], 2),
    ([], [], 0),
    ([1, 2], [], 0),
    (['a', 'b', 'c', 'd', 'e', 'f'], ['c', 'f'], 2),
])
def test_solve(receipts, expected_result, expected_count):
    result, count = solve(receipts)
    assert result == expected_result
    assert count == expected_count