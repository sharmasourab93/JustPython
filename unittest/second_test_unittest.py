import unittest


class TestStringMethods(unittest.TestCase):
    
    def setUp(self) -> None:
        pass
    
    def test_strings_a(self):
        self.assertEqual('a'*4, 'aaaa')
        
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_strip(self):
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks')
        
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
            
            
if __name__ == '__main__':
    unittest.main()
    
    