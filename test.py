#!/usr/bin/env python
# -*- coding: utf-8 -*-

## IMPORTANT INFORMATION TO RUN THE TESTS!!
## run command to test with this file 'python -m unittest test.py' 

## run command  to run coverage package over tests 'coverage run -m unittest discover'
## then run 'coverage report' or 'coverage html' 
import unittest
from unittest import mock
from unittest.mock import patch
import main
import io


class OrdersRegister(unittest.TestCase):
    # Test case 1
    # Test case for the option to register a new order
    # first incorrect formats are inputted for ID, pick up date,
    # return date and also car selected, then correct options
    def setUp(self):
        self.maxDiff = None
        self.bad_format_id = '78916-VV'
        self.bad_format_id_message = 'Passport number is incorrect, try again!'
        self.good_id = '1234567-A'
        self.good_id_message = 'Customer found!'
        self.bad_format_pickupdate = 'Adsdsd'
        self.bad_format_pickupdate_message = 'Incorrect date format, try again!'
        self.good_pickupdate = '20/06/1997'
        self.bad_format_returndate = '4444/44/44'
        self.bad_format_returndate_message = 'Incorrect date format, try again!'
        self.good_returndate = '19/06/1997'
        self.bad_car_selection = 'Z'
        self.bad_car_selection_message = 'Invalid option. Please try again'
        self.good_car_selection = '1'
        self.good_car_selection_message = 'Order registered!'
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_order_register_success(self, mock_stdout):
        # Orders menu option register with some bad formats
        # and finally register successfully
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_id,
            self.good_id,
            self.bad_format_pickupdate,
            self.good_pickupdate,
            self.bad_format_returndate,
            self.good_returndate,
            self.bad_car_selection,
            self.good_car_selection
        ]):
            main.register_order()
            self.assertIn(self.bad_format_id_message, mock_stdout.getvalue())
            self.assertIn(self.bad_format_pickupdate_message, mock_stdout.getvalue())
            self.assertIn(self.bad_format_returndate_message, mock_stdout.getvalue())
            self.assertIn(self.bad_car_selection_message, mock_stdout.getvalue())
            self.assertIn(self.good_car_selection_message, mock_stdout.getvalue())


class OrdersRegisterFailed(unittest.TestCase):
    # Test case 2
    # Test case for the option to register a new order
    # non exitent customer and unavailable car option but then correct order
    def setUp(self):
        self.maxDiff = None
        self.bad_id = '7891690-V'
        self.bad_format_id_message = 'User does not exist, do you want to try again ? (y/n)'
        self.yes_not_selection_id = 'Y'
        self.good_id = '1234567-A'
        self.good_id_message = 'Customer found!'
        self.good_pickupdate = '20/06/1997'
        self.good_returndate = '19/06/1997'
        self.bad_car_selection = '3'
        self.bad_car_selection_message = 'Car of type COUPE is unavailable, Do you want to pick another type (y/n)'
        self.yes_not_selection_car = 'Y'
        self.good_car_selection = '2'
        self.good_car_selection_message = 'Order registered!'
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_order_register_failed_success(self, mock_stdout):
        # Orders menu option register with bad inputs then good
        # and finally register successfully
        with mock.patch('builtins.input', side_effect=[
            self.bad_id,
            self.yes_not_selection_id,
            self.good_id,
            self.good_pickupdate,
            self.good_returndate,
            self.bad_car_selection,
            self.yes_not_selection_car,
            self.good_car_selection
        ]):
            main.register_order()
            self.assertIn(self.bad_format_id_message, mock_stdout.getvalue())
            self.assertIn(self.good_id_message, mock_stdout.getvalue())
            self.assertIn(self.bad_car_selection_message, mock_stdout.getvalue())
            self.assertIn(self.good_car_selection_message, mock_stdout.getvalue())

