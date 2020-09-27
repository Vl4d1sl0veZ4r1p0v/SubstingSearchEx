import pytest

from algorithms import boyer_moore_algorithm, bruteforce
from algorithms import prefix_function, rabin_karp_algorithm
from algorithms import z_function


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.boyer_moore_search,
                          bruteforce.bruteforce,
                          prefix_function.prefix,
                          rabin_karp_algorithm.rabin_karp,
                          z_function.z])
def test_query_pattern_equality(algorithm):
    query = "ab"
    pattern = "ab"
    results, _ = algorithm(pattern=pattern, query=query)
    assert results == [0]


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.boyer_moore_search,
                          bruteforce.bruteforce,
                          prefix_function.prefix,
                          rabin_karp_algorithm.rabin_karp,
                          z_function.z])
def test_query_smaller_than_pattern(algorithm):
    query = "ab"
    pattern = "abc"
    results, _ = algorithm(pattern=pattern, query=query)
    assert results == []


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.boyer_moore_search,
                          bruteforce.bruteforce,
                          prefix_function.prefix,
                          rabin_karp_algorithm.rabin_karp,
                          z_function.z])
def test_without_a_query(algorithm):
    query = ""
    pattern = "abc"
    results, _ = algorithm(pattern=pattern, query=query)
    assert results == []


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.boyer_moore_search,
                          bruteforce.bruteforce,
                          prefix_function.prefix,
                          rabin_karp_algorithm.rabin_karp,
                          z_function.z])
def test_pattern_at_the_end(algorithm):
    query = "ccab"
    pattern = "ab"
    results, _ = algorithm(pattern=pattern, query=query)
    assert results == [2]


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.boyer_moore_search,
                          bruteforce.bruteforce,
                          prefix_function.prefix,
                          rabin_karp_algorithm.rabin_karp,
                          z_function.z])
def test_pattern_at_the_beginning(algorithm):
    query = "abcc"
    pattern = "ab"
    results, _ = algorithm(pattern=pattern, query=query)
    assert results == [0]


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.boyer_moore_search,
                          bruteforce.bruteforce,
                          prefix_function.prefix,
                          rabin_karp_algorithm.rabin_karp,
                          z_function.z])
def test_no_matches(algorithm):
    query = "aaaaaaaaaaaaaaaaaaa"
    pattern = "akla"
    results, _ = algorithm(pattern=pattern, query=query)
    assert results == []


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.boyer_moore_search,
                          bruteforce.bruteforce,
                          prefix_function.prefix,
                          rabin_karp_algorithm.rabin_karp,
                          z_function.z])
def test_many_matches(algorithm):
    query = "abcab"
    pattern = "ab"
    results, _ = algorithm(pattern=pattern, query=query)
    assert results == [0, 3]
