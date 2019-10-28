import unittest

from parameterized import parameterized

from Sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.sudoku9 = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                               ["6", "x", "x", "x", "9", "5", "x", "x", "x"],
                               ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                               ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                               ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                               ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                               ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                               ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                               ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.sudoku4 = Sudoku([["4", "x", "3", "1"],
                               ["x", "3", "x", "x"],
                               ["3", "1", "x", "2"],
                               ["x", "4", "x", "x"]])

    def test_Sudoku_9_tablero_correcto(self):

        self.assertTrue(self.sudoku9.validar())

    @parameterized.expand([
        (7, 0, 2),
        (5, 1, 7),
        (6, 2, 3),
        (8, 3, 6),
        (4, 4, 4),
        (7, 5, 6),
        (6, 6, 3),
        (9, 7, 0),
        (8, 8, 1),
    ])
    def test_Sudoku_9_poner_numeros_misma_fila(self, numero, fila, columna):

        result = self.sudoku9.poner_numero(numero, fila, columna)

        self.assertEqual(
            result,
            "No puede ingresar ese numero ahi"
        )

    @parameterized.expand([
        (5, 8, 0),
        (3, 8, 1),
        (8, 7, 2),
        (4, 0, 3),
        (7, 6, 4),
        (9, 0, 5),
        (2, 0, 6),
        (6, 7, 7),
        (9, 0, 8),
    ])
    def test_Sudoku_9_poner_numeros_misma_columna(self, numero, fila, columna):

        result = self.sudoku9.poner_numero(numero, fila, columna)

        self.assertEqual(
            result,
            "No puede ingresar ese numero ahi"
        )

    @parameterized.expand([
        (3, 2, 0),
        (9, 0, 3),
        (6, 0, 8),
        (7, 3, 2),
        (2, 3, 5),
        (6, 3, 6),
        (6, 8, 0),
        (9, 8, 3),
        (8, 8, 6),
    ])
    def test_Sudoku_9_poner_numeros_misma_zona(self, numero, fila, columna):

        result = self.sudoku9.poner_numero(numero, fila, columna)

        self.assertEqual(
            result,
            "No puede ingresar ese numero ahi"
        )

    @parameterized.expand([
        (4, 0, 2),
        (6, 0, 3),
        (8, 0, 5),
        (9, 0, 6),
        (1, 0, 7),
        (2, 0, 8),
        (7, 1, 1),
        (2, 1, 2),
        (1, 1, 3),
        (3, 1, 6),
        (4, 1, 7),
        (8, 1, 8),
        (1, 2, 0),
        (3, 2, 3),
        (4, 2, 4),
        (2, 2, 5),
        (5, 2, 6),
        (7, 2, 8),
        (5, 3, 1),
        (9, 3, 2),
        (7, 3, 3),
        (1, 3, 5),
        (4, 3, 6),
        (2, 3, 7),
        (2, 4, 1),
        (6, 4, 2),
        (5, 4, 4),
        (7, 4, 6),
        (9, 4, 7),
        (1, 5, 1),
        (3, 5, 2),
        (9, 5, 3),
        (4, 5, 5),
        (8, 5, 6),
        (5, 5, 7),
        (9, 6, 0),
        (1, 6, 2),
        (5, 6, 3),
        (3, 6, 4),
        (7, 6, 5),
        (4, 6, 8),
        (2, 7, 0),
        (8, 7, 1),
        (7, 7, 2),
        (6, 7, 6),
        (3, 7, 7),
        (3, 8, 0),
        (4, 8, 1),
        (5, 8, 2),
        (2, 8, 3),
        (6, 8, 5),
        ("x", 8, 2),
        ("x", 8, 3),
        ("x", 8, 5),
        ("x", 8, 6),
        (1, 8, 6),
    ])
    def test_Sudoku_9_poner_valor_correcto(self, numero, fila, columna):

        result = self.sudoku9.poner_numero(numero, fila, columna)

        self.assertNotEqual(
            result,
            "No puede ingresar ese numero ahi"
        )

    def test_Sudoku_9_misma_fila(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "3", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.validar())

    def test_Sudoku_9_misma_columna(self):
        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.validar())

    def test_Sudoku_9_misma_zona(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "3", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.validar())

    def test_Sudoku_9_todavia_no_gana(self):

        self.assertFalse(self.sudoku9.gano())

    def test_Sudoku_9_gano(self):
        sudoku = Sudoku([["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                         ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                         ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                         ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                         ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                         ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                         ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                         ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                         ["3", "4", "5", "2", "8", "6", "1", "7", "9"]])

        self.assertTrue(sudoku.gano())

    def test_Sudoku_4_misma_fila(self):

        sudoku = Sudoku([["4", "x", "3", "4"],
                         ["x", "3", "x", "x"],
                         ["3", "1", "x", "2"],
                         ["x", "4", "x", "x"]])

        self.assertFalse(sudoku.validar())

    def test_Sudoku_4_misma_columna(self):
        sudoku = Sudoku([["4", "x", "3", "1"],
                         ["x", "3", "x", "x"],
                         ["3", "1", "x", "2"],
                         ["x", "4", "3", "x"]])

        self.assertFalse(sudoku.validar())

    def test_Sudoku_4_misma_zona(self):

        sudoku = Sudoku([["4", "x", "3", "1"],
                         ["x", "x", "x", "x"],
                         ["3", "1", "x", "2"],
                         ["x", "3", "x", "x"]])

        self.assertFalse(sudoku.validar())

    def test_Sudoku_4_tablero_correcto(self):

        self.assertTrue(self.sudoku4.validar())

    @parameterized.expand([
        (4, 0, 1),
        (3, 0, 1),
        (4, 1, 0),
        (3, 1, 0),
        (1, 3, 0),
        (1, 1, 2),
        (2, 3, 2),
    ])
    def test_Sudoku_4_poner_numeros_misma_zona(self, numero, fila, columna):

        result = self.sudoku4.poner_numero(numero, fila, columna)

        self.assertEqual(result, "No puede ingresar ese numero ahi")

    @parameterized.expand([
        (3, 0, 1),
        (3, 1, 3),
        (1, 2, 2),
        (4, 3, 3),
    ])
    def test_Sudoku_4_poner_numeros_misma_fila(self, numero, fila, columna):

        result = self.sudoku4.poner_numero(numero, fila, columna)

        self.assertEqual(result, "No puede ingresar ese numero ahi")

    @parameterized.expand([
        (4, 3, 0),
        (3, 1, 0),
        (4, 0, 1),
        (1, 0, 1),
        (3, 3, 2),
        (1, 3, 3),
        (2, 1, 3),
    ])
    def test_Sudoku_4_poner_numeros_misma_columna(self, numero, fila, columna):

        result = self.sudoku4.poner_numero(numero, fila, columna)

        self.assertEqual(result, "No puede ingresar ese numero ahi")

    @parameterized.expand([
        (2, 0, 1),
        (4, 2, 2),
        (1, 1, 0),
        (2, 3, 0),
        (2, 1, 2),
        (4, 1, 3),
        (1, 3, 2),
        ("x", 1, 2),
        ("x", 1, 3),
        ("x", 3, 2),
        (3, 3, 3),
    ])
    def test_Sudoku_4_poner_valor_correcto(self, numero, fila, columna):

        result = self.sudoku4.poner_numero(numero, fila, columna)

        self.assertNotEqual(result, "No puede ingresar ese numero ahi")

    def test_Sudoku_4_todavia_no_gana(self):

        self.assertFalse(self.sudoku4.gano())

    def test_Sudoku_4_gano(self):
        sudoku = Sudoku([["4", "2", "3", "1"],
                         ["1", "3", "2", "4"],
                         ["3", "1", "4", "2"],
                         ["2", "4", "1", "3"]])

        self.assertTrue(sudoku.gano())


if __name__ == '__main__':
    unittest.main()
