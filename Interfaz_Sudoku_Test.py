import unittest
import io
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from Sudoku import Sudoku
from Interfaz_Sudoku import Interfaz


class TestInterfazSudoku(unittest.TestCase):

    def setUp(self):
        self.user4 = Interfaz()
        self.user4.tam = 4
        self.user4.lvl = 1
        self.user4.game = Sudoku([["4", "x", "3", "1"],
                                  ["x", "3", "x", "x"],
                                  ["3", "1", "x", "2"],
                                  ["x", "4", "x", "x"]])

        self.user9 = Interfaz()
        self.user9.tam = 9
        self.user9.lvl = 1
        self.user9.game = Sudoku([
                    ["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                    ["6", "x", "x", "x", "9", "5", "x", "x", "x"],
                    ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                    ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                    ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                    ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                    ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                    ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                    ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

    @parameterized.expand([
        ("a", "4", "6"),
        ("2", "g", "6"),
        ("2", "4", "d"),
        ("!", "4", "6"),
        ("2", "!", "6"),
        ("2", "4", "!"),
        ("!", "4", "$"),
        ("+", "g", "6"),
        ("3", "as", "/"),
        (".", "%", "d")
    ])
    def test_ingresar_letras_y_simbolos(self, numero, fila, columna):
        result = self.user4.ingresar(numero, fila, columna)
        self.assertFalse(result)

    def test_ingresar_letra_x_en_numero_correcto(self):
        result = self.user4.ingresar("x", 1, 1)
        self.assertTrue(result)

    def test_pedir_tam_4(self):
        with patch("builtins.input", return_value="4"):
            self.user4.pedir_tam()
        self.assertEqual(self.user4.tam, "4")

    @parameterized.expand([
        ("2"),
        ("a"),
        ("!"),
        ("&"),
        ("49"),
        ("94")
    ])
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_pedir_tam_mal(self, tamMal, mock_stdout):
        mock = MagicMock()
        mock.side_effect = [tamMal, "4"]
        with patch("builtins.input", new=mock):
            self.user4.pedir_tam()
        self.assertEqual(mock_stdout.getvalue(), "Ingrese 4 o 9 \n\n\n")

    def test_pedir_lvl_1(self):
        with patch("builtins.input", return_value="1"):
            self.user4.pedir_lvl()
        self.assertEqual(self.user4.level, "1")

    def test_pedir_lvl_2(self):
        with patch("builtins.input", return_value="2"):
            self.user4.pedir_lvl()
        self.assertEqual(self.user4.level, "2")

    def test_pedir_lvl_3(self):
        with patch("builtins.input", return_value="3"):
            self.user4.pedir_lvl()
        self.assertEqual(self.user4.level, "3")

    @parameterized.expand([
        ("33"),
        ("a"),
        ("!"),
        ("&"),
        ("11"),
        ("22"),
        ("12"),
        ("23"),
        ("21"),
        ("123")
    ])
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_pedir_lvl_mal(self, lvlMal, mock_stdout):
        mock = MagicMock()
        mock.side_effect = [lvlMal, "1"]
        with patch("builtins.input", new=mock):
            self.user4.pedir_lvl()
        self.assertEqual(mock_stdout.getvalue(), "Ingrese 1, 2 o 3 \n\n\n")

    @parameterized.expand([
        ("2", "0", "1"),
        ("2", "-1", "1"),
        ("2", "5", "1"),
        ("2", "8", "1"),
        ("2", "19", "1"),
    ])
    def test_pedir_valores_fila_mal4(self, numero, fila, columna):
        mock = MagicMock()
        mock.side_effect = [numero, fila, columna]
        with patch("builtins.input", new=mock):
            result = self.user4.pedirvalores()
        self.assertEqual(result, "\nIngrese numeros validos")

    @parameterized.expand([
        ("2", "1", "0"),
        ("2", "1", "-1"),
        ("2", "1", "5"),
        ("2", "1", "8"),
        ("2", "1", "19"),
    ])
    def test_pedir_valores_columna_mal4(self, numero, fila, columna):
        mock = MagicMock()
        mock.side_effect = [numero, fila, columna]
        with patch("builtins.input", new=mock):
            result = self.user4.pedirvalores()
        self.assertEqual(result, "\nIngrese numeros validos")

    @parameterized.expand([
        ("0", "2", "1"),
        ("-1", "2", "1"),
        ("5", "2", "1"),
        ("8", "2", "1"),
        ("19", "2", "1"),
    ])
    def test_pedir_valores_numero_mal4(self, numero, fila, columna):
        mock = MagicMock()
        mock.side_effect = [numero, fila, columna]
        with patch("builtins.input", new=mock):
            result = self.user4.pedirvalores()
        self.assertEqual(result, "\nIngrese numeros validos")

    @parameterized.expand([
        ("2", "1", "2"),
        ("4", "3", "3"),
        ("1", "2", "1"),
        ("2", "4", "1"),
        ("2", "2", "3"),
        ("4", "2", "4"),
        ("1", "4", "3"),
        ("3", "4", "4"),
    ])
    def test_pedir_valores_fila_bien4(self, numero, fila, columna):
        mock = MagicMock()
        mock.side_effect = [numero, fila, columna]
        with patch("builtins.input", new=mock):
            result = self.user4.pedirvalores()
        self.assertNotEqual(result, "\nIngrese numeros validos")

    def test_pedir_tam_9(self):
        with patch("builtins.input", return_value="9"):
            self.user9.pedir_tam()
        self.assertEqual(self.user9.tam, "9")

    @parameterized.expand([
        ("4", "1", "3"),
        ("6", "1", "4"),
        ("8", "1", "6"),
        ("9", "1", "7"),
        ("1", "1", "8"),
        ("2", "1", "9"),
        ("7", "2", "2"),
        ("2", "2", "3"),
        ("1", "2", "4"),
        ("3", "2", "7"),
        ("4", "2", "8"),
        ("8", "2", "9"),
        ("1", "3", "1"),
        ("3", "3", "4"),
        ("4", "3", "5"),
        ("2", "3", "6"),
        ("5", "3", "7"),
        ("7", "3", "9"),
        ("5", "4", "2"),
        ("9", "4", "3"),
        ("7", "4", "4"),
        ("1", "4", "6"),
        ("4", "4", "7"),
        ("2", "4", "8"),
        ("2", "5", "2"),
        ("6", "5", "3"),
        ("5", "5", "5"),
        ("7", "5", "7"),
        ("9", "5", "8"),
        ("1", "6", "2"),
        ("3", "6", "3"),
        ("9", "6", "4"),
        ("4", "6", "6"),
        ("8", "6", "7"),
        ("5", "6", "8"),
        ("9", "7", "1"),
        ("1", "7", "3"),
        ("5", "7", "4"),
        ("3", "7", "5"),
        ("7", "7", "6"),
        ("4", "7", "9"),
        ("2", "8", "1"),
        ("8", "8", "2"),
        ("7", "8", "3"),
        ("6", "8", "7"),
        ("3", "8", "8"),
        ("3", "9", "1"),
        ("4", "9", "2"),
        ("5", "9", "3"),
        ("2", "9", "4"),
        ("6", "9", "6"),
        ("1", "9", "7"),
    ])
    def test_pedir_valores_fila_bien9(self, numero, fila, columna):
        mock = MagicMock()
        mock.side_effect = [numero, fila, columna]
        with patch("builtins.input", new=mock):
            result = self.user9.pedirvalores()
        self.assertNotEqual(result, "\nIngrese numeros validos")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_play_ganador4(self, mock_stdout):

        mock = MagicMock()
        mock.side_effect = ["2", "1", "2",
                            "4", "3", "3",
                            "1", "2", "1",
                            "2", "4", "1",
                            "2", "2", "3",
                            "4", "2", "4",
                            "1", "4", "3",
                            "3", "4", "4"]
        with patch("Interfaz_Sudoku.Interfaz.inicio",
                   return_value=None), patch("builtins.input", new=mock):
            self.user4.play()
        self.assertEqual(mock_stdout.getvalue()[-6:], "\n\nFIN\n")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_play_ganador9(self, mock_stdout):

        mock = MagicMock()
        mock.side_effect = ["4", "1", "3",
                            "6", "1", "4",
                            "8", "1", "6",
                            "9", "1", "7",
                            "1", "1", "8",
                            "2", "1", "9",
                            "7", "2", "2",
                            "2", "2", "3",
                            "1", "2", "4",
                            "3", "2", "7",
                            "4", "2", "8",
                            "8", "2", "9",
                            "1", "3", "1",
                            "3", "3", "4",
                            "4", "3", "5",
                            "2", "3", "6",
                            "5", "3", "7",
                            "7", "3", "9",
                            "5", "4", "2",
                            "9", "4", "3",
                            "7", "4", "4",
                            "1", "4", "6",
                            "4", "4", "7",
                            "2", "4", "8",
                            "2", "5", "2",
                            "6", "5", "3",
                            "5", "5", "5",
                            "7", "5", "7",
                            "9", "5", "8",
                            "1", "6", "2",
                            "3", "6", "3",
                            "9", "6", "4",
                            "4", "6", "6",
                            "8", "6", "7",
                            "5", "6", "8",
                            "9", "7", "1",
                            "1", "7", "3",
                            "5", "7", "4",
                            "3", "7", "5",
                            "7", "7", "6",
                            "4", "7", "9",
                            "2", "8", "1",
                            "8", "8", "2",
                            "7", "8", "3",
                            "6", "8", "7",
                            "3", "8", "8",
                            "3", "9", "1",
                            "4", "9", "2",
                            "5", "9", "3",
                            "2", "9", "4",
                            "6", "9", "6",
                            "1", "9", "7"]
        with patch("Interfaz_Sudoku.Interfaz.inicio",
                   return_value=None), patch("builtins.input", new=mock):
            self.user9.play()
        self.assertEqual(mock_stdout.getvalue()[-6:], "\n\nFIN\n")


if __name__ == '__main__':
    unittest.main()
