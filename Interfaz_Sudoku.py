import requests
from Sudoku import Sudoku


class Interfaz (Sudoku):

    def __init__(self):
        self.resp = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=9')
        self.lista = [["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"]]
        for item in self.resp.json()["squares"]:
            self.lista[item["x"]][item["y"]] = item["value"]
        Sudoku.__init__(self, self.lista)

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

# juego = Interfaz()
# juego.play()
