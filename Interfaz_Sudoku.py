from Sudoku import Sudoku


class Interfaz (Sudoku):

    def __init__(self, lista):
        Sudoku.__init__(self, lista)

    def ingresar(self, numero, x, y):
        try:
            if int(x) > 8:
                return False
            elif int(y) > 8:
                return False
            elif numero != "x":
                if int(numero) > 0 and int(numero) < 10:
                    return True
            else:
                return True
        except:
            return False

    def play(self):

        for fila in self.tablero:
            print(" ")
            for elemento in fila:
                print(elemento, end=" ")

        while not Sudoku.gano(self):
            print("")
            self.n = input("Ingrese un numero   ")
            self.i = input("ingrese la fila   ")
            self.j = input("Ingrese la columna   ")
            if self.ingresar(self.n, self.i, self.j):
                self.tabla = Sudoku.poner_numero(self, self.n, int(self.i), int(self.j))

                if len(self.tabla) == 9:
                    for fila in self.tabla:
                        print(" ")
                        for elemento in fila:
                            print(elemento, end=" ")

                else:
                    print("\n", self.tabla)

            else:
                print("Ingrese numeros validos")

        print("FIN")

# juego = Interfaz(["53xx7xxxx",
#                   "6xx195xxx",
#                   "x98xxxx6x",
#                   "8xxx6xxx3",
#                   "4xx8x3xx1",
#                   "7xxx2xxx6",
#                   "x6xxxx28x",
#                   "xxx419xx5",
#                   "xxxx8xx79"])
# juego.play()
