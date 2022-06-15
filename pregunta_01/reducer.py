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

    llave_actual = None
    total = 0

    for line in sys.stdin:

        llave, valor = line.split("\t")
        valor = int(valor)

        if llave == llave_actual:
            total += valor
        else:
            if llave_actual is not None:
                sys.stdout.write("{}\t{}\n".format(llave_actual, total))

            llave_actual = llave
            total = valor

    sys.stdout.write("{}\t{}\n".format(llave_actual, total))