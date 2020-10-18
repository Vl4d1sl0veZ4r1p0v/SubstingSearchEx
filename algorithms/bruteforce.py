import pytest

from memory_profiler import memory_usage
from time import perf_counter
from typing import Sequence


def performance_testing(data: Sequence, tests_count: int):
    results_times = []
    results_memories = []
    occurences = []
    for batch in data:
        times_of_batch = []
        memories_of_batch = []
        for _ in range(tests_count):
            performance_memory, vals = memory_usage(
                (bruteforce, (batch[0], batch[1])),
                retval=True
            )
            occurrences, performance_time = vals
            times_of_batch.append(performance_time)
            memories_of_batch.append(
                max(performance_memory) - min(performance_memory)
            )
        results_times.append(times_of_batch)
        results_memories.append(memories_of_batch)
    return results_times, results_memories, occurrences


def performance_testing_occurences_by_length(
        data: Sequence,
        tests_count: int) -> list:
    result = []
    for batch in data:
        occurrences_of_batch = []
        for _ in range(tests_count):
            occurrences, performance_time = bruteforce(batch[0], batch[1])
            occurrences_of_batch.append(len(occurrences))
        result.append(occurrences_of_batch)
    return result


def bruteforce(pattern: str, query: str):
    print(end='')
    result = []
    start = perf_counter()
    current_progress = 0
    for i in range(len(query)):
        if query[i] == pattern[current_progress]:
            current_progress += 1
            if current_progress == len(pattern):
                result.append(i - len(pattern) + 1)
                current_progress = 0
    end = perf_counter()
    return result, end - start
