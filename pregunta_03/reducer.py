#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator
if __name__ == '__main__':
    dict_from_list = {}

    for line in sys.stdin:

        num, letter = line.strip().split("\t")
        sys.stdout.write("{},{}\n".format(letter, num))