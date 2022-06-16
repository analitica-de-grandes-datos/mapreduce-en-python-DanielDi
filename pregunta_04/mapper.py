#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

  for line in sys.stdin:

    letter, _, _ = line.strip().split()

    print ("{}\t1".format(letter))