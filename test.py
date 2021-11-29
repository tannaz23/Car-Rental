#!/usr/bin/env python
# -*- coding: utf-8 -*-

## IMPORTANT INFORMATION TO RUN THE TESTS!!
## run command 'python -m unittest test.py' 

import unittest
from unittest import mock
from unittest.mock import patch
import main
import io

class MockTest(unittest.TestCase):
    # Test cases for testing how mock works
    def setUp(self):
        pass
    
    def test_mock_functionality(self):
        with mock.patch('builtins.input', side_effect=["yes","no"]):
            result = main.test_mock()
            self.assertEqual(result, "no")

class CustomerAddition(unittest.TestCase):
    # Test case 12
    # Test cases for customer addition functionality successfull
    def setUp(self):
        self.maxDiff = None
        self.good_name = 'Tannaz'
        self.good_surname = 'Kamandi'
        self.good_address = 'fake street 123'
        self.good_id = '1234567-A'
        self.good_credit_card = '1234567891234567'
        self.good_customer_registered_message = 'Customer registered successfully: Tannaz, Kamandi, fake street 123, 1234567-A, 1234567891234567.'

    def test_format_name(self):
        # First name function
        with mock.patch('builtins.input', side_effect=[
            self.good_name,
        ]):
            result = main.get_first_name()
            self.assertEqual(result, self.good_name)
    
    def test_format_surname(self):
        # Last name function
        with mock.patch('builtins.input', side_effect=[
            self.good_surname,
        ]):
            result = main.get_last_name()
            self.assertEqual(result, self.good_surname)
    
    def test_format_address(self):
        # Address function
        with mock.patch('builtins.input', side_effect=[
            self.good_address,
        ]):
            result = main.get_address()
            self.assertEqual(result, self.good_address)
    
    def test_format_id(self):
        # ID function
        with mock.patch('builtins.input', side_effect=[
            self.good_id
        ]):
            result = main.get_passport_id()
            self.assertEqual(result, self.good_id)
    
    def test_bad_format_credit_card(self):
        # Credit card function
        with mock.patch('builtins.input', side_effect=[
            self.good_credit_card,
        ]):
            result = main.get_credit_card()
            self.assertEqual(result, self.good_credit_card)
    
    @unittest.expectedFailure
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_customer_addition(self, mock_stdout):
        # Customer addition function
        with mock.patch('builtins.input', side_effect=[
            self.good_name,
            self.good_surname,
            self.good_address,
            self.good_id,
            self.good_credit_card
        ]):
            main.customers1()
            self.assertEqual(mock_stdout.getvalue(), self.good_customer_registered_message)


