from itertools import accumulate


def parts_sums(ls):
    return [0, *accumulate(ls[::-1])][::-1]


print(parts_sums([0, 1, 3, 6, 10]))
