import pytest

from algorithms import boyer_moore_algorithm, bruteforce
from algorithms import prefix_function, rabin_karp_algorithm
from algorithms import z_function


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing])
def test_query_pattern_equality(algorithm):
    query = "ab"
    pattern = "ab"
    _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == [0]


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing])
def test_query_smaller_than_pattern(algorithm):
    query = "ab"
    pattern = "abc"
    _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == []


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing])
def test_without_a_query(algorithm):
    query = ""
    pattern = "abc"
    _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == []


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing])
def test_pattern_at_the_end(algorithm):
    query = "ccab"
    pattern = "ab"
    _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == [2]


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing])
def test_pattern_at_the_beginning(algorithm):
    query = "abcc"
    pattern = "ab"
    _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == [0]


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing])
def test_no_matches(algorithm):
    query = "aaaaaaaaaaaaaaaaaaa"
    pattern = "akla"
    _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == []


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing])
def test_many_matches(algorithm):
    query = "abcab"
    pattern = "ab"
    _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == [0, 3]
