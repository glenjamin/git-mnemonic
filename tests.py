#!/usr/bin/env python

import unittest

import git_mnemonic as gm

class GitMnemonicTests(unittest.TestCase):
    def test_encode(self):
        self.assertTrue(gm.encode("master"))

    def test_decode(self):
        self.assertTrue(gm.decode("end line grab ding line pot end bear"))

    def test_invertible(self):
        once = gm.encode("master")
        self.assertEquals(gm.encode(gm.decode(once)), once)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GitMnemonicTests)
    unittest.TextTestRunner(verbosity=2).run(suite)