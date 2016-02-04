import unittest,sys
sys.path.append("/hometu/etudiants/m/e/E145465P/info2/prod_log/")
import Td1

class premierTest(unittest.TestCase):
        """
        Tests pour 1.py
        """

        def test0(self):
                """
                test avec 0
                """
                self.assertFalse(Td1.premier(0))

        def test1(self):
                """
                test avec 1
                """
                self.assertFalse(Td1.premier(1))

        def test2(self):
                """
                test avec un nombre premier
                """
                self.assertTrue(Td1.premier(5))

        def test3(self):
                """
                test avec un nombre non premier autre que 1
                """
                self.assertFalse(Td1.premier(9))
                
if __name__ == '__main__':
        unittest.main()