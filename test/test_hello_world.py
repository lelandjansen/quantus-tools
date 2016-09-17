import unittest
from src.lib.hello_world import hello

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello(), "Hello World!")
