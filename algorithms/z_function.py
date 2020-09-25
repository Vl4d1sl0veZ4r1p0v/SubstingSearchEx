from time import time
from typing import Sequence, Tuple


def performance_testing(data: Sequence, tests_count: int) -> list:
    result = []
    for batch in data:
        times_of_batch = []
        batch[1] = batch[0] + '#' + batch[1]
        for _ in range(tests_count):
            occurrences, performance_time = z(batch[0], batch[1])
            times_of_batch.append(performance_time)
        result.append(times_of_batch)
    return result


def z(pattern: str, query: str) -> Tuple:
    """This finction find index of first enter pattern in text and returns
    tuple of entres and time in milliseconds."""
    result = []
    left, right = 0, 0
    z_list = [0] * len(query)
    start = time()
    for i in range(1, len(query)):
        if i <= right:
            z_list[i] = min(right - i + 1, z_list[i - left])
        while i + z_list[i] < len(query) \
                and query[z_list[i]] == query[i + z_list[i]]:
            z_list[i] += 1
        if i + z_list[i] - 1 > right:
            left = i
            right = i + z_list[i] - 1
        if len(pattern) == z_list[i]:
            result.append(i)
    end = time()
    return z_list, end - start


if __name__ == "__main__":
    pass
