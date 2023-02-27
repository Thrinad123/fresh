
from hello import say_hello
##class TestHello(unittest.TestCase):
    def test_say_hello():
        assert say_hello("Alice") == "Hello, Alice!"
        assert say_hello("bob") == "Hello, Bob!"
        print("above function is working fine ")

if __name__ == '__main__':
        test_say_hello()