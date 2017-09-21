#!/usr/bin/env python

import random
import unittest
import xmlrunner



class SomeTestsClass(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    def test_should_pass(self):
        self.assertTrue(True)

    def test_should_fail(self):
        self.assertFalse(True)

class SomeOtherClass(unittest.TestCase):
    def test_this_should_also_pass(self):
        self.assertEqual(0,0)

    def test_this_should_also_fail(self):
        self.assertEqual("pigs","fly")

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
