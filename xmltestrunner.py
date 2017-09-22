#!/usr/bin/env python

import random
import unittest
import xmlrunner

rnd = random.Random()

class SomeTestsClass(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    def test_should_fail_one_in_eight(self):
        if rnd.uniform(0,1.0) < 0.125:
            test_failed = True
        else:
            test_failed = False

    def test_should_always_pass(self):
        self.assertTrue(True)

    def test_should_fail_half_the_time(self):
        self.assertFalse(rnd.choice([True,False]))


class SomeOtherClass(unittest.TestCase):
    def test_this_should_also_pass(self):
        self.assertEqual(0,0)

    def test_this_should_pass(self):
        self.assertEqual(True, True)

    def test_this_ones_pass_too(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
