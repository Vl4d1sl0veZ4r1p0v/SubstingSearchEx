import argparse
import numpy as np
import os
import pytest
import sys
from algorithms import boyer_moore_algorithm, bruteforce
from algorithms import prefix_function, rabin_karp_algorithm
from algorithms import z_function
from data_loaders import data_best
from statisticians import plotters


# 892

def check_arguments_first_experiment(tests_count,
                                     algorithm,
                                     substring,
                                     text_filename,
                                     maxlength,
                                     ):
    if 1 <= tests_count \
            and algorithm in globals() \
            and len(substring) \
            and os.path.isfile(text_filename) \
            and 1 <= maxlength <= 100:
        return True
    print("Check failed")
    return False


def first_experiment(parsed_args):
    tests_count = parsed_args.c
    algorithm_name = parsed_args.a
    text_filename = parsed_args.t
    substring = parsed_args.substring
    maxlength = parsed_args.maxlength
    if check_arguments_first_experiment(
            tests_count,
            algorithm_name,
            substring,
            text_filename,
            maxlength,
    ):
        algorithm_tester = globals()[algorithm_name].performance_testing
        results = algorithm_tester(data_best.
                                   generate(max_lenght=maxlength,
                                            substring=substring,
                                            text_filename=text_filename),
                                   tests_count,
                                   )
        results = np.array(results)
        return results


def second_experiment():
    pass


def create_parser():
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
    return parser


def test_first_experiment_works():
    parser = create_parser()
    parsed_args = parser.parse_args(['1',
                                     '5',
                                     "bruteforce",
                                     "./data/Texts/Normal/INP_TEXT",
                                     '-m',
                                     '2',
                                     '-s',
                                     "tree"
                                     ])
    results = first_experiment(parsed_args=parsed_args)
    mask = np.isfinite(results).all(axis=1)
    used_indices = np.where(mask)[0]
    results = results[used_indices]
    assert results.shape == (int(2 * 2661770 / 100 / 1_000), 5)


def test_second_experiment_works():
    parser = create_parser()
    parsed_args = parser.parse_args(['2',
                                     '5',
                                     "bruteforce",
                                     "./data/Texts/Normal/INP_TEXT",
                                     '-l',
                                     '4200',
                                     '-S',
                                     "data/Texts/Normal/substrings.txt"
                                     ])
    assert False


if __name__ == "__main__":
    parser = create_parser()
    parsed_args = parser.parse_args(['1',
                                     '5',
                                     "bruteforce",
                                     "./data/Texts/Normal/INP_TEXT",
                                     '-m',
                                     '10',
                                     '-s',
                                     "tree",
                                     ])
    experiments_list = [first_experiment, second_experiment]
    if 1 <= parsed_args.n <= len(experiments_list):
        results = experiments_list[parsed_args.n - 1](parsed_args=parsed_args)
        print(results.shape)
        mask = np.isfinite(results).all(axis=1)
        used_indices = np.where(mask)[0]
        results = results[used_indices]
        print(results)
