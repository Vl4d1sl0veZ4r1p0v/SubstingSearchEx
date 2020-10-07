from time import time
from typing import Sequence


class BohrVertex:

    def __init__(self):
        pass


class AhoCorasick:
    alf_length = 26
    bohr = []
    pattern = []

    def make_bohr_vertex(self, parent: int, symbol: str):
        vertex = BohrVertex()
        vertex.next_vertex = [-1] * self.alf_length
        vertex.auto_move = [-1] * self.alf_length
        vertex.flag = False
        vertex.suffix_link = -1
        vertex.parent = parent
        vertex.symbol = ord(symbol)
        vertex.suffix_flink = -1
        vertex.pattern_num = -100
        return vertex

    def bohr_init(self):
        self.bohr.append(self.make_bohr_vertex(0, '$'))

    def add_string_to_bohr(self, string: str):
        num = 0
        for i in range(len(string)):
            symbol = ord(string[i]) - ord('a')
            if self.bohr[num].next_vertex[symbol] == -1:
                self.bohr.append(self.make_bohr_vertex(num, chr(symbol)))
                self.bohr[num].next_vertex[symbol] = len(self.bohr) - 1
            num = self.bohr[num].next_vertex[symbol]
        self.bohr[num].flag = True
        self.pattern.append(string)
        self.bohr[num].pattern_num = len(self.pattern) - 1

    def is_string_in_bohr(self, string: str):
        num = 0
        for i in range(len(string)):
            symbol = ord(string[i]) - ord('a')
            if self.bohr[num].next_vertex[symbol] == -1:
                return False
            num = self.bohr[num].next_vertex[symbol]
        return True

    def get_suffix_link(self, vertex_num: int):
        if self.bohr[vertex_num].suffix_link == -1:
            if vertex_num == 0 or self.bohr[vertex_num].parent == 0:
                self.bohr[vertex_num].suffix_link = 0
            else:
                self.bohr[vertex_num].suffix_link = self.get_auto_move(
                    self.get_suffix_link(self.bohr[vertex_num].parent),
                    self.bohr[vertex_num].symbol
                )
        return self.bohr[vertex_num].suffix_link

    def get_auto_move(self, vertex_num: int, symbol: int):
        if self.bohr[vertex_num].auto_move[symbol] == -1:
            if self.bohr[vertex_num].next_vertex[symbol] != -1:
                self.bohr[vertex_num].auto_move[symbol] = \
                    self.bohr[vertex_num].next_vertex[symbol]
            else:
                if vertex_num == 0:
                    self.bohr[vertex_num].auto_move[symbol] = 0
                else:
                    self.bohr[vertex_num].auto_move[symbol] = \
                        self.get_auto_move(
                        self.get_suffix_link(vertex_num),
                        symbol
                    )
        return self.bohr[vertex_num].auto_move[symbol]

    def get_suffix_flink(self, vertex_num: int):
        if self.bohr[vertex_num].suffix_flink == -1:
            u = self.get_suffix_link(vertex_num)
            if u == 0:
                self.bohr[vertex_num].suffix_flink = 0
            else:
                self.bohr[vertex_num].suffix_flink = u if self.bohr[u].flag \
                    else self.get_suffix_flink(u)
        return self.bohr[vertex_num].suffix_flink

    def check(self, vertex_num: int, i: int):
        results = []
        u = vertex_num
        while u != 0:
            if self.bohr[u].flag:
                results.append(i - len(self.pattern[self.bohr[u].pattern_num]))
            u = self.get_suffix_flink(u)
        return results

    def find_all_positions(self, string: str):
        results = []
        u = 0
        for i in range(len(string)):
            u = self.get_auto_move(u, ord(string[i]) - ord('a'))
            tmp = self.check(u, i + 1)
            results.extend(tmp)
        return results


def aho_corasick(pattern: str, query: str):
    results = []
    start = time()
    ahck = AhoCorasick()
    if len(pattern) <= len(query):
        ahck.bohr_init()
        ahck.add_string_to_bohr(pattern)
        results = ahck.find_all_positions(query)
    end = time()
    return results, end - start


def performance_testing(data: Sequence, tests_count: int) -> list:
    result = []
    occurences = []
    for batch in data:
        times_of_batch = []
        for _ in range(tests_count):
            occurrences, performance_time = aho_corasick(batch[0], batch[1])
            times_of_batch.append(performance_time)
        result.append(times_of_batch)
    return result, occurrences


def test_pattern_at_the_beginning():
    query = "abcc"
    pattern = "ab"
    _, occurrences = performance_testing([[pattern, query]], 1)
    assert occurrences == [0]


def test_many_matches():
    query = "abcab"
    pattern = "ab"
    _, occurrences = performance_testing([[pattern, query]], 1)
    assert occurrences == [0, 3]
