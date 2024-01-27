# tests/test_calculator.py

import unittest
from flask import Flask
from app import app

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_addition(self):
        response = self.app.post('/add', data=dict(num1='5', num2='3'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The result is: 8.0', response.data)

    def test_subtraction(self):
        response = self.app.post('/subtract', data=dict(num1='8', num2='3'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The result is: 5.0', response.data)

    def test_multiplication(self):
        response = self.app.post('/multiply', data=dict(num1='4', num2='2'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The result is: 8.0', response.data)

    def test_division(self):
        response = self.app.post('/divide', data=dict(num1='10', num2='2'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The result is: 5.0', response.data)

if __name__ == '__main__':
    unittest.main()
