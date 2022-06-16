#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

  for line in sys.stdin:

    letter, date, num = line.strip().split()

    if len(num) == 1:
        num = "00" + num
    elif len(num) == 2:
        num = "0" + num

    print ("{},{},{}".format(letter, num, date))