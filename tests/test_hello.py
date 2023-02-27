import unittest
from hello import say_hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        ##assert say_hello("Alice") == "Hello, Alice!"
        assert say_hello("thrinad") == "Hello, Bob!"

if __name__ == '__main__':
    unittest.main()