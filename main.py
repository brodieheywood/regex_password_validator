# Brodie Heywood
# November 26, 2018

"""Regex Password Validator"""

import doctest
import re


def password_validator(password):
    """Test password strength.

    Indicate if password is strong.
    PARAM: password, a single string to test for password strength
    PRECONDITION: none
    POSTCONDITION: returns True if password is strong (>= 8 characters, upper and lowercase, >= 1 digit)
    RETURN: Boolean
    >>> password_validator('')
    False
    >>> password_validator('a')
    False
    >>> password_validator('Under8')
    False
    >>> password_validator('ALLUPPER')
    False
    >>> password_validator('alllower')
    False
    >>> password_validator('66666666')
    False
    >>> password_validator('abcdefG1')
    True
    """
    if re.match(r'^(?=.{8,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*', password):
        print(True)
    else:
        print(False)


def main():
    password = 'hello'
    password_validator(password)
    password = 'helloThere3'
    password_validator(password)
    password = ''
    password_validator(password)
    password = 'helloTherehowareyou'
    password_validator(password)


if __name__ == '__main__':
    main()
    doctest.testmod()
