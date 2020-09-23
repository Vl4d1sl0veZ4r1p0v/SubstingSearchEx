from algorithms import boyer_moore_algorithm, z_function, prefix_function
from algorithms import rabin_karp_algorithm
from data_loaders import data_best

pattern = 'sdafasdf'
testing_data = data_best.generate(5)


def test_z_function():
    assert isinstance(z_function.performance_testing(pattern, testing_data), list)


def test_boyer_moore_algorithm():
    assert isinstance(boyer_moore_algorithm.performance_testing(pattern, testing_data), list)


def test_prefix_function():
    assert isinstance(prefix_function.performance_testing(pattern, testing_data), list)


def test_Rabin_Karp_algorithm():
    assert isinstance(rabin_karp_algorithm.performance_testing(pattern, testing_data), list)


def main():
    pass


if __name__ == '__main__':
    main()
