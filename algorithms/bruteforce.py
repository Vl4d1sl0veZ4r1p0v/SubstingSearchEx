from time import time
from typing import Sequence

#Need to write a test
def check_results(occurences, reference_occurences):
    print("OK")


def performance_testing(data: Sequence) -> list:
    result = []
    for pattern, text in data:
        occurrences, performance_time = bruteforce(pattern, text)
        result.append(performance_time)
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


def test_bruteforce_if_correctly_finds_occurrences():
    query = "abhhhhhhhab"
    pattern = "ab"
    results, _ = bruteforce(pattern=pattern, query=query)
    assert [0, 9] == results


if __name__ == "__main__":
    pass