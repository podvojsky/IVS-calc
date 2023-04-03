#!/usr/bin/env python3
import unittest
import pytest
import math_lib

class TestMathLib(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(math_lib.add(4,3), 7)
        self.assertEqual(math_lib.add(-2,2), 0)
        self.assertEqual(math_lib.add(3,-4), -1)
        self.assertEqual(math_lib.add(-2,-7), -9)
        self.assertEqual(math_lib.add(0,0), 0)
        self.assertEqual(math_lib.add(1.2, 3.7), 4.9)
        self.assertEqual(math_lib.add(2, 1.97), 3.97)
        self.assertEqual(math_lib.add(1.53, 4), 5.53)
        self.assertEqual(math_lib.add(-1.5, 1.1), -0.4)
        self.assertEqual(math_lib.add(2.5, -15.25), -12.75)
        self.assertEqual(math_lib.add(5, -2.5), 2.5)
        self.assertEqual(math_lib.add(-3.255, 1), -2.255)
        self.assertEqual(math_lib.add(-10.525, -2.5), -13.025)
        self.assertEqual(math_lib.add(-3.255, -1), -4.255)
        self.assertEqual(math_lib.add(-5, -1.25), -6.25)
        self.assertEqual(math_lib.add(10.951475986427845368741, 14.541796248961426486), 25.4932722354)
    
    def test_sub(self):
        self.assertEqual(math_lib.sub(4,3), 1)
        self.assertEqual(math_lib.sub(-2,2), -4)
        self.assertEqual(math_lib.sub(2,-2), 4)
        self.assertEqual(math_lib.sub(-2,-7), 5)
        self.assertEqual(math_lib.sub(0,0), 0)
        self.assertEqual(math_lib.sub(1.2, 3.7), -2.5)
        self.assertEqual(math_lib.sub(2, 1.97), 0.03)
        self.assertEqual(math_lib.sub(1.53, 4), -2.47)
        self.assertEqual(math_lib.sub(-1.5, 1.1), -2.6)
        self.assertEqual(math_lib.sub(2.5, -15.25), 17.75)
        self.assertEqual(math_lib.sub(5, -2.5), 7.5)
        self.assertEqual(math_lib.sub(-3.255, 1), -4.255)
        self.assertEqual(math_lib.sub(-10.525, -2.5), -8.025)
        self.assertEqual(math_lib.sub(-3.255, -1), -2.255)
        self.assertEqual(math_lib.sub(-5, -1.25), -3.75)
        self.assertEqual(math_lib.sub(10.951475986427845368741, 14.541796248961426486), -3.5903202625)
        
if __name__ == '_main_':
    unittest.main()