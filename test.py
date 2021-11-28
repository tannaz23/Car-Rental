#!/usr/bin/env python
# -*- coding: utf-8 -*-

## IMPORTANT INFORMATION TO RUN THE TESTS!!
## run command 'python -m unittest test.py' 

import unittest
from unittest import mock
import main

class MockTest(unittest.TestCase):
    # Test cases for testing how mock works
    def setUp(self):
        pass
    
    def test_mock_functionality(self):
        with mock.patch('builtins.input', side_effect=["yes","no"]):
            result = main.test_mock()
            self.assertEqual(result, "no")

class CustomerAddition(unittest.TestCase):
    # Test cases for customer addition functionalities
    def setUp(self):
        self.good_name = 'Tannaz'
        self.good_surname = 'Kamandi'
        self.good_address = 'fake street 123'
        self.good_id = '1234567-A'
        self.good_credit_card = '1234567891234567'
        self.good_customer_registered_message = 'Customer registered successfully: Tannaz, Kamandi, fake street 123, 1234567-A, 1234567891234567.'

    def test_success_addition(self):
        with mock.patch('builtins.input', side_effect=[
            self.good_name,
            self.good_surname,
            self.good_address,
            self.good_id,
            self.good_credit_card
        ]):
            result = main.customers1()
            self.assertEqual(result, self.good_customer_registered_message)

def suite():
  # Test suite
  # See https://docs.python.org/3/library/unittest.html to understand what it is
  suite = unittest.TestSuite()
  suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestApp))
  return suite

def customerTestCases():
    # Test suite for customer functionality
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader())

if __name__ == '__main__':
  unittest.TextTestRunner(verbosity=2).run(suite())