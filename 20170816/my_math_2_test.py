# python 3.5.2

from unittest.mock import patch

import pytest

import my_math


class TestFibonacci:
    def test(self):
        assert my_math.fibonacci(1) == 1
        assert my_math.fibonacci(5) == 5
        assert my_math.fibonacci(10) == 55
        assert my_math.fibonacci(20) == 6765
        assert my_math.fibonacci(30) == 832040
        assert my_math.fibonacci(35) == 9227465


class TestSumAll:
    def test(self):
        assert my_math.sum_all(1) == 1
        assert my_math.sum_all(5) == 15
        assert my_math.sum_all(10) == 55
        assert my_math.sum_all(20) == 210
        assert my_math.sum_all(30) == 465
        assert my_math.sum_all(35) == 630


class TestDeltaOfSumAllAndFibonacci:

    @pytest.mark.skip
    def test_slow(self):
        assert my_math.delta_of_sum_all_and_fibonacci(1) == 1 - 1
        assert my_math.delta_of_sum_all_and_fibonacci(5) == 15 - 5
        assert my_math.delta_of_sum_all_and_fibonacci(10) == 55 - 55
        assert my_math.delta_of_sum_all_and_fibonacci(20) \
            == -1 * (210 - 6765)
        assert my_math.delta_of_sum_all_and_fibonacci(30) \
            == -1 * (465 - 832040)
        assert my_math.delta_of_sum_all_and_fibonacci(35) \
            == -1 * (630 - 9227465)

    def test_patch(self):
        with patch('my_math.fibonacci') as mock_fib:
            mock_fib.return_value = 1
            assert my_math.delta_of_sum_all_and_fibonacci(1) == 1 - 1
            mock_fib.return_value = 5
            assert my_math.delta_of_sum_all_and_fibonacci(5) == 15 - 5
            mock_fib.return_value = 55
            assert my_math.delta_of_sum_all_and_fibonacci(10) == 55 - 55
            mock_fib.return_value = 6765
            assert my_math.delta_of_sum_all_and_fibonacci(20) \
                == -1 * (210 - 6765)
            mock_fib.return_value = 832040
            assert my_math.delta_of_sum_all_and_fibonacci(30) \
                == -1 * (465 - 832040)
            mock_fib.return_value = 9227465
            assert my_math.delta_of_sum_all_and_fibonacci(35) \
                == -1 * (630 - 9227465)


class TestSurplusTimeBy:
    def test(self):
        with patch('my_math.time') as mock_time:
            mock_time.time.return_value = 1000
            assert my_math.surplus_time_by(3) == 1
            assert my_math.surplus_time_by(5) == 0
            mock_time.time.return_value = 1001
            assert my_math.surplus_time_by(3) == 2
            assert my_math.surplus_time_by(5) == 1

    def test2(self):
        with patch('my_math.time.time') as mock_time:
            mock_time.return_value = 1000
            assert my_math.surplus_time_by(3) == 1
            assert my_math.surplus_time_by(5) == 0
            mock_time.return_value = 1001
            assert my_math.surplus_time_by(3) == 2
            assert my_math.surplus_time_by(5) == 1
