import unittest

from Sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    def test_Sudoku_1(self):

        sudoku = Sudoku(["53xx7xx3x",
                         "6xx195xxx",
                         "x98xxxx6x",
                         "8xxx6xxx3",
                         "4xx8x3xx1",
                         "7xxx2xxx6",
                         "x6xxxx28x",
                         "xxx419xx5",
                         "xxxx8xx79"])

        self.assertFalse(sudoku.validar())

    def test_Sudoku_2(self):
        sudoku = Sudoku(["53xx7xxxx",
                         "6xx195xxx",
                         "x98xxxx6x",
                         "8xxx6xxx3",
                         "4xx8x3xx1",
                         "7xxx2xxx6",
                         "x6xxxx28x",
                         "x3x419xx5",
                         "xxxx8xx79"])

        self.assertFalse(sudoku.validar())

    def test_Sudoku_3(self):

        sudoku = Sudoku(["53xx7xxxx",
                         "6x3195xxx",
                         "x98xxxx6x",
                         "8xxx6xxx3",
                         "4xx8x3xx1",
                         "7xxx2xxx6",
                         "x6xxxx28x",
                         "xxx419xx5",
                         "xxxx8xx79"])

        self.assertFalse(sudoku.validar())


    def test_Sudoku_4(self):

        sudoku = Sudoku(["53xx7xxxx",
                         "6xx195xxx",
                         "x98xxxx6x",
                         "8xxx6xxx3",
                         "4xx8x3xx1",
                         "7xxx2xxx6",
                         "x6xxxx28x",
                         "xxx419xx5",
                         "xxxx8xx79"])

        self.assertTrue(sudoku.validar())


    def test_Sudoku_5(self):

        sudoku = Sudoku(["53xx7xxxx",
                         "6xx195xxx",
                         "x98xxxx6x",
                         "8xxx6xxx3",
                         "4xx8x3xx1",
                         "7xxx2xxx6",
                         "x6xxxx28x",
                         "xxx419xx5",
                         "xxxx8xx79"])

        sudoku.poner_numero(1, 0, 2)

        sudoku.poner_numero(1, 1, 2)

        self.assertNotEqual(sudoku.tablero[0][0], sudoku.tablero[1][2])


    def test_Sudoku_6(self):

        sudoku = Sudoku(["53xx7xxxx",
                         "6xx195xxx",
                         "x98xxxx6x",
                         "8xxx6xxx3",
                         "4xx8x3xx1",
                         "7xxx2xxx6",
                         "x6xxxx28x",
                         "xxx419xx5",
                         "xxxx8xx79"])

        sudoku.poner_numero(2, 0, 2)

        self.assertEqual(sudoku.tablero[0][2], "2")


    def test_Sudoku_7(self):

        sudoku = Sudoku(["53xx7xxxx", "6xx195xxx", "x98xxxx6x", "8xxx6xxx3", "4xx8x3xx1", "xxx2xxx6", "x6xxxx28x", "xxx419xx5", "xxxx8xx79"])

        self.assertFalse(sudoku.gano())


    def test_Sudoku_8(self):
        sudoku = Sudoku(["836974215", "715362849", "429158673", "691745328", "372689154", "548231796", "154826937", "967513482", "283497561"])

        self.assertTrue(sudoku.gano())


if __name__ == '__main__':
    unittest.main()
