import unittest
from cities2 import city_info2

class CityTestCases(unittest.TestCase):

    def test_city_country(self):
        single_str = city_info2("santiago","chile")
        self.assertEqual(single_str,"Santiago , Chile")

    def test_city_country2(self):
        single_str2 = city_info2("MAYUR", "PATIL")
        self.assertEqual(single_str2, "Mayur , Patil")

    def test_city_country_population(self):
        single_str3 = city_info2("santiago","chile",50000000)
        self.assertEqual(single_str3,"Santiago , Chile - Population 50000000")

if __name__ == '__main__':
    unittest.main()