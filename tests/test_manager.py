import numpy as np

from manager import check_arguments_first_experiment
from manager import check_arguments_second_experiment
from manager import create_parser
from manager import first_experiment, second_experiment


def test_check_arguments_first_experiment():
    arguments_parser = create_parser()
    parsed_arguments = arguments_parser.parse_args(
        ['1',
         '5',
         "./data/Texts/Normal/INP_TEXT",
         '-m',
         '2',
         '-s',
         "tree"
         ])
    assert check_arguments_first_experiment(
        tests_count=parsed_arguments.c,
        algorithms_=parsed_arguments.a,
        substring=parsed_arguments.substring,
        text_filename=parsed_arguments.t,
        maxlength=parsed_arguments.maxlength,
    )


def test_check_arguments_second_experiment():
    arguments_parser = create_parser()
    parsed_arguments = arguments_parser.parse_args([
        '2',
        '5',
        "./data/Texts/Normal/INP_TEXT",
        '-l',
        '4200',
        '-S',
        "./data/Texts/Normal/Substrings.txt"
    ])
    assert check_arguments_second_experiment(
        tests_count=parsed_arguments.c,
        algorithms_=parsed_arguments.a,
        text_filename=parsed_arguments.t,
        substrings_filename=parsed_arguments.substrings_filename,
        length=parsed_arguments.length,
    )


def test_first_experiment_works():
    arguments_parser = create_parser()
    parsed_arguments = arguments_parser.parse_args([
        '1',
        '5',
        "./data/Texts/Normal/INP_TEXT",
        '-m',
        '2',
        '-s',
        "tree"
    ])
    results_times, _ = first_experiment(
        parsed_arguments=parsed_arguments,
        sparce_=1_000
    )
    results_times = np.array(results_times)
    assert results_times.shape == (1, 8, 5)


def test_second_experiment_works():
    arguments_parser = create_parser()
    parsed_arguments = arguments_parser.parse_args([
        '2',
        '5',
        "./data/Texts/Normal/INP_TEXT",
        '-l',
        '4200',
        '-S',
        "./data/Texts/Normal/Substrings.txt"
    ])
    results_times, _ = second_experiment(parsed_arguments=parsed_arguments)
    results_times = np.array(results_times)
    assert results_times.shape == (1, 9, 5)
