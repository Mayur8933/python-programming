import unittest
from cities import city_info

class CityTestCases(unittest.TestCase):

    def test_city_country(self):
        single_str = city_info("santiago","chile")
        self.assertEqual(single_str,"Santiago , Chile")

    def test_city_country2(self):
        single_str2 = city_info("MAYUR", "PATIL")
        self.assertEqual(single_str2, "Mayur , Patil")

if __name__ == '__main__':
    unittest.main()