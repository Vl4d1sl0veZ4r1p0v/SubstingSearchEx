from time import time
from typing import Sequence, Tuple


def performance_testing(pattern: str, data: Sequence) -> list:
    """This function returns list of times
    like O(n+m) by complexity of algorithm."""
    result = []
    for text in data:
        enters, performance_time = boyer_moore_search(pattern, text)
        result.append(performance_time)
    return result


def z_array(query: str) -> list:
    left, right = 0, 0
    z_list = [0] * len(query)
    for i in range(1, len(query)):
        if i <= right:
            z_list[i] = min(right - i + 1, z_list[i - left])
        while i + z_list[i] < len(query) \
                and query[z_list[i]] == query[i + z_list[i]]:
            z_list[i] += 1
        if i + z_list[i] - 1 > right:
            left = i
            right = i + z_list[i] - 1
    return z_list


def get_small_l(z_array_by_pattern: list) -> list:
    small_lp = [0] * len(z_array_by_pattern)
    for i in range(len(z_array_by_pattern)):
        if z_array_by_pattern[i] == i + 1:
            small_lp[len(z_array_by_pattern) - i - 1] = i + 1
    for i in range(len(z_array_by_pattern) - 2, -1, -1):
        if small_lp[i] == 0:
            small_lp[i] = small_lp[i + 1]
    return small_lp


def good_suffix_precalc(pattern: str) -> Tuple:
    z_array_by_pattern = z_array(pattern[::-1])[::-1]
    l_by_pattern = [0] * len(pattern)
    for j in range(len(pattern) - 1):
        if z_array_by_pattern[j] > 0:
            l_by_pattern[len(pattern) - z_array_by_pattern[j]] = j + 1
    return [l_by_pattern[0]] + [max(l_by_pattern[i], l_by_pattern[i - 1])
                                for i in range(1, len(pattern))],\
        get_small_l(z_array_by_pattern)


def get_shift_bad_character(text: str) -> dict:
    result = {}
    for i in range(len(text)):
        result[text[i]] = i + 1
    return result


def get_shift_good_suffix(i: int, big_l: list, small_l_prime: list) -> int:
    assert i < len(big_l)
    if i == len(big_l) - 1:
        return 0
    i += 1
    if big_l[i] > 0:
        return len(big_l) - big_l[i]
    return len(big_l) - small_l_prime[i]


def boyer_moore_search(pattern: str, query: str) -> Tuple:
    result = []
    shift_bad_character = get_shift_bad_character(pattern)
    big_l, small_l_prime = good_suffix_precalc(pattern)
    shift_good_suffix = [get_shift_good_suffix(i, big_l, small_l_prime)
                         for i in range(len(pattern))]
    start = time()
    i = 0
    while i <= len(query) - len(pattern):
        j = len(pattern)
        for j in range(len(pattern) - 1, -1, -1):
            if pattern[j] != query[i + j]:
                shift_by_bad_character = shift_bad_character[pattern[j]] if \
                    query[i + j] not in shift_bad_character else 1
                i += max(shift_by_bad_character, shift_good_suffix[j])
                break
        else:
            result.append(i)
            i += max(1, shift_good_suffix[j])
    end = time()
    return result, end - start


def main():
    pattern = 'aa'
    text = 'a' * 10
    print(boyer_moore_search(pattern, text))


if __name__ == '__main__':
    main()
