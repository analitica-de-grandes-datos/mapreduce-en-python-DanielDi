#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

  for line in sys.stdin:

    _, date, _ = line.strip().split()
    month = date.split('-')[1]

    print ("{}\t1".format(month))