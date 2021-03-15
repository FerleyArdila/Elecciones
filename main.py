# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    while True:
        print("Seleccione la opcion "
              "\n1:Establecer ruta de archivo "
              "\n2:Agrupar por candidato "
              "\n3:agrupar por partido "
              "\n4:Agrupar por puesto "
              "\n5:Agrupar por municipio "
              "\n6:Agrupar por departamento")

        try:
            user_input = int(input())
            print("Ha seleccionado " + str(user_input))

            if user_input==1:
                print('Por favor ingrese la ruta del archivo csv')
                path_file = str(input())

        except ValueError:
            print("Not an integer! Try again.")


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
