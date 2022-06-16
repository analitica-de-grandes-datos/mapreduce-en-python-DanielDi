#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    count = 0

    while count <= 5:

        count += 1

        num, letter, date = sys.stdin.readline().strip().split('\t')

        num = int(num)

        sys.stdout.write("{}   {}   {}\n".format(letter, date, num))