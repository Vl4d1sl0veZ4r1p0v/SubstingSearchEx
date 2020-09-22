from time import time
from typing import Sequence, Tuple


def performance_testing(pattern: str, data: Sequence) -> list:
    """This function returns list of times like O(n+m) by complexity of algorithm."""
    result = []
    for text in data:
        text = pattern + '#' + text
        enters, performance_time = z(pattern, text)
        result.append(performance_time)
    return result


def z(pattern: str, query: str) -> Tuple:
    """This finction find index of first enter pattern in text and returns
    tuple of entres and time in milliseconds."""
    result = []
    l, r = 0, 0
    z_list = [0] * len(query)
    start = time()
    for i in range(1, len(query)):
        if i <= r:
            z_list[i] = min(r - i + 1, z_list[i - l])
        while i + z_list[i] < len(query) \
                and query[z_list[i]] == query[i + z_list[i]]:
            z_list[i] += 1
        if i + z_list[i] - 1 > r:
            l = i
            r = i + z_list[i] - 1
        if len(pattern) == z_list[i]:
            result.append(i)
    end = time()
    return z_list, end - start


if __name__ == "__main__":
    pass
