"""

Sample tests

"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):


    def test_add_number(self):

        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substract_number(self):
        
        res = calc.sub(10, 4)

        self.assertEqual(res, 6)
        