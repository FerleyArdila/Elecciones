import sys
import pandas as pd


def print_hi(name):
    archivo_establecido = False
    file = None

    while True:
        print("Seleccione la opcion "
              "\n1:Establecer ruta de archivo "
              "\n2:Agrupar por candidato "
              "\n3:agrupar por partido "
              "\n4:Agrupar por puesto "
              "\n5:Agrupar por municipio "
              "\n6:Agrupar por departamento"
              "\n7:Exportar en xlsx"
              "\n8:Exportar en csv"
              "\n9:Salir"
              )

        try:
            user_input = int(input())
            print("Ha seleccionado " + str(user_input))

            if user_input == 1:
                print('Por favor ingrese la ruta del archivo csv')
                path_file = str(input())
                file = pd.read_csv(path_file)
                archivo_establecido = True

            if user_input == 2:
                if archivo_establecido:
                    file.groupby('candidato')

            if user_input == 3:
                if archivo_establecido:
                    file.groupby('partido')

            if user_input == 4:
                if archivo_establecido:
                    file.groupby('puesto')

            if user_input == 5:
                if archivo_establecido:
                    file.groupby('municipio')

            if user_input == 6:
                if archivo_establecido:
                    file.groupby('departamento')

            if user_input == 7:
                if archivo_establecido:
                    file.groupby('candidato')

            if user_input == 8:
                if archivo_establecido:
                    file.groupby('candidato')

            if user_input == 9:
                sys.exit()

        except ValueError:
            print("Not an integer! Try again.")


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
