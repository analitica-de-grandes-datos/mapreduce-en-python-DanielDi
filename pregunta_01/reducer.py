#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
# import sys
# from functools import reduce

# def make_counts(acc, nxt):
#     acc[nxt] = acc.get(nxt, 0) + 1
#     return acc

# words = list(map(lambda row: row.replace('\n',''), sys.stdin))

# count_dict = reduce(
#     make_counts,
#     words,
#     {}
# )
# list(
#     map(
#         lambda row: sys.stdout.write("{}\t{}\n".format(row, count_dict[row])),
#         count_dict
# ))

import sys

if __name__ == '__main__':

    curkey = None
    total = 0

    for line in sys.stdin:

        key, value = line.split("\t")
        value = int(value)

        if key == curkey:
            total += value
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, total))

            curkey = key
            total = value

    sys.stdout.write("{}\t{}\n".format(curkey, total))