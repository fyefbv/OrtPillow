import unittest
from order_form import validate_date, validate_phone

class OrderValidationTests(unittest.TestCase):
    def test_valid_dates(self):
        self.assertTrue(validate_date("2023-12-31"))
        self.assertTrue(validate_date("2024-02-29"))  # Leap year
        
    def test_invalid_dates(self):
        self.assertFalse(validate_date("31-12-2023"))  # Wrong format
        self.assertFalse(validate_date("2023-13-01"))  # Invalid month
        self.assertFalse(validate_date("2023-00-15"))  # Zero month

    def test_valid_phones(self):
        self.assertTrue(validate_phone("+79211234567"))
        self.assertTrue(validate_phone("+74957778899"))
        
    def test_invalid_phones(self):
        self.assertFalse(validate_phone("89211234567"))  # Missing +
        self.assertFalse(validate_phone("+7921"))       # Too short
        self.assertFalse(validate_phone("+7abc1234567")) # Letters

if __name__ == '__main__':
    unittest.main()