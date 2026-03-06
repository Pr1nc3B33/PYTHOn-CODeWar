import pytest

from codewars_solutions import even_or_odd, number_to_string, no_space, get_count


@pytest.mark.parametrize(
    "value, expected",
    [(2, "Even"), (7, "Odd"), (0, "Even"), (-3, "Odd"), (-4, "Even"), (10**9, "Even")],
)
def test_even_or_odd(value, expected):
    assert even_or_odd(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [(67, "67"), (0, "0"), (-12, "-12"), (10**12, "1000000000000")],
)
def test_number_to_string(value, expected):
    assert number_to_string(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("8 j 8   mBliB8g  imjB8B8  jl  B", "8j8mBliB8gimjB8B8jlB"),
        (" no spaces ", "nospaces"),
        ("", ""),
        ("     ", ""),  # edge case: spaces-only input
    ],
)
def test_no_space(value, expected):
    assert no_space(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("abracadabra", 5),
        ("hello world", 3),
        ("my pyx", 0),
        ("aeiou", 5),
        ("", 0),
        ("     ", 0),  # edge case: spaces-only input
    ],
)
def test_get_count(value, expected):
    assert get_count(value) == expected