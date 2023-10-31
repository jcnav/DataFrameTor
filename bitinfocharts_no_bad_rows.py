import csv
import re

# Eliminamos las filas que no siguen el formato de tabla

if __name__ == "__main__":
    file_input = 'data\\bitinfocharts_1.csv'
    file_output = 'data\\tmp_out_clean_rows.csv'

    with open(file_input, 'r', newline='') as my_input, open(file_output, 'w', newline='') as my_output:
        read_csv = csv.reader(my_input)
        write_csv = csv.writer(my_output)

        for fila in read_csv:
            if not fila[0].startswith(';'):
                write_csv.writerow(fila)

    print(f"Se han eliminado las filas que comienzan con ';' en {file_input}. El resultado se ha guardado en {file_output}.")
