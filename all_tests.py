import unittest
from Sudoku_Test import TestSudoku
from Interfaz_Sudoku_Test import TestInterfazSudoku
from API_Test import TestAPISudoku


def suite():
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.makeSuite(TestSudoku))

    test_suite.addTest(unittest.makeSuite(TestAPISudoku))

    test_suite.addTest(unittest.makeSuite(TestInterfazSudoku))
    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)
