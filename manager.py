import argparse
import numpy as np
import pytest
import sys
import algorithms
from statisticians import plotters


# 892

def check_arguments_first_experiment(tests_count,
                                     algorithm,
                                     substring,
                                     text_filename,
                                     maxlength,
                                     ):
    return False


def first_experiment(parsed_args):
    tests_count = parsed_args.count
    algorithm_name = parsed_args.algorithm_name
    substring = parsed_args.substring
    text_filename = parsed_args.text_filename
    maxlength = parsed_args.maxlength
    if check_arguments_first_experiment(
            tests_count,
            algorithm_name,
            substring,
            text_filename,
            maxlength,
    ):
        algorithm_tester = getattr(algorithms, algorithm_name).performance_testing
        with open(text_filename, 'rt') as fin:
            text = fin.read()
            length = maxlength * 100 / len(text)
            text = text[:length]
        results = []
        for _ in range(tests_count):
            results.append(algorithm_tester(substring, text))
        results = np.array(results)
        plotters.complete(results)


def second_experiment():
    pass


def parser_do():
    parser = argparse.ArgumentParser(description='Manager of tests',
                                     add_help=True)
    parser.add_argument('n', action='store', type=int)
    parser.add_argument('c', action='store', type=int,
                        help="number of test runs")
    parser.add_argument('a', action='store',
                        help="tested algorithm")
    parser.add_argument('t', action='store',
                        help="path to text")
    parser.add_argument('-l', action='store', dest="length", type=int,
                        help="maximum text length")
    parser.add_argument('-s', action='store', dest="substring",
                        help="substring to search")
    parser.add_argument('-m', action='store', dest="maxlength", type=int,
                        help="maximum percentage of text that can be selected")
    parser.add_argument('-S', action='store', dest="substrings_filename",
                        help="path to substrings")
    return parser.parse_args()


if __name__ == "__main__":
    parsed_args = parser_do()
    experiments_list = [first_experiment, second_experiment]
    if 1 <= parsed_args.n <= len(experiments_list):
        experiments_list[parsed_args.n]()
