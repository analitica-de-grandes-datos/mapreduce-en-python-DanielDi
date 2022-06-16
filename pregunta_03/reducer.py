#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    for line in sys.stdin:

        num, letter = line.strip().split("\t")
        sys.stdout.write("{},{}\n".format(letter, num))