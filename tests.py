import unittest

import git_mnemonic as gm

class GitMnemonic(unittest.TestCase):
    def test_encode(self):
        self.assertTrue(gm.encode("master"))

    def test_decode(self):
        self.assertTrue(gm.decode("any bear club"))

    def test_invertible(self):
        once = gm.encode("master")
        self.assertEquals(gm.encode(gm.decode(once)), once)

