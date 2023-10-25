import csv
import re

###
# La tercera columna es del tipo xxx,yyy BTC xcvbbxbx
# Y la transformamos en xxx.yyy
# Ej: 248,597 BTC ($6,432,033,211) -> 248.597
###

if __name__ == "__main__":
    file_input = 'data\\tmp_out_clean_rows.csv'
    file_output = 'data\\salida.csv'

    with open(file_input, 'r', newline='') as my_input, open(file_output, 'w', newline='') as my_output:
        read_csv = csv.reader(my_input, delimiter=';')
        write_csv = csv.writer(my_output, delimiter=',')

        for fila in read_csv:
            if not fila[0].startswith(';'):
                print(fila[2])
                match = re.search(r'(\S+) BTC', fila[2])
                if match:
                    numero = match.group(1)
                    fila[2] = numero.replace(",", ".")
                    print(fila[2])
                write_csv.writerow(fila)
    print(f"Se ha modificado la tercera columna de {file_input} y se ha guardado en {file_output}.")
