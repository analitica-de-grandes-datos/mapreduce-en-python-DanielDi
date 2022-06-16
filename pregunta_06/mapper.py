#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

  for line in sys.stdin:

    letter, _, number = line.strip().split()

    print ("{}\t{}".format(letter, number))