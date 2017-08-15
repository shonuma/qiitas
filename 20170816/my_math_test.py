# python 3.5.2

import pytest

import my_math


class TestFibonacci:
    def test(self):
        assert my_math.fibonacci(1) == 1
        assert my_math.fibonacci(2) == 1
        assert my_math.fibonacci(3) == 2
        assert my_math.fibonacci(4) > 2
        assert (my_math.fibonacci(5) == 5) is True

    def test_is_instance(self):
        assert isinstance(my_math.fibonacci(2), int)

    def test_as_array(self):
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        got = []

        for i in range(1, 11):
            got.append(my_math.fibonacci(i))

        assert expected == got

    def test_bool(self):
        with pytest.raises(TypeError):
            my_math.fibonacci(True)
        with pytest.raises(TypeError):
            my_math.fibonacci(False)


class TestSumAll:
    def test(self):
        assert my_math.sum_all(1) == 1
        assert my_math.sum_all(2) == 3
        assert my_math.sum_all(3) == 6
        assert my_math.sum_all(4) == 10
        assert my_math.sum_all(5) == 15
