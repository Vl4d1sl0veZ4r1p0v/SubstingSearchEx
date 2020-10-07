import os
from random import choice
from string import ascii_lowercase

from data_loaders import data_amorotized
from data_loaders import data_best


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
        tmp_substrings_file_name = os.path.join(tmp_dir_name,
                                                "substrings_file.txt")
        with open(tmp_text_file_name, 'w') as fout:
            fout.write(text)
        with open(tmp_substrings_file_name, 'w') as fout:
            for substring in substrings:
                print(substring, file=fout)

        batches = list(data_amorotized.generate(
            substrings_filename=tmp_substrings_file_name,
            text_filename=tmp_text_file_name,
        ))
    assert batches == [[substring, text] for substring in substrings]

def test_generate_checks_if_divides_correctly_into_batches():
    import tempfile as tf
    text_size = 10_000
    substring = "test"
    length = 42
    text = ''.join([choice(ascii_lowercase) for _ in range(text_size)])
    with tf.TemporaryDirectory() as tmp_dir_name:
        tmp_file_name = os.path.join(tmp_dir_name, "test_file.txt")
        with open(tmp_file_name, 'w') as fout:
            fout.write(text)
        batches = list(data_best.generate(
            max_lenght=length,
            substring=substring,
            text_filename=tmp_file_name,
            sparce=1_000
        ))
    assert batches == [
        [substring, text[:1_000 * i]]
        for i in range(1, int(text_size * length / 100 / 1_000) + 1)
    ]