import unittest
  
from tests/translator import englishToFrench, frenchToEnglish
class TestenglishToFrench(unittest.TestCase): 
        def test1(self): 
            self.assertEqual(englishToFrench(""), "") # test null
            self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test if Hello gives Bonjour.
            #self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.
            
class TestfrenchToEnglish(unittest.TestCase): 
        def test1(self): 
            self.assertEqual(frenchToEnglish(""), "") # test null.
            self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test if Bonjour gives Hello.
            #self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.
            
unittest.main()