class CustomerAdditionBadFormat(unittest.TestCase):
    # Test case 13
    # Test cases for customer addition functionality with bad formats
    # for name, surname, address (it will get shortened), id and credit card
    def setUp(self):
        self.maxDiff = None
        self.bad_format_name = 'Tanna7'
        self.good_format_name = 'Tannaz'
        self.bad_format_name_message = 'Only letters are allowed, try again\n'
        self.bad_format_surname = 'Kam4ndi'
        self.good_format_surname = 'Kamandi'
        self.bad_format_surname_message = 'Only letters are allowed, try again\n'
        self.bad_format_address = 'fake s7reet *********************'
        self.good_format_address = 'fake s7reet ******************'
        self.bad_format_id = '123-W'
        self.good_format_id = '7894561-Z'
        self.bad_format_id_message = 'Passport number or ID format is SSSSSSS-A, where SSSSSSS is the seven-digit serial number and A is the literal, please correct your input\n'
        self.bad_format_credit_card = '456 555'
        self.good_format_credit_card = '7896321458963214'
        self.bad_format_credit_card_message = 'Expected input for the credit card number is 16 digits without blank spaces, please try again\n'
        self.customer_addition_success = 'Customer registered successfully: Tannaz, Kamandi, fake s7reet ******************, 7894561-Z, 7896321458963214\n'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_name(self, mock_stdout):
        # First name function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_name,
            self.good_format_name,
        ]):
            result = main.get_first_name()
            self.assertEqual(mock_stdout.getvalue(), self.bad_format_name_message)
            self.assertEqual(result, self.good_format_name)
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_surname(self, mock_stdout):
        # Last name function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_surname,
            self.good_format_surname,
        ]):
            result = main.get_first_name()
            self.assertEqual(mock_stdout.getvalue(), self.bad_format_surname_message)
            self.assertEqual(result, self.good_format_surname)
    
    def test_bad_format_address(self):
        # Address function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_address,
        ]):
            result = main.get_address()
            self.assertEqual(result, self.good_format_address)
    
    @unittest.expectedFailure
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_id(self, mock_stdout):
        # ID function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_id,
            self.good_format_id
        ]):
            result = main.get_passport_id()
            self.assertEqual(mock_stdout.getvalue(), self.bad_format_id_message)
            self.assertEqual(result, self.good_format_id)
    
    @unittest.expectedFailure
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_credit_card(self, mock_stdout):
        # Credit card function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_credit_card,
            self.good_format_credit_card
        ]):
            result = main.get_credit_card()
            self.assertEqual(mock_stdout.getvalue(), self.bad_format_credit_card_message)
            self.assertEqual(result, self.good_format_credit_card)
    
    @unittest.expectedFailure
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_customer_addition(self, mock_stdout):
        # Customer addition function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_name,
            self.good_format_name,
            self.bad_format_surname,
            self.good_format_surname,
            self.bad_format_address,
            self.bad_format_id,
            self.good_format_id,
            self.bad_format_credit_card,
            self.good_format_credit_card,

        ]):
            main.customers1()
            self.assertEqual(mock_stdout.getvalue(), self.customer_addition_success)

class CustomerListAllAndAddNew(unittest.TestCase):
    # Test case 14
    # Test cases for customer list display and addition functionality 
    def setUp(self):
        self.maxDiff = None
        self.list_menu = 'Register new customers(1)\nDelete a customer(2)\nGo back(3)\n'
        self.selected_option = 1
        self.good_format_name = 'Tannaz'
        self.good_format_surname = 'Kamandi'
        self.good_format_address = 'fake street 123'
        self.good_format_id = '1234567-A'
        self.good_format_credit_card = '1234567891234560'
        self.customer_addition_success = 'Customer registered successfully: Tannaz, Kamandi, fake street 123, 1234567-A, 1234567891234560\n'

    @unittest.expectedFailure
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_customers_and_add(self, mock_stdout):
        # Customer list current customers
        with mock.patch('builtins.input', side_effect=[
            self.selected_option,
            self.good_format_name,
            self.good_format_surname,
            self.good_format_address,
            self.good_format_id,
            self.good_format_credit_card
        ]):
            main.listcustomers()
            self.assertIn(self.list_menu, mock_stdout.getvalue())
            self.assertIn(self.customer_addition_success, mock_stdout.getvalue())

class CustomerListAllAndDelete(unittest.TestCase):
    # Test case 15
    # Test cases for customer list display and drop customer functionality 
    # testing bad format, not finding and success for dropping customer
    def setUp(self):
        self.maxDiff = None
        self.list_menu = 'Register new customers(1)\nDelete a customer(2)\nGo back(3)\n'
        self.selected_option = 2
        self.bad_format_id = '516-P'
        self.bad_id = '7418529-P'
        self.bad_id_message = 'The customer with that passport number/id does not exist, do you want to try again ? (y/n)\n'
        self.yes_or_not_option = 'Y'
        self.good_format_id = '1234567-A '

    @unittest.expectedFailure
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_customers_and_drop(self, mock_stdout):
        # Customer list current customers
        with mock.patch('builtins.input', side_effect=[
            self.selected_option,
            self.bad_format_id,
            self.bad_id,
            self.yes_or_not_option,
            self.good_format_id,
        ]):
            main.listcustomers()
            self.assertIn(self.list_menu, mock_stdout.getvalue())
            self.assertIn(self.bad_id_message, mock_stdout.getvalue())
    
