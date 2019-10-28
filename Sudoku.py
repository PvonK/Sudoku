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

    def validarFilas(self, tabla):
        # Valido si algun elemento se repite en las filas
        for fil in tabla:
            for n in range(self.tam):
                self.elem = fil.pop(n)
                if self.elem in fil and self.elem != "x":
                    return False
                fil.insert(n, self.elem)
        return True

    # Valida si el tablero es un tablero que cumple las reglas
    def validar(self):

        # Valido si algun elemento se repite en las filas
        if not self.validarFilas(self.tablero):
            return False

        # Creo una tabla transpuesta
        # y valido si algun elemento se repite en las columnas
        # usando validar filas
        self.tablaT = []
        for i in range(self.tam):
            self.column = []
            for j in range(self.tam):
                self.column.append(self.tablero[j][i])
            self.tablaT.append(self.column)

        if not self.validarFilas(self.tablaT):
            return False

        # hago una lista con los elementos de las zonas como filas
        # y valido si algun elemento se repite en las zonas
        # usando validar filas
        self.listaDeZonas = []
        for i in range(0, self.tam, self.zona):
            for j in range(0, self.tam, self.zona):
                self.listaZ = []
                for x in range(self.zona):
                    self.listaZ.extend(self.tablero[i+x][j:j+self.zona])
                self.listaDeZonas.append(self.listaZ)

        if not self.validarFilas(self.listaDeZonas):
            return False

        return True

    def getTable(self):
        self.tableroImpreso = ""
        for i in range(self.tam):
            if i == self.zona or i == self.zona*2:
                for n in range(self.tam):
                    self.tableroImpreso += "--"
                    if n == self.zona-1 or n == self.zona*2-1:
                        self.tableroImpreso += "+-"
                if n == self.zona-1 or n == self.zona*2-1:
                    self.tableroImpreso = self.tableroImpreso[:-3]
                self.tableroImpreso += "\n"
            for j in range(self.tam):
                if j == self.zona or j == self.zona*2:
                    self.tableroImpreso += "| "
                self.tableroImpreso += self.tablero[i][j] + " "
            self.tableroImpreso += "\n"

        return self.tableroImpreso

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

        return self.getTable()

    # Se fija si hay "x" en el tablero
    def gano(self):
        for n in range(self.tam):
            if ("x" in self.tablero[n]):
                return False
        return True
