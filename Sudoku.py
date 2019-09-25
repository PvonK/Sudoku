import copy


class Sudoku():

    def __init__(self, lista):
        self.tablero = []
        for n in range(len(lista)):
            self.tablero.append(list(lista[n]))

        self.no_borrable = []
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                if (self.tablero[i][j] != "x"):
                    self.no_borrable.append((i, j))

    def validar(self):
        self.contador = -1
        self.c = -3
        self.f = -3
        for fil in self.tablero:
            self.contador += 1
            for i in range(len(self.tablero)):
                for j in range(len(self.tablero[i])):
                    if fil[i] == fil[j] and fil[i] != "x" and i != j:
                        return False
                    elif (self.tablero[i][j] == fil[j] and fil[j] != "x" and
                          i != self.contador):
                        return False
        for fila in range(0, 9, 3):
            for columna in range(0, 9, 3):
                for x in range(3):
                    for y in range(3):
                        for i in range(3):
                            for j in range(3):
                                if(self.tablero[x+fila][y+columna] != "x" and
                                   self.tablero[i+fila][j+columna] == self.tablero[x+fila][y+columna] and
                                   (x+fila, y+columna) != (i+fila, j+columna)):
                                    return False
        return True

    def poner_numero(self, numero, x, y):
        self.tabla_temp = copy.deepcopy(self.tablero)
        self.tablero[x][y] = str(numero)

        if (not self.validar() or (x, y) in self.no_borrable):
            self.tablero = self.tabla_temp
            print(self.tabla_temp[x][y])

        for fila in self.tablero:
            print(" ")
            for elemento in fila:
                print(elemento, end=" ")

        return self.tablero

    def gano(self):
        for n in range(9):
            if ("x" in self.tablero[n]):
                return False
        return True
