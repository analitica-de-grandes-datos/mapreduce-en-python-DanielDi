#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    
    for line in sys.stdin:
        key, value = line.strip().split("\t")
        value = int(value)

        if curkey == key:
            sys.stdout.write(",{}".format(value))

        else:

            if curkey is not None:
                sys.stdout.write("\n")
                
            sys.stdout.write("{}\t{}".format(key, value))
            curkey = key
    sys.stdout.write("\n")