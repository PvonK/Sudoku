import unittest

from Sudoku import Sudoku


class TestSudoku(unittest.TestCase):

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

    def test_Sudoku_9_tablero_correcto(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertTrue(sudoku.validar())

    def test_Sudoku_9_poner_numeros_en_la_misma_fila(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "x", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        sudoku.poner_numero(1, 0, 2)

        sudoku.poner_numero(1, 1, 2)

        self.assertNotEqual(
            sudoku.getTable(),
            "5 3 1 x 7 x x x x \n"
            "6 x 1 x 9 5 x x x \n"
            "x 9 8 x x x x 6 x \n"
            "8 x x x 6 x x x 3 \n"
            "4 x x 8 x 3 x x 1 \n"
            "7 x x x 2 x x x 6 \n"
            "x 6 x x x x 2 8 x \n"
            "x x x 4 1 9 x x 5 \n"
            "x x x x 8 x x 7 9 \n"
        )

    def test_Sudoku_9_poner_valor_correcto(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        sudoku.poner_numero(2, 0, 2)

        self.assertEqual(
            sudoku.getTable(),
            "5 3 2 x 7 x x x x \n"
            "6 x x 1 9 5 x x x \n"
            "x 9 8 x x x x 6 x \n"
            "8 x x x 6 x x x 3 \n"
            "4 x x 8 x 3 x x 1 \n"
            "7 x x x 2 x x x 6 \n"
            "x 6 x x x x 2 8 x \n"
            "x x x 4 1 9 x x 5 \n"
            "x x x x 8 x x 7 9 \n"
        )

    def test_Sudoku_9_todavia_no_gana(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["x", "x", "x", "2", "x", "x", "x", "6", "x"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.gano())

    def test_Sudoku_9_gano(self):
        sudoku = Sudoku([["8", "3", "6", "9", "7", "4", "2", "1", "5"],
                         ["7", "1", "5", "3", "6", "2", "8", "4", "9"],
                         ["4", "2", "9", "1", "5", "8", "6", "7", "3"],
                         ["6", "9", "1", "7", "4", "5", "3", "2", "8"],
                         ["3", "7", "2", "6", "8", "9", "1", "5", "4"],
                         ["5", "4", "8", "2", "3", "1", "7", "9", "6"],
                         ["1", "5", "4", "8", "2", "6", "9", "3", "7"],
                         ["9", "6", "7", "5", "1", "3", "4", "8", "2"],
                         ["2", "8", "3", "4", "9", "7", "5", "6", "1"]])

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

        sudoku = Sudoku([["4", "x", "3", "1"],
                         ["x", "3", "x", "x"],
                         ["3", "1", "x", "2"],
                         ["x", "4", "x", "x"]])

        self.assertTrue(sudoku.validar())

    def test_Sudoku_4_poner_numeros_en_la_misma_zona(self):

        sudoku = Sudoku([["4", "x", "3", "1"],
                         ["x", "3", "x", "x"],
                         ["3", "1", "x", "2"],
                         ["x", "4", "x", "x"]])

        sudoku.poner_numero(2, 0, 1)

        sudoku.poner_numero(2, 1, 0)

        self.assertNotEqual(
            sudoku.getTable(),
            "4 2 3 1 \n"
            "2 3 x x \n"
            "3 1 x 2 \n"
            "x 4 x x \n"
        )

    def test_Sudoku_4_poner_valor_correcto(self):

        sudoku = Sudoku([["4", "x", "3", "1"],
                         ["x", "3", "x", "x"],
                         ["3", "1", "x", "2"],
                         ["x", "4", "x", "x"]])

        sudoku.poner_numero(2, 0, 1)

        self.assertEqual(
            sudoku.getTable(),
            "4 2 3 1 \n"
            "x 3 x x \n"
            "3 1 x 2 \n"
            "x 4 x x \n"
        )

    def test_Sudoku_4_todavia_no_gana(self):

        sudoku = Sudoku([["4", "x", "3", "1"],
                         ["x", "3", "x", "x"],
                         ["3", "1", "x", "2"],
                         ["x", "4", "x", "x"]])

        self.assertFalse(sudoku.gano())

    def test_Sudoku_4_gano(self):
        sudoku = Sudoku([["4", "2", "3", "1"],
                         ["1", "3", "2", "4"],
                         ["3", "1", "4", "2"],
                         ["2", "4", "1", "3"]])

        self.assertTrue(sudoku.gano())


if __name__ == '__main__':
    unittest.main()
