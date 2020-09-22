import os
import pytest
from random import choice
from string import ascii_lowercase


def generate(substrings_filename, text_filename):
    with open(text_filename) as fin_text, open(substrings_filename) as fin_substrings:
        text = fin_text.read()
        substrings = filter(lambda x: len(x), fin_substrings.read().split("\n"))
    for substring in substrings:
        yield [substring, text]


def test_generate_checks_if_completes_correctly_into_batches():
    import tempfile as tf

    def generate_string(string_size):
        return ''.join([choice(ascii_lowercase) for _ in range(string_size)])

    text_size = 10
    substring = "test"
    text = generate_string(text_size)
    substrings = [generate_string(i) for i in range(3, 20, 9)]

    with tf.TemporaryDirectory() as tmp_dir_name:
        tmp_text_file_name = os.path.join(tmp_dir_name, "text_file.txt")
        tmp_substrings_file_name = os.path.join(tmp_dir_name, "substrings_file.txt")
        with open(tmp_text_file_name, 'w') as fout:
            fout.write(text)
        with open(tmp_substrings_file_name, 'w') as fout:
            for substring in substrings:
                print(substring, file=fout)

        batches = list(generate(
            substrings_filename=tmp_substrings_file_name,
            text_filename=tmp_text_file_name,
        ))
    assert batches == [[substring, text] for substring in substrings]


