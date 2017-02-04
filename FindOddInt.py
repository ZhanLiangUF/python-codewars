from collections import defaultdict
#First brute force solution 
def find_it(seq):
    dictionary = defaultdict(int)
    for item in seq:
        dictionary[item] += 1
    for key, value in dictionary.items():
        if value % 2 == 1:
            return key

#Better solution
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
