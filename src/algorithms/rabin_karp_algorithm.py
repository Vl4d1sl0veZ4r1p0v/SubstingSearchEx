from time import perf_counter
from typing import Sequence


def performance_testing(data: Sequence, tests_count: int) -> list:
    result = []
    occurrences = []
    for batch in data:
        times_of_batch = []
        for _ in range(tests_count):
            occurrences, performance_time = rabin_karp(batch[0], batch[1])
            times_of_batch.append(performance_time)
        result.append(times_of_batch)
    return result, occurrences


def get_new_hash(string_hash: int, string: str, i: int,
                 limit: int = int(1e9 + 7), base: int = 13) -> int:
    return ((string_hash * base) % limit + ord(string[i]) % limit) % limit


def rabin_karp(pattern: str, query: str,
               base: int = 7, limit: int = int(1e9 + 7)) -> list:
    result = []
    query_hash = 0
    pattern_hash = 0
    start = perf_counter()
    for i in range(min(len(pattern), len(query))):
        query_hash = get_new_hash(query_hash, query, i)
        pattern_hash = get_new_hash(pattern_hash, pattern, i)
    i = 0
    while i <= len(query) - len(pattern):
        if pattern_hash == query_hash:
            j = 0
            while query[i + j] == pattern[j]:
                j += 1
                if j == len(pattern):
                    result.append(i)
                    break
        i += 1
        if i <= len(query) - len(pattern):
            query_hash = limit + query_hash
            query_hash -= (ord(query[i-1])*base**(len(pattern)-1)) % limit
            query_hash *= base
            query_hash %= limit
            query_hash += ord(query[i + len(pattern) - 1]) % limit
            query_hash %= limit
    if query.endswith(pattern) and len(query) > len(pattern):
        result.append(len(query) - len(pattern))
    end = perf_counter()
    return result, end - start
