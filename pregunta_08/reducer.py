#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    sum_num = 0
    count = 0
    mean = 0
    
    for line in sys.stdin:
        key, value = line.strip().split("\t")
        value = float(value)

        if curkey == key:
            sum_num += value
            count+=1

        else:

            if curkey is not None:
                mean = sum_num / count 
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, sum_num, mean))

            curkey = key
            sum_num = float(value)
            count = 1 
            
    mean = sum_num / count 
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, sum_num, mean))