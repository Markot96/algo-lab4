import unittest

from lab4.wchain import WChain


class WChainTest(unittest.TestCase):

    def test_chain(self):
        w = WChain()
        self.assertEqual(6, w.count_chains("wchain.in"))

    if __name__ == '__main__':
        unittest.main()
