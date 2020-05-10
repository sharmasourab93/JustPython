"""
Test isolation is important
Test driven development
"""
import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # print('SetupClass')
        pass
        
    @classmethod
    def tearDownClass(cls) -> None:
        # print('tearDownClass')
        pass
    
    def setUp(self):
        # print("setUp")
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', "Smith", 60000)
    
    def tearDown(self):
        #print('tearDown')
        pass
    
    def test_email(self):
        # print("test_email")
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')
        
    def test_fullname(self):
        # print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')
    
    def test_apply_raise(self):
        # print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
    
    def test_monthly_schedule(self):
        with patch('requests.get') as mocked_get:
            mocked_get.return_val.ok = True
            mocked_get.return_val.text = "Success"
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get('http://company.com/Schafer/May')
            mocked_get.copy()
            print(schedule, mocked_get)
            self.assertNotEqual(schedule, 'Success')

            mocked_get.return_val.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Success')


if __name__ == '__main__':
    unittest.main()
