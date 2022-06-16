#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    for line in sys.stdin:

        letter, num, date = line.strip().split(',')

        num = int(num)

        sys.stdout.write("{}   {}   {}\n".format(letter, date, num))