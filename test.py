import unittest
from datetime import datetime

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires



class TestBattery(unittest.TestCase):
    def test_spindler_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        spindler = SpindlerBattery(today, last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        spindler = SpindlerBattery(today, last_service_date)
        self.assertFalse(spindler.needs_service())

    def test_nubbin_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        nubbin = NubbinBattery(today, last_service_date)
        self.assertTrue(nubbin.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        nubbin = NubbinBattery(today, last_service_date)
        self.assertFalse(nubbin.needs_service())
        
class TestEngine(unittest.TestCase):
    
    ###capulet################################

    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet.needs_service())
        
        ###sternman################################
        
    def test_sternman_engine_should_be_serviced(self):
        warning_light_is_on = True

        sternman = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman.needs_service())

    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        sternman = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman.needs_service())
        
        ###willoughby################################

    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby.needs_service())

    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())
        
class TestTires(unittest.TestCase):
    def test_carrigan_tires_should_be_serviced(self):
        tire_wear = [1,0.8,0.4,0.6]

        carrigan = CarriganTires(tire_wear)
        self.assertTrue(carrigan.needs_service())

    def test_carrigan_tires_should_not_be_serviced(self):
        tire_wear = [0.3,0.8,0.4,0.6]

        carrigan = CarriganTires(tire_wear)
        self.assertFalse(carrigan.needs_service())

    def test_octoprime_tires_should_be_serviced(self):
        tire_wear = [1.4,0.9,0.4,0.6]

        octoprime = OctoprimeTires(tire_wear)
        self.assertTrue(octoprime.needs_service())

    def test_octoprime_tires_should_not_be_serviced(self):
        tire_wear = [0.1,0.8,0.4,0.2]

        octoprime = OctoprimeTires(tire_wear)
        self.assertFalse(octoprime.needs_service())

if __name__ == '__main__':
    unittest.main()
