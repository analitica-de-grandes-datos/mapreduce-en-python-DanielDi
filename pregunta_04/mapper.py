#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

  for line in sys.stdin:

    letter, date, num = line.strip().split()

    print ("{}\t{}\t{}".format(date, letter, num))