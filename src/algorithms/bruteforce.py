from time import time
from typing import Sequence


def performance_testing(data: Sequence, tests_count: int) -> list:
    result = []
    for batch in data:
        times_of_batch = []
        for _ in range(tests_count):
            occurrences, performance_time = bruteforce(batch[0], batch[1])
            times_of_batch.append(performance_time)
        result.append(times_of_batch)
    return result


def performance_testing_occurences_by_length(data: Sequence,
                                             tests_count: int) -> list:
    result = []
    for batch in data:
        occurrences_of_batch = []
        for _ in range(tests_count):
            occurrences, performance_time = bruteforce(batch[0], batch[1])
            occurrences_of_batch.append(len(occurrences))
        result.append(occurrences_of_batch)
    return result


def bruteforce(pattern: str, query: str) -> list:
    result = []
    start = time()
    current_progress = 0
    for i in range(len(query)):
        if query[i] == pattern[current_progress]:
            current_progress += 1
            if current_progress == len(pattern):
                result.append(i - len(pattern) + 1)
                current_progress = 0
    end = time()
    return result, end - start


