import argparse
import json
import numpy as np
import os
import pytest

from algorithms import boyer_moore_algorithm, bruteforce
from algorithms import prefix_function, rabin_karp_algorithm
from algorithms import z_function
from data_loaders import data_best, data_amorotized
from statisticians.simple_statiscian import Statiscian


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


def check_arguments_second_experiment(tests_count,
                                      algorithm,
                                      text_filename,
                                      substrings_filename,
                                      length,
                                      ):
    if 1 <= tests_count \
            and algorithm in globals() \
            and os.path.isfile(text_filename) \
            and os.path.isfile(substrings_filename) \
            and 1 <= length:
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
                                   generate(maxlength,
                                            substring,
                                            text_filename),
                                   tests_count,
                                   )
        results = np.array(results)
        return results


def preparation_for_second_experiment(substrings_filename: str,
                                      text_filename: str,
                                      length: int):
    with open(text_filename) as fin:
        text = fin.read()[:length]
    with open(substrings_filename) as fin_substrings:
        for i, substring in enumerate(fin_substrings.readlines()):
            substring = substring.strip()
            save_dir = os.path.dirname(substrings_filename)
            out_filename = os.path.join(save_dir, f'substring_{i}')
            if not os.path.isfile(out_filename):
                occurences, _ = bruteforce.bruteforce(substring, text)
                with open(out_filename, 'w') as fout:
                    json.dump({
                        "substring_length": len(substring),
                        "count_of_occurences": len(occurences),
                        "occurences": occurences,
                    }, fout)


def second_experiment(parsed_args):
    tests_count = parsed_args.c
    algorithm_name = parsed_args.a
    text_filename = parsed_args.t
    substrings_filename = parsed_args.substrings_filename
    length = parsed_args.length
    if check_arguments_second_experiment(
            tests_count,
            algorithm_name,
            text_filename,
            substrings_filename,
            length,
    ):
        preparation_for_second_experiment(
            substrings_filename,
            text_filename,
            length,
        )
        algorithm_tester = globals()[algorithm_name].performance_testing
        results = algorithm_tester(data_amorotized.
                                   generate(substrings_filename,
                                            text_filename),
                                   tests_count,
                                   )
        results = np.array(results)
        return results


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
                                     "./data/Texts/Normal/Substrings.txt"
                                     ])
    results = second_experiment(parsed_args=parsed_args)
    mask = np.isfinite(results).all(axis=1)
    used_indices = np.where(mask)[0]
    results = results[used_indices]
    assert results.shape == (12, 5)


if __name__ == "__main__":
    parser = create_parser()
    parsed_args = parser.parse_args(['1',
                                     '5',
                                     "bruteforce",
                                     "./data/Texts/Normal/INP_TEXT",
                                     '-m',
                                     '10',
                                     '-s',
                                     "рри"
                                     ])
    experiments_list = [first_experiment, second_experiment]
    if 1 <= parsed_args.n <= len(experiments_list):
        results = experiments_list[parsed_args.n - 1](parsed_args=parsed_args)
        mask = np.isfinite(results).all(axis=1)
        used_indices = np.where(mask)[0]
        results = results[used_indices]
        statiscian = Statiscian()
        # statiscian.make_plot(running_times=results,
        #                      x_label_="Length of input text, letters",
        #                      y_label_="Time of working, milliseconds",
        #                      out_filename="test")
        dir_name = os.path.dirname(parsed_args.substrings_filename)
        length_list = []
        occurences_list = []
        for substring_file in os.listdir(dir_name):
            if substring_file.startswith("substring_"):
                with open(os.path.join(dir_name, substring_file), 'r') as fin:
                    data = json.load(fin)
                    length_list.append(data["substring_length"])
                    occurences_list.append(data["count_of_occurences"])
        occurences_list = sorted(occurences_list,
                                 key=lambda x:
                                 length_list[occurences_list.index(x)])
        length_list.sort()
        statiscian.make_table(np.mean(results, axis=1),
                              occurences_list, length_list)
