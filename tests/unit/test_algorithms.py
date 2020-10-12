import pytest

from algorithms import aho_corasick
from algorithms import boyer_moore_algorithm, bruteforce
from algorithms import prefix_function, pythons_find
from algorithms import rabin_karp_algorithm
from algorithms import z_function


def test_aho_corasick_many_strings_in_bohr():
    ahck = aho_corasick.AhoCorasick()
    ahck.bohr_init()
    ahck.add_string_to_bohr("abc")
    ahck.add_string_to_bohr("bc")
    ahck.add_string_to_bohr("cccb")
    ahck.add_string_to_bohr("bcdd")
    ahck.add_string_to_bohr("bbbc")
    assert ahck.find_all_positions(
        "abcdcbcddbbbcccbbbcccbb"
    ) == [0, 1, 5, 5, 9, 11, 12, 15, 17, 18]


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing,
                          aho_corasick.performance_testing,
                          pythons_find.performance_testing])
def test_query_pattern_equality(algorithm):
    query = "ab"
    pattern = "ab"
    _, _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == [0]


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing,
                          aho_corasick.performance_testing,
                          pythons_find.performance_testing])
def test_query_smaller_than_pattern(algorithm):
    query = "ab"
    pattern = "abc"
    _, _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == []


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing,
                          aho_corasick.performance_testing,
                          pythons_find.performance_testing])
def test_without_a_query(algorithm):
    query = ""
    pattern = "abc"
    _, _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == []


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing,
                          aho_corasick.performance_testing,
                          pythons_find.performance_testing])
def test_pattern_at_the_end(algorithm):
    query = "ccab"
    pattern = "ab"
    _, _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == [2]


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing,
                          aho_corasick.performance_testing,
                          pythons_find.performance_testing])
def test_pattern_at_the_beginning(algorithm):
    query = "abcc"
    pattern = "ab"
    _, _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == [0]


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing,
                          aho_corasick.performance_testing,
                          pythons_find.performance_testing])
def test_no_matches(algorithm):
    query = "aaaaaaaaaaaaaaaaaaa"
    pattern = "akla"
    _, _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == []


@pytest.mark.parametrize('algorithm',
                         [boyer_moore_algorithm.performance_testing,
                          bruteforce.performance_testing,
                          prefix_function.performance_testing,
                          rabin_karp_algorithm.performance_testing,
                          z_function.performance_testing,
                          aho_corasick.performance_testing,
                          pythons_find.performance_testing])
def test_many_matches(algorithm):
    query = "abcab"
    pattern = "ab"
    _, _, occurrences = algorithm([[pattern, query]], 1)
    assert occurrences == [0, 3]
