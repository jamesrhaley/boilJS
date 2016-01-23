import unittest
from InputMap import InputMap
# python -m unittest test.testInputMap

class TestInputMap(unittest.TestCase):

    def setUp(self):
        self.boil = InputMap()

    def test_catch_phrase(self):
        self.boil.catch_phrase("new_name",
                  "what should the project be called now: ")
        self.assertEqual(self.boil.get_inputs('new_name'),'test-name')

    def test_catch_phrase_wrong(self):
        self.boil.catch_phrase("new_name",
                  "what should the project be called now: ")
        self.assertFalse(self.boil.get_inputs('new_name'),'1')

if __name__ == '__main__':
    unittest.main()