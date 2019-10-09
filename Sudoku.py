import copy

import math


class Sudoku():

    def __init__(self, lista):
        self.tablero = lista
        self.tam = len(self.tablero)
        self.zona = int(math.sqrt(self.tam))

        # Guarda las coordenadas de los numeros que no se pueden borrar
        self.no_borrable = []
        for i in range(self.tam):
            for j in range(len(self.tablero[i])):
                if (self.tablero[i][j] != "x"):
                    self.no_borrable.append((i, j))

    # Valida si el tablero es un tablero que cumple las reglas
    def validar(self):
        self.contador = -1

        # Valido si algun elemento se repite en las filas y en las columnas
        for fil in self.tablero:
            self.contador += 1
            for i in range(self.tam):
                for j in range(self.tam):
                    if fil[i] == fil[j] and fil[i] != "x" and i != j:
                        return False
                    elif (self.tablero[i][j] == fil[j] and fil[j] != "x" and
                          i != self.contador):
                        return False

        # Valido si algun elemento se repite en las zonas
        for fila in range(0, self.tam, self.zona):
            for columna in range(0, self.tam, self.zona):
                for x in range(self.zona):
                    for y in range(self.zona):
                        for i in range(self.zona):
                            for j in range(self.zona):
                                if(self.tablero[x+fila][y+columna] != "x" and
                                   self.tablero[i+fila][j+columna] == self.tablero[x+fila][y+columna] and
                                   (x+fila, y+columna) != (i+fila, j+columna)):
                                    return False
        return True

    # Pone el numero en las coordenadas elegidas si es valido
    def poner_numero(self, numero, x, y):
        # Crea un duplicado de la tabla
        self.tabla_temp = copy.deepcopy(self.tablero)

        # agrega el numero ingresado en el tablero original
        self.tablero[x][y] = str(numero)

        # Checkea si se cumple la funcion validar para un tablero con el
        # numero que se ha agregado y se fija si las coordenadaas son las
        # de un numero fijo
        if (not self.validar() or (x, y) in self.no_borrable):

            # Si no se cumple, el tablero original se iguala al duplicado
            # que era correcto
            self.tablero = self.tabla_temp
            return "No puede ingresar ese numero ahi"

        return self.tablero

    # Se fija si hay "x" en el tablero
    def gano(self):
        for n in range(self.tam):
            if ("x" in self.tablero[n]):
                return False
        return True
