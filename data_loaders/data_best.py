def generate(max_lenght: int, substring: str, text_filename: str, sparce: int):
    with open(text_filename, 'r') as fin:
        text = fin.read()
        max_amount = int(max_lenght * len(text) / 100 / sparce)
        for i in range(1, max_amount + 1):
            amount = i * sparce
            text_for_search = text[:amount]
            yield [substring, text_for_search]
