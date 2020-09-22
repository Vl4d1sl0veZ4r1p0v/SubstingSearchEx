from time import time
from typing import Sequence


def performance_testing(pattern: str, data: Sequence) -> list:
    """This finction returns list of times like O(n+m) by complexity of algirithm."""
    result = []
    for text in data:
        text = pattern + '#' + text
        enters, performance_time = prefix(pattern, text)
        result.append(performance_time)
    return result


def prefix(pattern: str, query: str) -> list:
    """This finction find index of first enter pattern in text and returns
    tuple of entres and time in milliseconds."""
    result = []
    p_list = [0] * len(query)
    start = time()
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
    end = time()
    return result, end - start


if __name__ == "__main__":
    pass