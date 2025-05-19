import unittest
from reviews_form import validate_review_data, validate_author, validate_phone, validate_text

class ReviewValidationTests(unittest.TestCase):
    def test_valid_data(self):
        data = {
            'author': 'Roman',
            'text': 'Great pillow!',
            'phone': '+7 (999) 123-45-67'
        }
        self.assertEqual(validate_review_data(data), {})

    def test_invalid_data(self):
        data = {
            'author': 'A',
            'text': 'odmemv',
            'phone': 'akwfok,'
        }
        errors = validate_review_data(data)
        self.assertEqual(len(errors), 3)
        self.assertEqual(errors['author'], 'Name must be at least 3 characters')
        self.assertEqual(errors['text'], 'Review must be at least 10 characters')
        self.assertEqual(errors['phone'], 'Invalid phone format')

    def test_valid_author(self):
        self.assertIsNone(validate_author('Roman'))

        self.assertIsNone(validate_author('ake_akf'))

        self.assertIsNone(validate_author('Abc'))

        self.assertIsNone(validate_author('A' * 15))

    def test_invalid_author(self):
        self.assertEqual(validate_author(''), 'Name field is required')

        self.assertEqual(validate_author('    '), 'Name field is required')

        self.assertEqual(validate_author('Ab'), 'Name must be at least 3 characters')

        self.assertEqual(validate_author('A' * 16), 'Name cannot exceed 15 characters')
        
    def test_valid_text(self):
        self.assertIsNone(validate_text('Yes, your pillows are good!'))

        self.assertIsNone(validate_text('sfokefokef'))

        self.assertIsNone(validate_text('A' * 1000))

    def test_invalid_text(self):
        self.assertEqual(validate_text(''), 'Review field is required')

        self.assertEqual(validate_text('    '), 'Review field is required')

        self.assertEqual(validate_text('Short'), 'Review must be at least 10 characters')

        self.assertEqual(validate_text('A' * 1001), 'Review cannot exceed 300 characters')

    def test_valid_phone(self):
        valid_phones = [
            '+7 (574) 356-23-63',
            '+7 (999) 123-45-67'
        ]
        
        for phone in valid_phones:
            self.assertIsNone(validate_phone(phone))

    def test_invalid_phone(self):
        self.assertEqual(validate_phone(''), 'Phone field is required')

        self.assertEqual(validate_phone('    '), 'Phone field is required')

        invalid_phones = [
            '89991234567',
            '+7 999 123-45-67',
            '+7(999)123-45-67',
            '+7 (999) 123-45-6',
            '+7 (abc) 123-45-67',
        ]
        
        for phone in invalid_phones:
            self.assertEqual(validate_phone(phone), 'Invalid phone format')

if __name__ == '__main__':
    unittest.main()