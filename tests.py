#!/usr/bin/env python

import unittest

import git_mnemonic as gm

class GitMnemonicTests(unittest.TestCase):
    def test_encode(self):
        self.assertTrue(gm.encode("master"))

    def test_decode(self):
        self.assertTrue(gm.decode("bis alo ama aha"))

    def test_invertible(self):
        once = gm.encode("master")
        self.assertEquals(gm.encode(gm.decode(once)), once)

if __name__ == '__main__':
    unittest.main(verbosity=2)