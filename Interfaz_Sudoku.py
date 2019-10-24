from api import api

from Sudoku import Sudoku


class Interfaz ():

    def pedir_tam(self):

        self.tam = 0

        while self.tam != "9" and self.tam != "4":
            self.tam = input("Ingrese el tamaño del tablero (4/9)  ")

            if self.tam != "9" and self.tam != "4":
                print("Ingrese 4 o 9 \n\n")

        self.tam = int(self.tam)

        self.lista = api(self.tam)
        self.game = Sudoku(self.lista)

    def ingresar(self, numero, x, y):
        try:
            if int(x) > self.tam:
                return False
            elif int(y) > self.tam:
                return False
            elif numero != "x":
                if int(numero) > 0 and int(numero) < self.tam+1:
                    return True
            else:
                return True
        except Exception:
            return False

    def pedirvalores(self):

        self.n = input("Ingrese un numero   ")
        self.i = input("ingrese la fila   ")
        self.j = input("Ingrese la columna   ")
        print("")

    def play(self):

        self.pedir_tam()
        print("")
        print(self.game.getTable())

        while not self.game.gano():
            self.pedirvalores()
            if self.ingresar(self.n, self.i, self.j):
                print(self.game.poner_numero(
                                             self.n,
                                             int(self.i)-1,
                                             int(self.j)-1
                                             )
                      )

            else:
                print("Ingrese numeros validos")

        print("\nFIN")


if __name__ == "__main__":
    juego = Interfaz()
    juego.play()
