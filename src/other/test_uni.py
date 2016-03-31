import unittest,sys
import connexion as co


class premierTest(unittest.TestCase):
        """
        Tests pour 1.py
        """

        def test0(self):
                bd, cursor = co.run()
                cursor.execute("SELECT id_activity FROM activity where nom_activity ='Triathlon'")
                id = cursor.fetchone()
                """
                test 0
                """
                self.assertEquals(8301, id)

                
if __name__ == '__main__':
        unittest.main()