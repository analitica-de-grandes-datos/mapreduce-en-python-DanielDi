#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    max_amount = 0

    for line in sys.stdin:
        row = line.split("\t")
        key = row[0]
        value = int(row[1])

        if curkey == key:
            if value > max_amount:
                max_amount = value
            else:
                value = max_amount

        else:

            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, max_amount))

            curkey = key
            max_amount = value

    sys.stdout.write("{}\t{}\n".format(curkey, max_amount))
