from time import perf_counter
from typing import Sequence
from memory_profiler import memory_usage


def performance_testing(data: Sequence, tests_count: int):
    results_times = []
    results_memories = []
    occurences = []
    for batch in data:
        times_of_batch = []
        memories_of_batch = []
        batch[1] = batch[0] + '#' + batch[1]
        for _ in range(tests_count):
            performance_memory, vals = memory_usage(
                (prefix, (batch[0], batch[1])),
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


def prefix(pattern: str, query: str):
    """This finction find index of first enter pattern in text and returns
    tuple of entres and time in milliseconds."""
    print(end='')
    result = []
    p_list = [0] * len(query)
    start = perf_counter()
    for i in range(1, len(query)):
        temp = p_list[i - 1]
        while temp > 0 and query[i] != query[temp]:
            temp = p_list[temp - 1]
        if query[i] == query[temp]:
            p_list[i] = temp + 1
        else:
            p_list[i] = 0
        if p_list[i] == len(pattern):
            result.append(i - 2 * len(pattern))
    end = perf_counter()
    return result, end - start
