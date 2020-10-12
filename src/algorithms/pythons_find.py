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
                (pythons_find_, (batch[0], batch[1])),
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


def pythons_find_(pattern: str, query: str):
    print(end='')
    result = []
    start = perf_counter()
    occurence = query.find(pattern)
    while occurence != -1:
        result.append(occurence)
        occurence = query.find(pattern, occurence + 1)
    end = perf_counter()
    return result, end - start
