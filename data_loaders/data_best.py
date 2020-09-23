import os
import pytest
from random import choice
from string import ascii_lowercase


def generate(maxlenght: int, substring: str, text_filename: str):
    with open(text_filename, 'r') as fin:
        text = fin.read()
        max_amount = int(100 * maxlenght / len(text))
        for i in range(1, max_amount, 2):
            amount = i * 10_000
            text_for_search = text[:amount]
            yield [substring, text_for_search]


def test_generate_checks_if_divides_correctly_into_batches():
    import tempfile as tf
    text_size = 1_000
    substring = "test"
    length = 42
    text = ''.join([choice(ascii_lowercase) for _ in range(text_size)])
    with tf.TemporaryDirectory() as tmp_dir_name:
        tmp_file_name = os.path.join(tmp_dir_name, "test_file.txt")
        with open(tmp_file_name, 'w') as fout:
            fout.write(text)
        batches = list(generate(
            maxlenght=length,
            substring=substring,
            text_filename=tmp_file_name,
        ))
    assert batches == [[substring, text[:10_000 * i]] for i in range(1, int(100 * length / text_size), 2)]
