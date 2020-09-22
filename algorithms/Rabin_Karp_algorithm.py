from time import time
from typing import Sequence, Tuple


def performance_testing(pattern: str, data: Sequence) -> list:
    """This function returns list of times like O(n+m) by complexity of algorithm."""
    result = []
    for text in data:
        enters, performance_time = rabin_karp(pattern, text)
        result.append(performance_time)
    return result


def get_new_hash(string_hash: int, string: str, i: int,
                 limit: int = int(1e9 + 7), base: int = 13) -> int:
    return ((string_hash * base) % limit + ord(string[i]) % limit) % limit


def rabin_karp(pattern: str, query: str,
               base: int = 13, limit: int = int(1e9 + 7)) -> list:
    result = []
    query_hash = 0
    pattern_hash = 0
    start = time()
    for i in range(len(pattern)):
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
            text_hash = limit + query_hash
            text_hash -= (ord(query[i - 1]) * base ** (len(pattern) - 1)) % limit
            text_hash *= base
            text_hash %= limit
            text_hash += ord(query[i + len(pattern) - 1]) % limit
            text_hash %= limit
    end = time()
    return result, end - start


if __name__ == "__main__":
    pass