from unittest import TestCase
from Forecast import Forecast

class TestForecast(TestCase):
    def test_api_str(self):
        forecast_inst = Forecast(coordinates= (38.9072, -77.0369))
        self.assertIsInstance(forecast_inst.api_url, str)

    def test_api_return_dict(self):
        forecast_inst = Forecast(coordinates=(38.9072, -77.0369))
        self.assertIsInstance(forecast_inst.api_landing, dict)

    pass
