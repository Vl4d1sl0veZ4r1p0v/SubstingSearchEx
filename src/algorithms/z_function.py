from time import perf_counter
from typing import Sequence, Tuple
from memory_profiler import memory_usage


def performance_testing(data: Sequence, tests_count: int):
    result_time = []
    occurences = []
    for batch in data:
        times_of_batch = []
        batch[1] = batch[0] + '#' + batch[1]
        for _ in range(tests_count):
            result_memory, vals = memory_usage(
                (z, (batch[0], batch[1])),
                retval=True
            )
            occurrences, performance_time = vals
            times_of_batch.append(performance_time)
        result_time.append(times_of_batch)
    return result_time, result_memory, occurrences


def z(pattern: str, query: str) -> Tuple:
    """This finction find index of first enter pattern in text and returns
    tuple of entres and time in milliseconds."""
    result = []
    left, right = 0, 0
    z_list = [0] * len(query)
    start = perf_counter()
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
            result.append(i - len(pattern) - 1)
    end = perf_counter()
    return result, end - start
