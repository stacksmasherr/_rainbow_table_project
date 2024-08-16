import unittest
from rainbow_table import RainbowTable
import hashlib

class TestRainbowTable(unittest.TestCase):
    def test_hash_function(self):
        rt = RainbowTable()
        self.assertEqual(rt.hash('password'), hashlib.md5('password'.encode('utf-8')).hexdigest())

    def test_chain_creation(self):
        rt = RainbowTable()
        chain_end = rt.create_chain('password')
        self.assertEqual(len(chain_end), 6)

    def test_lookup(self):
        rt = RainbowTable()
        rt.generate_table(['password', '123456'])
        hash_value = rt.hash('password')
        self.assertEqual(rt.lookup(hash_value), 'password')

if __name__ == '__main__':
    unittest.main()
