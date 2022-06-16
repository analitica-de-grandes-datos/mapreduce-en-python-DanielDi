#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    llave_actual = None
    total = 0

    for line in sys.stdin:

        llave, valor = line.split("\t")
        valor = int(valor)

        if llave == llave_actual:
            total += valor
        else:
            if llave_actual is not None:
                sys.stdout.write("{},{}\n".format(llave_actual, total))

            llave_actual = llave
            total = valor

    sys.stdout.write("{},{}\n".format(llave_actual, total))