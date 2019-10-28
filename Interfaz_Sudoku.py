from api import api

from Sudoku import Sudoku


class Interfaz ():

    def pedir_tam(self):
        self.tam = 0

        while self.tam != "9" and self.tam != "4":
            self.tam = input("Ingrese el tamaño del tablero (4/9)  ")

            if self.tam != "9" and self.tam != "4":
                print("Ingrese 4 o 9 \n\n")

    def pedir_lvl(self):
        self.level = 0

        while self.level != "1" and self.level != "2" and self.level != "3":
            self.level = input("Ingrese una dificultad (1, 2 o 3)  ")

            if self.level != "1" and self.level != "2" and self.level != "3":
                print("Ingrese 1, 2 o 3 \n\n")

    def inicio(self):
        self.pedir_tam()
        self.pedir_lvl()
        self.tam = int(self.tam)
        self.lista = api(self.tam, self.level)
        self.game = Sudoku(self.lista)

    def ingresar(self, numero, x, y):
        try:
            if int(x) > self.tam or int(x) < 1:
                return False
            elif int(y) > self.tam or int(y) < 1:
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

        if self.ingresar(self.n, self.i, self.j):
            return self.game.poner_numero(self.n, int(self.i)-1, int(self.j)-1)
        else:
            return "\nIngrese numeros validos"

    def play(self):

        self.inicio()
        print("")
        print(self.game.getTable())

        while not self.game.gano():
            print(self.pedirvalores())

        print("\nFIN")


if __name__ == "__main__":
    juego = Interfaz()
    juego.play()
