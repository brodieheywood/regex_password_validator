from unittest import TestCase
from regex_password_validator import main


class TestPassword_validator(TestCase):
    def test_password_validator_empty(self):
        self.assertFalse(main.password_validator(''))

    def test_password_one_character(self):
        self.assertFalse(main.password_validator('a'))

    def test_password_validator_under_eight_chars(self):
        self.assertFalse(main.password_validator('Under8'))

    def test_password_validator_all_upper(self):
        self.assertFalse(main.password_validator('ALLUPPER'))

    def test_password_validator_all_lower(self):
        self.assertFalse(main.password_validator('alllower'))

    def test_password_validator_all_numbers(self):
        self.assertFalse(main.password_validator('66666666'))
