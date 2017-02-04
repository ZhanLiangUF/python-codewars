from collections import defaultdict
def find_it(seq):
    dictionary = defaultdict(int)
    for item in seq:
        dictionary[item] += 1
    for key, value in dictionary.items():
        if value % 2 == 1:
            return key
