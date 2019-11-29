from oeis import A001622
from hypothesis import given
from hypothesis.strategies import integers


def test_sequence():
    assert A001622() == [1, 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2]
    assert A001622(20, 15) == [0, 4, 5, 8, 6, 8, 3, 4, 3, 6, 5, 6, 3, 8, 1]
    assert A001622(limit=105) == [
        1,
        6,
        1,
        8,
        0,
        3,
        3,
        9,
        8,
        8,
        7,
        4,
        9,
        8,
        9,
        4,
        8,
        4,
        8,
        2,
        0,
        4,
        5,
        8,
        6,
        8,
        3,
        4,
        3,
        6,
        5,
        6,
        3,
        8,
        1,
        1,
        7,
        7,
        2,
        0,
        3,
        0,
        9,
        1,
        7,
        9,
        8,
        0,
        5,
        7,
        6,
        2,
        8,
        6,
        2,
        1,
        3,
        5,
        4,
        4,
        8,
        6,
        2,
        2,
        7,
        0,
        5,
        2,
        6,
        0,
        4,
        6,
        2,
        8,
        1,
        8,
        9,
        0,
        2,
        4,
        4,
        9,
        7,
        0,
        7,
        2,
        0,
        7,
        2,
        0,
        4,
        1,
        8,
        9,
        3,
        9,
        1,
        1,
        3,
        7,
        4,
        8,
        4,
        7,
        5,
    ]


@given(integers(min_value=0, max_value=200), integers(min_value=1, max_value=200))
def test_sequence_length(start, limit):
    assert len(A001622(start, limit)) == limit


@given(integers(min_value=0, max_value=1000))
def test_A001622(limit):
    assert A001622(limit=limit + 1)[:-1] == A001622(limit=limit)