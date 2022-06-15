#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
# import sys

# list(
#     map(
#         #Imprimir cada credit_history
#         lambda row_credit: sys.stdout.write("{}\n".format(row_credit)),
#         # Obtener cada credit_history
#         map( lambda line: line.split(',')[2], sys.stdin)
#     )
# )



#! /usr/bin/ python
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        credit_type=line.split(",")[2]
        sys.stdout.write("{}\t1\n".format(credit_type))