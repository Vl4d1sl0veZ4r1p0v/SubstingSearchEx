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
                (aho_corasick, (batch[0], batch[1])),
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


class BohrVertex:

    def __init__(self):
        pass


class AhoCorasick:

    def __init__(self):
        self.bohr = []
        self.pattern = []

    def make_bohr_vertex(self, parent: int, symbol: str):
        vertex = BohrVertex()
        vertex.next_vertex = {}
        vertex.auto_move = {}
        vertex.flag = False
        vertex.suffix_link = -1
        vertex.parent = parent
        vertex.symbol = symbol
        vertex.suffix_flink = -1
        vertex.pattern_num = -100
        return vertex

    def bohr_init(self):
        self.bohr.append(self.make_bohr_vertex(0, '$'))

    def add_string_to_bohr(self, string: str):
        num = 0
        for i in range(len(string)):
            symbol = string[i]
            if symbol not in self.bohr[num].next_vertex:
                self.bohr.append(self.make_bohr_vertex(num, symbol))
                self.bohr[num].next_vertex[symbol] = len(self.bohr) - 1
            num = self.bohr[num].next_vertex[symbol]
        self.bohr[num].flag = True
        self.pattern.append(string)
        self.bohr[num].pattern_num = len(self.pattern) - 1

    def is_string_in_bohr(self, string: str):
        num = 0
        for i in range(len(string)):
            symbol = string[i]
            if symbol not in self.bohr[num].next_vertex:
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
        if symbol not in self.bohr[vertex_num].auto_move:
            if symbol in self.bohr[vertex_num].next_vertex:
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
            u = self.get_auto_move(u, string[i])
            tmp = self.check(u, i + 1)
            results.extend(tmp)
        return results


def aho_corasick(pattern: str, query: str):
    print(end='')
    results = []
    start = perf_counter()
    ahck = AhoCorasick()
    if len(pattern) <= len(query):
        ahck.bohr_init()
        ahck.add_string_to_bohr(pattern)
        results = ahck.find_all_positions(query)
    end = perf_counter()
    return results, end - start
