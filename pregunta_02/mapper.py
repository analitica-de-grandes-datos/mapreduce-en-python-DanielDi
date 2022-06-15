#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

#! /usr/bin/ python
import sys

if __name__ == "__main__":
    
    for line in sys.stdin:
        credit_type=line.split(",")
        sys.stdout.write("{}\t{}\n".format(credit_type[3], credit_type[4]))



# import sys

# list(
#     map(
#         #Imprimir cada credit_history
#         lambda row_credit: sys.stdout.write("{}-{}\n".format(row_credit[0], row_credit[1])),
#         # Obtener cada credit_history
#         map( lambda line: (line.split(',')[3], line.split(',')[4]), sys.stdin)
#     )
# )