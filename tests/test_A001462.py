from oeis import A001462
from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=1, max_value=1000))
def test_increasing(n):
    assert A001462[n] <= A001462[n + 1]


@given(integers(min_value=1, max_value=120))
def test_increasing(n):
    assert A001462[n - 1] == A001462[:1820].count(n)


def test_sequence():
    assert A001462[0] == 1
    assert A001462[:84] == [
        1,
        2,
        2,
        3,
        3,
        4,
        4,
        4,
        5,
        5,
        5,
        6,
        6,
        6,
        6,
        7,
        7,
        7,
        7,
        8,
        8,
        8,
        8,
        9,
        9,
        9,
        9,
        9,
        10,
        10,
        10,
        10,
        10,
        11,
        11,
        11,
        11,
        11,
        12,
        12,
        12,
        12,
        12,
        12,
        13,
        13,
        13,
        13,
        13,
        13,
        14,
        14,
        14,
        14,
        14,
        14,
        15,
        15,
        15,
        15,
        15,
        15,
        16,
        16,
        16,
        16,
        16,
        16,
        16,
        17,
        17,
        17,
        17,
        17,
        17,
        17,
        18,
        18,
        18,
        18,
        18,
        18,
        18,
        19,
    ]