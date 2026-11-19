def one_hundred(chars):
    while (len(chars) < 100):
        chars += chars
    return chars[:100]