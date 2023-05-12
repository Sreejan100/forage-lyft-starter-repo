
from datetime import datetime
from test.test_car import TestCalliope
from test.test_car import TestGlissade
from test.test_car import TestPalindrome
from test.test_car import TestRorschach
from test.test_car import TestThovex
import unittest

class Car():
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.TestCalliope  = TestCalliope()
        self.TestGlissade = TestGlissade()
        self.TestPalindrome = TestPalindrome()
        self.TestRorschach = TestRorschach()
        self.TestThovex = TestThovex()

    def needs_service(self):
        today = datetime.today().date()
        if (self.TestCalliope.test_battery_should_be_serviced()) or (self.TestCalliope.test_engine_should_be_serviced()) :
            return True
        elif (self.TestCalliope.test_battery_should_not_be_serviced()) or (self.TestCalliope.test_engine_should_not_be_serviced()):
            return False
        elif (self.TestGlissade.test_battery_should_be_serviced()) or (self.TestGlissade.test_engine_should_be_serviced()):
            return True
        elif (self.TestGlissade.test_battery_should_not_be_serviced()) or (self.TestGlissade.test_engine_should_not_be_serviced()):
            return False
        elif (self.TestPalindrome.test_battery_should_be_serviced()) or (self.TestPalindrome.test_engine_should_be_serviced()):
            return True
        elif (self.TestPalindrome.test_battery_should_not_be_serviced()) or (self.TestPalindrome.test_engine_should_not_be_serviced()):
            return False
        elif (self.TestRorschach.test_battery_should_be_serviced()) or (self.TestRorschach.test_engine_should_be_serviced()):
            return True
        elif (self.TestRorschach.test_battery_should_not_be_serviced()) or (self.TestRorschach.test_engine_should_not_be_serviced()):
            return False
        elif (self.TestThovex.test_battery_should_be_serviced()) or (self.TestThovex.test_engine_should_be_serviced()):
            return True
        else:
            return False
        
        
    
        
