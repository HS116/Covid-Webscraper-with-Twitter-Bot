import unittest
import covid_Webscraper_and_Twitter as app

class Tests(unittest.TestCase):
    #Unit tests for 12th April 10:48 PM
    def test_HongKong(self):
        self.assertEqual(app.countryData["Hong Kong"], "156,505")

    def test_Germany(self):
        self.assertEqual(app.countryData["Germany"], "269,162")

    def test_India(self):
        self.assertEqual(app.countryData["India"], "30,651")

    def test_USA(self):
        self.assertEqual(app.countryData["USA"], "245,425")


if __name__ == "__main__":
    unittest.main()





