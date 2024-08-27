import unittest
from src.weather_fetcher import get_weather

class TestWeatherFetcher(unittest.TestCase):
    def test_get_weather(self):
        #Call the function
        temp, description = get_weather()

        #Basic Checks
        self.assertIsInstance(temp, (int, float), "Temperature")
        self.assertIsInstance(description, str, "Weather description")

        #Further checks can be added if needed

if __name__=='__main__':
    unittest.main()