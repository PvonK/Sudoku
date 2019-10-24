import unittest

from Interfaz_Sudoku import Interfaz


class TestInterfazSudoku(unittest.TestCase):

    def test_Interfaz_1(self):
        user = Interfaz()
        user.tam = 4
        result = user.ingresar("a", 4, 6)
        self.assertFalse(result)

    def test_Interfaz_2(self):
        user = Interfaz()
        user.tam = 4
        result = user.ingresar(0, "g", 6)
        self.assertFalse(result)

    def test_Interfaz_3(self):
        user = Interfaz()
        user.tam = 4
        result = user.ingresar(0, 4, "d")
        self.assertFalse(result)

    def test_Interfaz_4(self):
        user = Interfaz()
        user.tam = 4
        result = user.ingresar("!", 4, 6)
        self.assertFalse(result)

    def test_Interfaz_5(self):
        user = Interfaz()
        user.tam = 4
        result = user.ingresar(0, "!", 6)
        self.assertFalse(result)

    def test_Interfaz_6(self):
        user = Interfaz()
        user.tam = 4
        result = user.ingresar(0, 4, "!")
        self.assertFalse(result)

    def test_Interfaz_7(self):
        user = Interfaz()
        user.tam = 4
        result = user.ingresar("!", 4, "$")
        self.assertFalse(result)

    def test_Interfaz_8(self):
        user = Interfaz()
        user.tam = 4
        result = user.ingresar("+", "g", 6)
        self.assertFalse(result)

    def test_Interfaz_9(self):
        user = Interfaz()
        user.tam = 4
        result = user.ingresar(".", "%", "d")
        self.assertFalse(result)

    def test_Interfaz_10(self):
        user = Interfaz()
        user.tam = 4
        result = user.ingresar("x", 1, 1)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
