# python 3.5.2

import sys

import pytest

import my_math


class TestGetFibonacciByIndex:
    def test(self):
        assert my_math.get_fibonacci_by_index(1) == 1
        assert my_math.get_fibonacci_by_index(2) == 1
        assert my_math.get_fibonacci_by_index(3) == 2
        assert my_math.get_fibonacci_by_index(4) > 2
        assert (my_math.get_fibonacci_by_index(5) == 5) is True

    def test_is_instance(self):
        assert isinstance(my_math.get_fibonacci_by_index(2), int)

    def test_as_array(self):
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        got = []

        for i in range(1, 11):
            got.append(my_math.get_fibonacci_by_index(i))

        assert expected == got

    @pytest.mark.skip
    def test_bool(self):
        with pytest.raises(TypeError):
            my_math.get_fibonacci_by_index(True)
        with pytest.raises(TypeError):
            my_math.get_fibonacci_by_index(False)
