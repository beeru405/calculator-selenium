# tests/test_calculator.py

from selenium import webdriver
import unittest

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")

    def test_addition(self):
        num1_input = self.driver.find_element_by_id("num1")
        num2_input = self.driver.find_element_by_id("num2")
        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")

        num1_input.send_keys("5")
        num2_input.send_keys("3")
        submit_button.click()

        result_element = self.driver.find_element_by_xpath("//p[contains(text(), 'The result is:')]")
        result = result_element.text.split(":")[1].strip()

        self.assertEqual(result, "8")

    # Add similar test methods for subtraction, multiplication, and division

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

