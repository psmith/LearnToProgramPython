import unittest
import a1

class TestA1(unittest.TestCase):
    def test_seconds_difference(self):
        self.assertEqual(a1.seconds_difference(1800.0, 3600.0), 1800.0)
        self.assertEqual(a1.seconds_difference(3600.0, 1800.0), -1800.0)
        self.assertEqual(a1.seconds_difference(1800.0, 2160.0), 360.0)
        self.assertEqual(a1.seconds_difference(1800.0, 1800.0), 0.0)

    def test_hours_difference(self):
        self.assertEqual(a1.hours_difference(1800.0, 3600.0), 0.5)
        self.assertEqual(a1.hours_difference(3600.0, 1800.0), -0.5)
        self.assertEqual(a1.hours_difference(1800.0, 2160.0), 0.1)
        self.assertEqual(a1.hours_difference(1800.0, 1800.0), 0.0)
        
    def test_to_float_hours(self):
        self.assertEqual(a1.to_float_hours(0, 15, 0), 0.25)
        self.assertEqual(a1.to_float_hours(2, 45, 9), 2.7525)
        self.assertEqual(a1.to_float_hours(1, 0, 36), 1.01)
        
    def test_to_24_hour_clock(self):
        self.assertEqual(a1.to_24_hour_clock(24), 0)
        self.assertEqual(a1.to_24_hour_clock(48), 0)
        self.assertEqual(a1.to_24_hour_clock(25), 1)
        self.assertEqual(a1.to_24_hour_clock(4), 4)
        self.assertEqual(a1.to_24_hour_clock(28.5), 4.5)
        
    def test_get_hours(self):
        self.assertEqual(a1.get_hours(3600), 1)
        
    def test_get_minuts(self):
        self.assertEqual(a1.get_minutes(0), 0)
        self.assertEqual(a1.get_minutes(63), 1)
        self.assertEqual(a1.get_minutes(59), 0)
        self.assertEqual(a1.get_minutes(61), 1)
        self.assertEqual(3, a1.get_minutes(237));
        self.assertEqual(3, a1.get_minutes(3800));
        self.assertEqual(1, a1.get_minutes(3660));
        
    def test_get_seconds(self):
        self.assertEqual(a1.get_seconds(0), 0)
        self.assertEqual(20, a1.get_seconds(3800))
        
    def test_time_from_utc(self):
        self.assertEqual(a1.time_from_utc(+0, 12.0), 12.0)
        self.assertEqual(a1.time_from_utc(+1, 12.0), 13.0)
        self.assertEqual(a1.time_from_utc(-1, 12.0), 11.0)
        self.assertEqual(a1.time_from_utc(+6, 6.0), 12.0)
        self.assertEqual(a1.time_from_utc(-7, 6.0), 23.0)
        self.assertEqual(a1.time_from_utc(-1, 0.0), 23.0)
        self.assertEqual(a1.time_from_utc(-1, 23.0), 22.0)
        self.assertEqual(a1.time_from_utc(+1, 23.0), 0.0)
        
    def test_time_to_utc(self):
        self.assertEqual(a1.time_to_utc(+0, 12.0), 12.0)
        self.assertEqual(a1.time_to_utc(+1, 12.0), 11.0)
        self.assertEqual(a1.time_to_utc(-1, 12.0), 13.0)
        self.assertEqual(a1.time_to_utc(-11, 18.0), 5.0)
        self.assertEqual(a1.time_to_utc(-1, 0.0), 1.0)
        self.assertEqual(a1.time_to_utc(-1, 23.0), 0.0)
    