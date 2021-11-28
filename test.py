test.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from app import process_input

class TestApp(unittest.TestCase):
  #Test the functionality of car rental app

  def setUp(self):
      #This runs before the test cases are executed
      
      # self variables 
      # change this for our own variables
      self.a = 10
      self.b = 5
  def test_0010_add(self):
      # Test any kind of operation from the app
      result = process_input(self.a, self.b, "add")
      self.assertEqual(result, 15)

def suite():
  # Test suite
  # See https://docs.python.org/3/library/unittest.html to understand what it is
  suite = unittest.TestSuite()
  suite.addTests(
      unittest.TestLoader().loadTestsFromTestCase(TestApp)
  )
  return suite

if __name__ == '__main__':
  unittest.TextTestRunner(verbosity=2).run(suite())