class CustomerListAllAndDeleteNotFind(unittest.TestCase):
    # Test case 16
    # Test cases for customer list display and drop customer functionality 
    # testing not finding and go back to menu
    def setUp(self):
        self.maxDiff = None
        self.list_menu = 'Register new customers(1)\nDelete a customer(2)\nGo back(3)\n'
        self.selected_option = 2
        self.bad_id = '7418529-P'
        self.bad_id_message = 'The customer with that passport number/id does not exist, do you want to try again ? (y/n)\n'
        self.yes_or_not_option = 'N'

    @unittest.expectedFailure
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_customers_and_drop_failed(self, mock_stdout):
        # Customer list current customers
        with mock.patch('builtins.input', side_effect=[
            self.selected_option,
            self.bad_id,
            self.yes_or_not_option
        ]):
            main.listcustomers()
            self.assertIn(self.list_menu, mock_stdout.getvalue())
            self.assertIn(self.bad_id_message, mock_stdout.getvalue())
 
class CustomerListAllAndGoBack(unittest.TestCase):
    # Test case 17
    # Test cases for customer list display and go back to customer menu
    # testing not finding and go back to menu
    def setUp(self):
        self.maxDiff = None
        self.list_menu = 'Register new customers(1)\nDelete a customer(2)\nGo back(3)\n'
        self.selected_option = 3
        self.customer_menu = '------Customer menu------\nRegister new customer(1)\nList of current customers(2)\nSearch for a customer(3)\nGo back(4)\n'

    @unittest.expectedFailure
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_customers_go_back(self, mock_stdout):
        # Customer list current customers
        with mock.patch('builtins.input', side_effect=[
            self.selected_option
        ]):
            main.listcustomers()
            self.assertIn(self.list_menu, mock_stdout.getvalue())
            self.assertIn(self.customer_menu, mock_stdout.getvalue())

class CustomerSearch(unittest.TestCase):
    # Test case 18
    # Test cases for customer search with bad format first
    # not finding after and finally display one found
    def setUp(self):
        self.maxDiff = None
        self.bad_format_id = '5646-8'
        self.bad_format_message = 'Passport number or ID format is SSSSSSS-A, where SSSSSSS is the seven-digit serial number and A is the literal, please correct your input\n'
        self.bad_id = '7418529-P'
        self.bad_message = 'The customer with that passport number/id does not exist, do you want to try again ? (y/n)\n'
        self.yes_or_not_option = 'Y'
        self.good_id = '7894561-Z'
        self.success_message = 'Customer found: Tannaz, Kamandi, fake s7reet ******************, 7894561-Z, 7896321458963214'

    @unittest.expectedFailure
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_customer_success(self, mock_stdout):
        # Customer search customer
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_id,
            self.bad_id,
            self.yes_or_not_option,
            self.good_id
        ]):
            main.searchcustomer()
            self.assertIn(self.bad_format_message, mock_stdout.getvalue())
            self.assertIn(self.bad_message, mock_stdout.getvalue())
            self.assertIn(self.success_message, mock_stdout.getvalue())

class CustomerSearchAndBack(unittest.TestCase):
    # Test case 19
    # Test cases for customer search 
    # not finding id and go back to customer menu
    def setUp(self):
        self.maxDiff = None
        self.bad_id = '7418529-P'
        self.bad_message = 'The customer with that passport number/id does not exist, do you want to try again ? (y/n)\n'
        self.yes_or_not_option = 'N'
    
    #@unittest.expectedFailure
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_customer_failed_back(self, mock_stdout):
        # Customer search customer failed and go back to
        # customer main menu
        with mock.patch('builtins.input', side_effect=[
            self.bad_id,
            self.yes_or_not_option,
        ]):
            main.searchcustomer()
            self.assertIn(self.bad_message, mock_stdout.getvalue())

def customerTestCases():
    # Test suite for customer functionality
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader())

if __name__ == '__main__':
  unittest.TextTestRunner(verbosity=2).run(suite())