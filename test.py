from single import *
from parkingManager import *
import unittest

class ParkingTest(unittest.TestCase):
    def test_getRemainingCost(self):
        tariff_loader = TariffMemoryLoader()
        capacity = 50
        parking_manager = ParkingManager(capacity, tariff_loader)
        Singleton().currentDate = datetime(2021, 12, 21, 16, 20)
        session = parking_manager.enter_parking('838')
        Singleton().currentDate = datetime(2021, 12, 21, 16, 50)
        money = parking_manager.GetRemainingCost(session.ticket_number)
        expected = 50
        self.assertEqual(expected, money)