class OrdersRegisterNotFound(unittest.TestCase):
    # Test case 3
    # Test case for the option to register a new order
    # non exitent customer and go back to order menu
    def setUp(self):
        self.maxDiff = None
        self.bad_id = '7891690-V'
        self.bad_format_id_message = 'User does not exist, do you want to try again ? (y/n)'
        self.yes_not_selection_id = 'P'
        self.orders_menu = '''
        ------OPTIONS------\n
        Register an order(1)\n
        Delete an order(2)\n
        Print an order list(3)\n
        Search for a specific order(4)\n
        Go back(5)\n
        '''
        self.last_selection = '5'
        self.final_selection = '5'
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_order_register_not_found_back(self, mock_stdout):
        # Orders menu option register with not found customer
        # and finally go backl to order menu
        with mock.patch('builtins.input', side_effect=[
            self.bad_id,
            self.yes_not_selection_id,
            self.last_selection,
            self.final_selection
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.register_order()
                self.assertIn(self.bad_format_id_message, mock_stdout.getvalue())
                self.assertIn(self.orders_menu, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

class OrdersRegisterNotAvailable(unittest.TestCase):
    # Test case 4
    # Test case for the option to register a new order
    # not available car and go back to order menu
    def setUp(self):
        self.maxDiff = None
        self.good_id = '1234567-A'
        self.good_id_message = 'Customer found!'
        self.good_pickupdate = '20/06/1997'
        self.good_returndate = '19/06/1997'
        self.bad_car_selection = '4'
        self.bad_car_selection_message = 'Car of type SUV is unavailable, Do you want to pick another type (y/n)'
        self.yes_not_selection_car = 'S'
        self.orders_menu = '''
        ------OPTIONS------\n
        Register an order(1)\n
        Delete an order(2)\n
        Print an order list(3)\n
        Search for a specific order(4)\n
        Go back(5)\n
        '''
        self.final_selection = '5'
        self.final_selection_main_menu = '5'
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_order_register_not_available_back(self, mock_stdout):
        # Orders menu option register with not available car
        # and finally go to orders menu
        with mock.patch('builtins.input', side_effect=[
            self.good_id,
            self.good_pickupdate,
            self.good_returndate,
            self.bad_car_selection,
            self.yes_not_selection_car,
            self.final_selection,
            self.final_selection_main_menu
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.register_order()
                self.assertIn(self.good_id_message, mock_stdout.getvalue())
                self.assertIn(self.bad_car_selection_message, mock_stdout.getvalue())
                self.assertIn(self.orders_menu, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)


class OrdersDropSuccessfully(unittest.TestCase):
    # Test case 5
    # Test case for the option to drop orders
    # with bad format and not existing ID
    # and finally drop successfully
    def setUp(self):
        self.maxDiff = None
        self.bad_format_id = 'PP'
        self.bad_format_id_message = 'Invalid order id format! Try again'
        self.bad_id = '999'
        self.bad_id_message = 'The order 999 does not exist, do you want to try again?(Y/N)'
        self.yes_not_option = 'Y'
        self.good_id = '42'
        self.good_id_message = 'Order with the id of 2 has been successfully deleted'
        self.final_selection = '5'
        self.final_selection_main_menu = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_order_drop(self, mock_stdout):
        # Orders menu option drop with no good format,
        # then not available and finally success
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_id,
            self.bad_id,
            self.yes_not_option,
            self.good_id,
            self.final_selection,
            self.final_selection_main_menu
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.delete_order()
                self.assertIn(self.bad_format_id_message, mock_stdout.getvalue())
                self.assertIn(self.bad_id_message, mock_stdout.getvalue())
                self.assertIn(self.good_id_message, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

class OrdersDropNotFound(unittest.TestCase):
    # Test case 6
    # Test case for the option to drop orders
    # not existing ID and finally go to orders menu
    def setUp(self):
        self.maxDiff = None
        self.bad_id = '999'
        self.bad_id_message = 'The order 999 does not exist, do you want to try again?(Y/N)'
        self.yes_not_option = 'I'
        self.orders_menu = '''
            ------OPTIONS------\n
            Register an order(1)\n
            Delete an order(2)\n
            Print an order list(3)\n
            Search for a specific order(4)\n
            Go back(5)\n
            '''
        self.final_selection = '5'
        self.final_selection_main_menu = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_order_drop(self, mock_stdout):
        # Orders menu option drop with not found
        # then go to orders menu
        with mock.patch('builtins.input', side_effect=[
            self.bad_id,
            self.yes_not_option,
            self.final_selection,
            self.final_selection_main_menu
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.delete_order()
                self.assertIn(self.bad_id_message, mock_stdout.getvalue())
                self.assertIn(self.orders_menu, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

class OrdersListAndSearch(unittest.TestCase):
    # Test case 7
    # Test case for the option to list orders
    # and then search for specific one
    def setUp(self):
        self.maxDiff = None
        self.print_menu = '''
        -------OPTIONS-------\n
        Search for a specific order(1)\n
        Go back(2)\n
        '''
        self.order_list_option = '3'
        self.selection_list = '1'
        self.bad_id = '999'
        self.bad_id_message = 'Order id 999 does not exist, do you want to try again ? (Y/y)'
        self.selection_search = 'I'
        self.final_selection = '5'
        self.final_selection_main_menu = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_and_search(self, mock_stdout):
        # Orders menu option list all orders
        # select the search option and go out
        with mock.patch('builtins.input', side_effect=[
            self.order_list_option,
            self.selection_list,
            self.bad_id,
            self.selection_search,
            self.final_selection,
            self.final_selection_main_menu
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.orders()
                self.assertIn(self.print_menu, mock_stdout.getvalue())
                self.assertIn(self.bad_id_message, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

class OrdersListAndGoBack(unittest.TestCase):
    # Test case 8
    # Test case for the option to list orders
    # and then go back to orders menu
    def setUp(self):
        self.maxDiff = None
        self.print_menu = '''
        -------OPTIONS-------\n
        Search for a specific order(1)\n
        Go back(2)\n
        '''
        self.order_list_option = 3
        self.selection_list = 2
        self.final_selection = '5'
        self.final_selection_main_menu = '5'
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_and_back(self, mock_stdout):
        # Orders menu option list all orders
        # and go back to orders menu
        with mock.patch('builtins.input', side_effect=[
            self.order_list_option,
            self.selection_list,
            self.final_selection,
            self.final_selection_main_menu
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.orders()
                self.assertIn(self.print_menu, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

class OrdersSearchAndGoBack(unittest.TestCase):
    # Test case 9
    # Test case for the option search specific
    # order first failing, formats. then not found
    # finally success an go to orders menu
    def setUp(self):
        self.maxDiff = None
        self.bad_format_id = 'Y'
        self.bad_format_message = 'Invalid order id format! Try again'
        self.bad_id = '999'
        self.bad_id_message = 'Order id 999 does not exist, do you want to try again ? (Y/y)'
        self.yes_not_option = 'Y'
        self.good_id = '2'
        self.good_id_message = 'Order found!'
        self.search_menu = '''
        -----options ------\n
        Delete the order(1)\n
        Go back(2)\n
        '''
        self.option_selection = '2'
        self.final_selection = '5'
        self.final_selection_main_menu = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_and_back(self, mock_stdout):
        # Orders menu option search an order
        # and go back to orders menu
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_id,
            self.bad_id,
            self.yes_not_option,
            self.good_id,
            self.option_selection,
            self.final_selection,
            self.final_selection_main_menu
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.search_order()
                self.assertIn(self.bad_format_message, mock_stdout.getvalue())
                self.assertIn(self.bad_id_message, mock_stdout.getvalue())
                self.assertIn(self.good_id_message, mock_stdout.getvalue())
                self.assertIn(self.search_menu, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

class OrdersSearchAndDelete(unittest.TestCase):
    # Test case 10
    # Test case for the option search specific
    # order and delete the one selected
    def setUp(self):
        self.maxDiff = None
        self.good_id = '4'
        self.search_menu = '''
        -----options ------\n
        Delete the order(1)\n
        Go back(2)\n
        '''
        self.option_selected = '1'
        self.id_to_delete = '4'
        self.delete_message = 'Order with the id of 4 has been successfully deleted\n'
        self.final_selection = '5'
        self.final_selection_main_menu = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_and_delete(self, mock_stdout):
        # Orders menu option search an order
        # and delete the one selected
        with mock.patch('builtins.input', side_effect=[
            self.good_id,
            self.option_selected,
            self.id_to_delete,
            self.final_selection,
            self.final_selection_main_menu
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.search_order()
                self.assertIn(self.search_menu, mock_stdout.getvalue())
                self.assertIn(self.delete_message, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)


class OrdersBackMenu(unittest.TestCase):
    # Test case 11
    # Test case for the option to go main menu from orders
    def setUp(self):
        self.maxDiff = None
        self.orders_selection = '5'
        self.main_menu = '-------Main Menu-------\nOrders(1)\nCars(2)\nCustomers(3)\nRegister an Order(4)\nExit(5)\n'
        self.final_selection_main_menu = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_order_to_main_menu(self, mock_stdout):
        # Orders menu option to main menu
        with mock.patch('builtins.input', side_effect=[
            self.orders_selection,
            self.final_selection_main_menu
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.orders()
                self.assertIn(self.main_menu, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)


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
            
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_good_format_customer_addition(self, mock_stdout):
        # Customer addition function
        with mock.patch('builtins.input', side_effect=[
            self.good_name,
            self.good_surname,
            self.good_address,
            self.good_id,
            self.good_credit_card
        ]):
            main.add_new_customer()
            self.assertIn(self.good_customer_registered_message, mock_stdout.getvalue())

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
        self.customer_addition_success = 'Customer registered successfully: Tannaz, Kamandi, fake s7reet ******************, 7894561-Z, 7896321458963214.\n'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_name(self, mock_stdout):
        # First name function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_name,
            self.good_format_name,
        ]):
            result = main.get_first_name()
            self.assertIn(self.bad_format_name_message, mock_stdout.getvalue())
            self.assertEqual(result, self.good_format_name)
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_surname(self, mock_stdout):
        # Last name function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_surname,
            self.good_format_surname,
        ]):
            result = main.get_first_name()
            self.assertIn(self.bad_format_surname_message, mock_stdout.getvalue())
            self.assertEqual(result, self.good_format_surname)
    
    def test_bad_format_address(self):
        # Address function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_address,
        ]):
            result = main.get_address()
            self.assertEqual(result, self.good_format_address)
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_id(self, mock_stdout):
        # ID function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_id,
            self.good_format_id
        ]):
            result = main.get_passport_id()
            self.assertIn( self.bad_format_id_message, mock_stdout.getvalue())
            self.assertEqual(result, self.good_format_id)
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_credit_card(self, mock_stdout):
        # Credit card function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_credit_card,
            self.good_format_credit_card
        ]):
            result = main.get_credit_card()
            self.assertIn(self.bad_format_credit_card_message, mock_stdout.getvalue())
            self.assertEqual(result, self.good_format_credit_card)
            
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
            main.add_new_customer()
            self.assertIn(self.customer_addition_success, mock_stdout.getvalue())

class CustomerListAllAndAddNew(unittest.TestCase):
    # Test case 14
    # Test cases for customer list display and addition functionality 
    def setUp(self):
        self.maxDiff = None
        self.list_menu = 'Register new customers(1)\nDelete a customer(2)\nGo back(3)\n'
        self.selected_option = '1'
        self.good_format_name = 'Tannaz'
        self.good_format_surname = 'Kamandi'
        self.good_format_address = 'fake street 123'
        self.good_format_id = '1234567-A'
        self.good_format_credit_card = '1234567891234560'
        self.customer_addition_success = 'Customer registered successfully: Tannaz, Kamandi, fake street 123, 1234567-A, 1234567891234560.\n'

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
            main.list_customers()
            self.assertIn(self.list_menu, mock_stdout.getvalue())
            self.assertIn(self.customer_addition_success, mock_stdout.getvalue())

class CustomerListAllAndDelete(unittest.TestCase):
    # Test case 15
    # Test cases for customer list display and drop customer functionality 
    # testing bad format, not finding and success for dropping customer
    def setUp(self):
        self.maxDiff = None
        self.list_menu = 'Register new customers(1)\nDelete a customer(2)\nGo back(3)\n'
        self.selected_option = '2'
        self.bad_format_id = '516-P'
        self.bad_id = '7418529-P'
        self.bad_id_message = 'The customer with that passport 7418529-P does not exist, do you want to try again ? (y/n)'
        self.yes_or_not_option = 'Y'
        self.good_format_id = '1234567-A'
        
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
            main.list_customers()
            self.assertIn(self.list_menu, mock_stdout.getvalue())
            self.assertIn(self.bad_id_message, mock_stdout.getvalue())

class CustomerListAllAndDeleteNotFind(unittest.TestCase):
    # Test case 16
    # Test cases for customer list display and drop customer functionality 
    # testing not finding and go back to menu
    def setUp(self):
        self.maxDiff = None
        self.list_menu = 'Register new customers(1)\nDelete a customer(2)\nGo back(3)\n'
        self.selected_option = '2'
        self.bad_id = '7418529-P'
        self.bad_id_message = 'The customer with that passport 7418529-P does not exist, do you want to try again ? (y/n)\n'
        self.yes_or_not_option = 'N'
        self.final_selection = '4'
        self.final_menu_selection = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_customers_and_drop_failed(self, mock_stdout):
        # Customer list current customers
        with mock.patch('builtins.input', side_effect=[
            self.selected_option,
            self.bad_id,
            self.yes_or_not_option,
            self.final_selection,
            self.final_menu_selection
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.list_customers()
                self.assertIn(self.list_menu, mock_stdout.getvalue())
                self.assertIn(self.bad_id_message, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)
 
class CustomerListAllAndGoBack(unittest.TestCase):
    # Test case 17
    # Test cases for customer list display and go back to customer menu
    # testing not finding and go back to menu
    def setUp(self):
        self.maxDiff = None
        self.list_menu = '-----What to do now?------\nRegister new customers(1)\nDelete a customer(2)\nGo back(3)\nPlease, select an option\n'
        self.selected_option = '3'
        self.final_selection = '4'
        self.final_selection_main_menu = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_customers_go_back(self, mock_stdout):
        # Customer list current customers
        with mock.patch('builtins.input', side_effect=[
            self.selected_option,
            self.final_selection,
            self.final_selection_main_menu
        ]):

            with self.assertRaises(SystemExit) as cm:
                 main.list_customers()
                 self.assertIn(self.list_menu, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

class CustomerSearch(unittest.TestCase):
    # Test case 18
    # Test cases for customer search with bad format first
    # not finding after and finally display one found
    def setUp(self):
        self.maxDiff = None
        self.bad_format_id = '5646-8'
        self.bad_format_message = 'Passport number or ID format is SSSSSSS-A, where SSSSSSS is the seven-digit serial number and A is the literal, please correct your input\n'
        self.bad_id = '7418529-P'
        self.bad_message = 'The customer with that passport 7418529-P does not exist, do you want to try again ? (y/n)'
        self.yes_or_not_option = 'Y'
        self.good_id = '7894561-Z'
        self.success_message = 'Customer found: Tannaz, Kamandi, fake s7reet ******************, 7894561-Z, 7896321458963214'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_customer_success(self, mock_stdout):
        # Customer search customer
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_id,
            self.bad_id,
            self.yes_or_not_option,
            self.good_id
        ]):
            main.search_customer()
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
        self.final_selection = '4'
        self.final_selection_main_menu = '5'

    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_customer_failed_back(self, mock_stdout):
        # Customer search customer failed and go back to
        # customer main menu
        with mock.patch('builtins.input', side_effect=[
            self.bad_id,
            self.yes_or_not_option,
            self.final_selection,
            self.final_selection_main_menu
        ]):
            with self.assertRaises(SystemExit) as cm:
                  main.search_customer()
                  self.assertIn(self.bad_message, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)
           
class CarShowList(unittest.TestCase):
    # Test case 20
    # Test cases for list of all car fleet
    # and then go back to car menu
    def setUp(self):
        self.maxDiff = None
        self.list_carmenu = '---------list of all cars ---------\n'
        self.options_list = '---------OPTIONS---------\nSearch for a specific car(1)\nGo back(2)'
        self.car_menu = '------Car menu------\nList of all cars in a car fleet\nList of unavailable cars(2)\nList of available cars(3)\nSearch for a specific car(4)\n'
        self.selected_option_second = '2'
        self.final_selection = '6'
        self.final_selection_main_menu = '5'


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_car_go_back(self,mock_stdout):
        with mock.patch('builtins.input', side_effect=[
            self.selected_option_second,
            self.final_selection,
            self.final_selection_main_menu
        ]):
            with self.assertRaises(SystemExit) as cm:
                 main.list_all_cars()
                 self.assertIn(self.list_carmenu, mock_stdout.getvalue())
                 self.assertIn(self.options_list, mock_stdout.getvalue())
                 self.assertIn(self.car_menu, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

            
            
class CarShowListSearch(unittest.TestCase):
    # Test case 21
    # Test case for list of all cars in a car fleet and successfully search one car
    # Car not finds and then go back to car menu
    # option 2 is for selecting going back on selecting specific car section
    def setUp(self):
        self.maxDiff = None
        self.selected_option = '1'
        self.NotFound_License = '1234ABC'
        self.Continue_message = 'License number 1234ABC does not exist.\nDo you want to try again?(Y/N)'
        self.YorN_option_N = 'N'
        self.availability_menu = '3'
        self.final_selection = '6'
        self.final_selection_main_menu = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_car_search(self, mock_stdout):
         with mock.patch('builtins.input', side_effect=[
            self.selected_option,
            self.NotFound_License,
            self.YorN_option_N,
            self.availability_menu,
            self.final_selection,
            self.final_selection_main_menu
         ]):

            with self.assertRaises(SystemExit) as cm:   
                main.list_all_cars()
                self.assertIn(self.Continue_message, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

        
class CarUnavailableSearch(unittest.TestCase):
    # Test case 22
    # Test case for list of unavailable cars and search for one
    # not found and go back
    def setUp(self):
            self.maxDiff = None
 #           self.list_unavailable_menu = '------list of all cars unavailable------'
            self.select_option_message = '--------OPTIONS--------\nSearch for a specific car(1)\nGo back(2)'
            self.select_option = '1'
            self.good_license = '1234AAA'
            self.notfinding_message = 'License number 1234AAA does not exist.\nDo you want to try again?'
            self.YorNo_option = 'N'
            self.final_selection = '6'
            self.final_selection_main_menu = '5'
     
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)  
    def test_car_UnavailableList_search(self, mock_stdout):
      # car search failed and go back to
      # car main menu
        with mock.patch('builtins.input', side_effect=[
            self.select_option,
            self.good_license,
            self.YorNo_option,
            self.final_selection,
            self.final_selection_main_menu
      ]):
            with self.assertRaises(SystemExit) as cm: 
                main.list_all_unavailable_cars()
                self.assertIn(self.select_option_message, mock_stdout.getvalue())
                self.assertIn(self.notfinding_message, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0) 
   
class CarUnavailableEmptyList(unittest.TestCase):
       # Test case 23
       # List of all unavailable cars
       # List is empty and return to car menu
    def setUp(self):
       self.maxDiff = None
       self.list_unavailable_empty_message = "\**** LIST IS EMPTY ! ****"
       self.select_option_message = '--------OPTIONS--------\nSearch for a specific car(1)\nGo back(2)'
       self.select_option= '2'
       self.final_selection = '6'
       self.final_selection_main_menu = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)  
    def test_car_unavailableList_empty(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=[
            self.select_option,
            self.final_selection,
            self.final_selection_main_menu
        ]):
             with self.assertRaises(SystemExit) as cm: 
                 main.list_all_unavailable_cars()
                 self.assertIn(self.unavailable_empty_message, mock_stdout.getvalue())
                 self.assertIn(self.select_option_message, mock_stdout.getvalue())
             self.assertEqual(cm.exception.code, 0)         
            
class CarAvailableList(unittest.TestCase):
    # Test case 24
    # List of all available cars and go back to car menu
    def setUp(self):
       self.maxDiff = None
       self.option_message = 'option\nSearch for a specific car(1)\nGo back(2)'
       self.select_option= '2' 
       self.final_selection = '6'
       self.final_selection_main_menu = '5'   
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_Car_available_list(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=[
            self.select_option,
            self.final_selection,
            self.final_selection_main_menu
        ]):
             with self.assertRaises(SystemExit) as cm:   
                 main.list_all_available_cars()
                 self.assertIn(self.option_message, mock_stdout.getvalue())
             self.assertEqual(cm.exception.code, 0)
        
class CarAvailableList(unittest.TestCase):
    # Test case 25
    # List of all available cars is empty and go back to main menu
    def setUp(self):
        self.maxDiff = None
        self.availableList_empty_message = '\n\LIST IS EMPTY'
        self.option_message = 'option\nSearch for a specific car(1)\nGo back(2)'
        self.select_option= '2'
        self.final_selection = '6'
        self.final_selection_main_menu = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_car_available_list_empty(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=[
            self.select_option,
            self.final_selection,
            self.final_selection_main_menu
        ]): 
            with self.assertRaises(SystemExit) as cm: 
                  main.list_all_available_cars()
                  self.assertIn(self.availableList_empty_message, mock_stdout.getvalue())
                  self.assertIn(self.option_message, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

class CarSearch(unittest.TestCase):
    # Test case 26
    # Test cases for searching a car with correct format and found
    def setUp(self):
        self.maxDiff = None
        self.good_license = '1234ABC'
        self.fining_license_message = '1234ABC found In System!'
        self.finfing_infromation_message = '\nName,Manufacturer,Year made,License number, Type of energy, category,Availavility'
        self.option_message = '\n---OPTIONS---\nAssign to the list of available cars(1))\nAssign to the list of unavailable cars(2)\nGo back(3)'
        self.select_option = '2'
        self.assign_success_message = '\nCar successfully moved from available to unavailable'
        self.final_selection = '6'
        self.final_selection_main_menu = '5'
              
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)      
    def test_search_car_success(self, mock_stdout):
        # car search and sign
        with mock.patch('builtins.input', side_effect=[
            self.good_license,
            self.select_option,
            self.final_selection,
            self.final_selection_main_menu
        ]):
            with self.assertRaises(SystemExit) as cm: 
                main.searchcar()
                self.assertIn(self.fining_license_message, mock_stdout.getvalue())
                self.assertIn(self.option_message, mock_stdout.getvalue())
                self.assertIn(self.assign_success_message, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)
            
class CarSearchmulti(unittest.TestCase):
    # Test case 27
    # Search for specific car, with all correct information (not found at first but then found)
    # move to unavailable and go back to menu with pressign g (not Y or N)
    def setUp(self):
        self.maxDiff = None
        self.bad_license = '1234BBB'                    
        self.notfining_license_message = '\n1234BBB not found in system\n ' 
        self.option_message =  'Do you want to try again?(Y/N)'
        self.select_optionmessage= 'Y'
        self.good_license = '1234MAT'
        self.fining_license_message = '\n1234ABC found in system\n '
        self.finfing_infromation_message = '\nName,Manufacturer,Year made,License number, Type of energy, category,Availavility'
        self.option_message_second = '\n---OPTIONS---\nAssign to the list of available cars(1)\nAssign to the list of unavailable cars\nGo back(3)'
        self.select_option = '1'
        self.assign_success_message = '\nCar successfully moved from unavailable to available'
        self.select_in_menu = '3'
        self.final_selection = '6'
        self.final_selection_main_menu = '5'
                  
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)      
    def test_search_car_success_assign(self, mock_stdout):
        # car search and sign
        with mock.patch('builtins.input', side_effect=[                 
               self.bad_license,
               self.select_optionmessage,
               self.good_license,
               self.select_option,
               self.select_in_menu,
               self.final_selection,
               self.final_selection_main_menu
        ]):
                with self.assertRaises(SystemExit) as cm: 
                     main.searchcar()
                     self.assertIn(self.notfining_license_message, mock_stdout.getvalue())
                     self.assertIn(self.option_message, mock_stdout.getvalue())       
                     self.assertIn(self.fining_license_message, mock_stdout.getvalue())
                     self.assertIn(self.finfing_infromation_message , mock_stdout.getvalue())       
                     self.assertIn(self.option_message_second , mock_stdout.getvalue())          
                     self.assertIn(self.assign_success_message , mock_stdout.getvalue())          
                self.assertEqual(cm.exception.code, 0)          
                      
class CarSearchwrong(unittest.TestCase):
    # Test case 28
    # Search for specific car with incorrect format
    # Then input a correct one and return to menu
    def setUp(self):
        self.maxDiff = None
        self.bad_license = 'AA123456'                    
        self.error_license_message = 'Invalid license number format, Try again\n' 
        self.good_license = '1234ABC'
        self.fining_license_message = '\n1234ABC found in system\n '
        self.finfing_infromation_message = '\nName,Manufacturer,Year made,License number, Type of energy, category,Availavility'
        self.option_message_second = '\n---OPTIONS---\nAssign to the list of available cars(1)\nAssign to the list of unavailable cars\nGo back(3)'
        self.select_option = '3'
        self.final_selection = '6'
        self.final_selection_main_menu = '5'
  
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_search_car_wrong_format(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=[   
          self.bad_license,
          self.good_license,
          self.select_option,
          self.final_selection,
          self.final_selection_main_menu
      ]):
            with self.assertRaises(SystemExit) as cm:
                main.searchcar()
                self.assertIn(self.error_license_message, mock_stdout.getvalue())
                self.assertIn(self.fining_license_message, mock_stdout.getvalue())
                self.assertIn(self.finfing_infromation_message, mock_stdout.getvalue())
                self.assertIn(self.option_message_second , mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)
                       
class AddingNewCar(unittest.TestCase):
    # Test case 29
    # Add a new car
    # fail all inputs at first and then input correct one
    def setUp(self):
        self.maxDiff = None        
        self.choose_option_carmenus = '5'
        self.bad_format_license = 'AAA1346'
        self.bad_format_license_message = 'License number is of incorrect format, try again\n'
        self.good_format_license = '1234ABC'
        self.bad_format_manufacture = '1A'
        self.bad_format_manufacture_message = 'Invalid format, try again!\n' 
        self.good_format_manufacture = 'Opel'
        self.bad_format_name = '2A'
        self.bad_format_name_message = 'Invalid format, try again!\n'  
        self.good_format_name = 'Astra'
        self.bad_format_year = '20222A'        
        self.bad_format_year_message = 'Invalid format, try again!\n'  
        self.good_format_year = '2021'
        self.bad_format_energy = 'petrolll'
        self.bad_format_energy_message = 'Invalid format, try again!\n'
        self.good_format_energy = 'petrol'
        self.bad_format_car_choose = 6
        self.bad_format_car_choose_message = 'Invalid format, try again!\n'
        self.good_format_car_choose= 4
        self.final_message = 'Astra- 2021- 1234ABC - petrol- SUV- availability= \nCar has been added!' 
                
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_license(self, mock_stdout):
        # license function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_license,
            self.good_format_license
        ]):
            result = main.get_license_plate()
            self.assertEqual(mock_stdout.getvalue(), self.bad_format_license_message)
            self.assertEqual(result, self.good_format_license)  
                               
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)                    
    def test_bad_format_manufacture(self, mock_stdout):
        # manufacture function
        with mock.patch('builtins.input', side_effect=[             
        self.bad_format_manufacture,
        self.good_format_manufacture
        ]):
            result = main.get_car_manu()
            self.assertEqual(mock_stdout.getvalue(), self.bad_format_manufacture_message)
            self.assertEqual(result, self.good_format_manufacture)
                                
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)              
    def test_bad_format_name(self, mock_stdout):
        # name function
        with mock.patch('builtins.input', side_effect=[                   
           self.bad_format_name,
           self.good_format_name
        
         ]):
            result = main.get_car_name()
            self.assertEqual(mock_stdout.getvalue(), self.bad_format_name_message)
            self.assertEqual(result, self.good_format_name)          

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)                     
    def test_bad_format_year(self, mock_stdout):
        # year function
        with mock.patch('builtins.input', side_effect=[
            self.bad_format_year,
            self.good_format_year
        ]):
            result = main.get_make_year()
            self.assertEqual(mock_stdout.getvalue(), self.bad_format_year_message)
            self.assertEqual(result, self.good_format_year)               
                   
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)                     
    def test_bad_format_energy(self, mock_stdout):
        # energy function
        with mock.patch('builtins.input', side_effect=[
         self.bad_format_energy,        
         self.good_format_energy          
      ]):
            result = main.get_car_type_energy()
            self.assertEqual(mock_stdout.getvalue(), self.bad_format_energy_message)
            self.assertEqual(result, self.good_format_energy)                 

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_format_car_addition(self, mock_stdout):
        # car addition function                
        with mock.patch('builtins.input', side_effect=[ 
           self.choose_option_carmenus,            
           self.bad_format_license,
           self.good_format_license,
           self.bad_format_manufacture,
           self.good_format_manufacture,
           self.bad_format_name, 
           self.good_format_name,
           self.bad_format_year,       
           self.good_format_year,
           self.bad_format_energy,
           self.good_format_energy,
           self.bad_format_car_choose,
           self.good_format_car_choose         
      ]):
            main.cars()   
            self.assertIn(self.bad_format_car_choose_message, mock_stdout.getvalue())       
            self.assertIn(self.final_message, mock_stdout.getvalue())       
                 
class AddingNewCar(unittest.TestCase):
    # Test case 30
    # Add a new car
    # all inputs are correct
    def setUp(self):
        self.maxDiff = None     
        self.choose_option_carmenu = '5'
        self.good_format_license_not_repeated = '8462ZOT'
        self.good_format_license = '1234PBC'
        self.good_format_manufacture = 'Opel'
        self.good_format_name = 'Astra' 
        self.good_format_year = '2021'
        self.good_format_energy = 'petrol'
        self.good_format_car_choose = '3'
        self.final_message = 'Car has been added!'
                       
    def test_format_license(self):
         # license function only good format            
         with mock.patch('builtins.input', side_effect=[
            self.good_format_license_not_repeated,
        ]):                     
            result = main.get_license_plate()
            self.assertEqual(result, self.good_format_license_not_repeated)           
                       
    def test_format_manufacture(self):
        # manufacture function
        with mock.patch('builtins.input', side_effect=[
            self.good_format_manufacture,
        ]):
            result = main.get_car_manu()
            self.assertEqual(result, self.good_format_manufacture)    
                       
    def test_format_name(self):
        # name function
        with mock.patch('builtins.input', side_effect=[
            self.good_format_name,
        ]):
            result = main.get_car_name()
            self.assertEqual(result, self.good_format_name)                    
        
    def test_format_year(self):
        # year function
        with mock.patch('builtins.input', side_effect=[
            self.good_format_year,
        ]):
            result = main.get_make_year()
            self.assertEqual(result, self.good_format_year) 
                       
    def test_format_energy(self):
          # type energy function
         with mock.patch('builtins.input', side_effect=[
            self.good_format_energy,
        ]):
            result = main.get_car_type_energy()
            self.assertEqual(result, self.good_format_energy)                  
              
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_format_cars_addition(self, mock_stdout):
        # Customer addition function
        with mock.patch('builtins.input', side_effect=[
           self.choose_option_carmenu,
           self.good_format_license,
           self.good_format_manufacture,
           self.good_format_name, 
           self.good_format_year,
           self.good_format_energy,
           self.good_format_car_choose
        ]):
            main.cars()
            self.assertIn(self.final_message, mock_stdout.getvalue())

class OrdersBackMenuCar(unittest.TestCase):
    # Test case 31
    # Test case for the option to go main menu from cars
    def setUp(self):
        self.maxDiff = None
        self.car_selection = '6'
        self.main_menu = '-------Main Menu-------\nOrders(1)\nCars(2)\nCustomers(3)\nRegister an Order(4)\nExit(5)\n'
        self.final_selection = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_car_to_main_menu(self, mock_stdout):
        # car menu option to main menu
        with mock.patch('builtins.input', side_effect=[
            self.car_selection,
            self.final_selection
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.cars()
                self.assertIn(self.main_menu, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

class Registeranorder(unittest.TestCase):
    # Test case 32
    #  Test case for register and order part (not found and back)
    def setUp(self):
        self.maxDiff = None
        self.main_message = ("-------Main Menu-------\nOrders(1)\nCars(2\nCustomers(3)\nRegister an Order(4)\nExit(5")
        self.register_selection = '4'
        self.good_orderid = '7539518-P'
        self.notfound_orderid_message = 'User does not exist, do you want to try again ? (y/n)'
        self.option_selection = 'N'
        self.final_selection = '5'
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_registerand_order(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=[
            self.register_selection,
            self.good_orderid,
            self.option_selection,
            self.final_selection
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.main_menu()
                self.assertIn(self.main_message, mock_stdout.getvalue())
                self.assertIn(self.notfound_orderid_message,mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

class Closewtheprogram(unittest.TestCase):
    # Test case 33
    #  Test case for closing the program
    def setUp(self):
        self.maxDiff = None
        self.main_message =  ("-------Main Menu-------\nOrders(1)\nCars(2\nCustomers(3)\nRegister an Order(4)\nExit(5")
        self.register_selection = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_close_program(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=[
            self.register_selection
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.main_menu()
                self.assertIn(self.main_message, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

class InvalidOptionMainmenu(unittest.TestCase):
    # Test case 34
    # Test case for input invalid number in the main menu
    def setUp(self):
        self.maxDiff = None
        self.main_message =  ("-------Main Menu-------\nOrders(1)\nCars(2\nCustomers(3)\nRegister an Order(4)\nExit(5")
        self.register_selection = '7'
        self.invalid_message = ("Invalid option. Please try again!")
        self.final_selection = '5'

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_number_mainmenu(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=[
            self.register_selection,
            self.final_selection
        ]):
            with self.assertRaises(SystemExit) as cm:
                main.main_menu()
                self.assertIn(self.main_message, mock_stdout.getvalue())
                self.assertIn(self.invalid_message, mock_stdout.getvalue())
            self.assertEqual(cm.exception.code, 0)

