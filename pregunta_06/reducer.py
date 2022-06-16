#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    min_num = 1000
    max_num = 0
    
    for line in sys.stdin:
        key, value = line.strip().split("\t")
        value = float(value)

        if curkey == key:

            if value > max_num:
                max_num = value

            elif value < min_num:
                min_num = value

        else:

            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, max_num, min_num))

            curkey = key
            min_num = float(value)
            max_num = float(value)   

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, max_num, min_num))