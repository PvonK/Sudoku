import math
import time
import sys

from Interfaz_Sudoku import Interfaz
"""
aa = int(input("aaa"))

if aa == 4:
    tablero = [["4", "2", "3", "1"],
                         ["1", "3", "2", "4"],
                         ["3", "1", "4", "2"],
                         ["2", "4", "1", "3"]]
else:
    tablero = [["8", "3", "6", "9", "7", "4", "2", "1", "5"],
                         ["7", "1", "5", "3", "6", "2", "8", "4", "9"],
                         ["4", "2", "9", "1", "5", "8", "6", "7", "3"],
                         ["6", "9", "1", "7", "4", "5", "3", "2", "8"],
                         ["3", "7", "2", "6", "8", "9", "1", "5", "4"],
                         ["5", "4", "8", "2", "3", "1", "7", "9", "6"],
                         ["1", "5", "4", "8", "2", "6", "9", "3", "7"],
                         ["9", "6", "7", "5", "1", "3", "4", "8", "2"],
                         ["2", "8", "3", "4", "9", "7", "5", "6", "1"]]


tam = len(tablero)
zona = int(math.sqrt(tam))
"""

"""
x = True
lista = ["*+ ", "+* "]
for i in range(100):
    for i in lista:
        sys.stdout.write("\r" + str(i) + "hola " + str(i))
        sys.stdout.flush()
        time.sleep(0.2)
print("\n")
"""
"""
start = time.perf_counter()

inpu = input()

if inpu == "a":
    tim = time.perf_counter() - start
    hours = str(int(tim/3600))
    minu = str(int(tim/60))
    secs = str(int(tim % 60))
    print(hours + ":" + minu + ":" + secs)
"""

x = Interfaz()

print(x)