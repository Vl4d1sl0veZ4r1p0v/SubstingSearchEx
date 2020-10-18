def generate(substrings_filename, text_filename):
    with open(text_filename) as fin_text, \
            open(substrings_filename) as fin_substrings:
        text = fin_text.read()
        substrings = filter(lambda x: len(x),
                            fin_substrings.read().split("\n"))
    for substring in substrings:
        yield substring, text
