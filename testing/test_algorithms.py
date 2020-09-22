import pytest
from algorithms import boyer_moore_algorithm, z_function, prefix_function
from algorithms import Rabin_Karp_algorithm
from data import data_best


pattern = 'sdafasdf'
testing_data = data_best.generate(5)


def test_z_function():
    assert isinstance(z_function.performance_testing(pattern, testing_data), list)


def test_boyer_moore_algorithm():
    assert isinstance(boyer_moore_algorithm.performance_testing(pattern, testing_data), list)


def test_prefix_function():
    assert isinstance(prefix_function.performance_testing(pattern, testing_data), list)


def test_Rabin_Karp_algorithm():
    assert isinstance(Rabin_Karp_algorithm.performance_testing(pattern, testing_data), list)


def main():
    pass


if __name__ == '__main__':
    main()
