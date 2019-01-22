import unittest  # to test import unittest
import cap 

class TestCap(unittest.TestCase): # inherit unittest.TestCase
    
    def test_one_words(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python') # check for equlity using self.assertEqual
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
if __name__ == '__main__':
    unittest.main() #run testcases using unittest.main()
