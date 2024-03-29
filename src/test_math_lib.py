#!/usr/bin/env python3

##
# @file test_math_lib.py
#
# @brief This module tests basic mathematical functions.
#
# @section author_doxygen_example Author(s)
# - Created by Michal Uhrecký on 04/18/2023.
#
# Copyright (c) 2023 xpodvo00-ivs-team. All rights reserved.

import unittest
import math_lib

class TestMathLib(unittest.TestCase):
    """! TestMathLib class.
    """
    
    def test_add(self):
        """! @brief Method test_add for testing math_lib.add.
        """
        self.assertEqual(math_lib.add(4,3), 7)
        self.assertEqual(math_lib.add(-2,2), 0)
        self.assertEqual(math_lib.add(3,-4), -1)
        self.assertEqual(math_lib.add(-2,-7), -9)
        self.assertEqual(math_lib.add(0,0), 0)
        self.assertEqual(math_lib.add(2,0), 2)
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
        """! @brief Method test_sub for testing math_lib.sub.
        """
        self.assertEqual(math_lib.sub(4,3), 1)
        self.assertEqual(math_lib.sub(-2,2), -4)
        self.assertEqual(math_lib.sub(2,-2), 4)
        self.assertEqual(math_lib.sub(-2,-7), 5)
        self.assertEqual(math_lib.sub(0,0), 0)
        self.assertEqual(math_lib.sub(2,0), 2)
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

    def test_mul(self):
        """! @brief Method test_mul for testing math_lib.mul.
        """
        self.assertEqual(math_lib.mul(4,3), 12)
        self.assertEqual(math_lib.mul(-2,2), -4)
        self.assertEqual(math_lib.mul(2,-2), -4)
        self.assertEqual(math_lib.mul(-2,-7), 14)
        self.assertEqual(math_lib.mul(0,0), 0)
        self.assertEqual(math_lib.mul(2,0), 0)
        self.assertEqual(math_lib.mul(1.2, 3.7), 4.44)
        self.assertEqual(math_lib.mul(2, 1.97), 3.94)
        self.assertEqual(math_lib.mul(1.53, 4), 6.12)
        self.assertEqual(math_lib.mul(-1.5, 1.1), -1.65)
        self.assertEqual(math_lib.mul(2.5, -15.25), -38.125)
        self.assertEqual(math_lib.mul(5, -2.5), -12.5)
        self.assertEqual(math_lib.mul(-3.255, 1), -3.255)
        self.assertEqual(math_lib.mul(6, -1), -6)
        self.assertEqual(math_lib.mul(-10.525, -2.5), 26.3125)
        self.assertEqual(math_lib.mul(-3.255, -1), 3.255)
        self.assertEqual(math_lib.mul(-5, -1.25), 6.25)
        self.assertEqual(math_lib.mul(10.951475986427845368741, 14.541796248961426486), 159.2541324200)

    def test_div(self):
        """! @brief Method test_div for testing math_lib.div.
        """
        self.assertEqual(math_lib.div(6,2), 3)
        self.assertEqual(math_lib.div(-2,2), -1)
        self.assertEqual(math_lib.div(2,-2), -1)
        self.assertEqual(math_lib.div(-7,-2), 3.5)
        self.assertEqual(math_lib.div(0,5), 0)
        self.assertEqual(math_lib.div(2.5, 1.25), 2)
        self.assertEqual(math_lib.div(4, 2.5), 1.6)
        self.assertEqual(math_lib.div(2.5, 2), 1.25)
        self.assertEqual(math_lib.div(-2.5, 1.25), -2)
        self.assertEqual(math_lib.div(2.5, -1.25), -2)
        self.assertEqual(math_lib.div(15, -2.5), -6)
        self.assertEqual(math_lib.div(-8.25, 4), -2.0625)
        self.assertEqual(math_lib.div(6, -1), -6)
        self.assertEqual(math_lib.div(-2.4, -7.5), 0.32)
        self.assertEqual(math_lib.div(-3.255, -1), 3.255)
        self.assertEqual(math_lib.div(10.951475986427845368741, 14.541796248961426486), 0.7531033855)

        self.assertRaises(ZeroDivisionError, math_lib.div, 10, 0)

    def test_fac(self):
        """! @brief Method test_fac for testing math_lib.fac.
        """
        self.assertEqual(math_lib.fac(6), 720)
        self.assertEqual(math_lib.fac(13), 6227020800)
        self.assertEqual(math_lib.fac(1), 1) 
        self.assertEqual(math_lib.fac(2), 2)
        self.assertEqual(math_lib.fac(3), 6)
        self.assertEqual(math_lib.fac(0), 1)

        self.assertRaises(ValueError, math_lib.fac, -4)
        self.assertRaises(ValueError, math_lib.fac, 171)
        self.assertRaises(ValueError, math_lib.fac, 1025)   

    def test_pow(self):
        """! @brief Method test_pow for testing math_lib.pow.
        """
        self.assertEqual(math_lib.pow(6,2), 36)
        self.assertEqual(math_lib.pow(-2,3), -8)
        self.assertEqual(math_lib.pow(2,-3), 0.125)
        self.assertEqual(math_lib.pow(-4,-2), 0.0625)
        self.assertEqual(math_lib.pow(0,5), 0)
        self.assertEqual(math_lib.pow(0,0), 1)
        self.assertEqual(math_lib.pow(5,0), 1)
        self.assertEqual(math_lib.pow(-5,0), 1)
        self.assertEqual(math_lib.pow(4.278,0), 1)
        self.assertEqual(math_lib.pow(10.5, 5.5), 413562.4932360662)
        self.assertEqual(math_lib.pow(4, 2.5), 32)
        self.assertEqual(math_lib.pow(2.5, 2), 6.25)
        self.assertEqual(math_lib.pow(2.5, -1.25), 0.3181082915)
        self.assertEqual(math_lib.pow(8, -2.5), 0.0055242717)
        self.assertEqual(math_lib.pow(-8.25, 3), -561.515625)
        self.assertEqual(math_lib.pow(1, 6), 1)
        self.assertEqual(math_lib.pow(1, -6), 1)

        self.assertRaises(ValueError, math_lib.pow, -2.5, 1.25)
        self.assertRaises(ValueError, math_lib.pow, -2.4, -7.5)

    def test_sqrt(self):
        """! @brief Method test_sqrt for testing math_lib.sqrt.
        """
        self.assertEqual(math_lib.sqrt(3,8), 2)
        self.assertEqual(math_lib.sqrt(-3,8), 0.5)
        self.assertEqual(math_lib.sqrt(3,-8), -2)
        self.assertEqual(math_lib.sqrt(5, 0), 0)
        self.assertEqual(math_lib.sqrt(0, 0), 0)
        self.assertEqual(math_lib.sqrt(10.5, 5.5), 1.1762800527)
        self.assertEqual(math_lib.sqrt(4, 2.5), 1.2574334297)
        self.assertEqual(math_lib.sqrt(2.5, 2), 1.3195079108)
        self.assertEqual(math_lib.sqrt(-8.25, 3), 0.8753205421)
        self.assertEqual(math_lib.sqrt(1, -6), -6)
        self.assertEqual(math_lib.sqrt(1, 6), 6)

        self.assertRaises(ZeroDivisionError, math_lib.sqrt, 0, 5)
        self.assertRaises(ValueError, math_lib.sqrt, -5, 0)
        self.assertRaises(ValueError, math_lib.sqrt, -8, -3)
        self.assertRaises(ValueError, math_lib.sqrt, 2, -16)
        self.assertRaises(ValueError, math_lib.sqrt, 2.5, -1.25)
        self.assertRaises(ValueError, math_lib.sqrt, 8, -2.5)
    
    def test_log(self):
        """! @brief Method test_log for testing math_lib.log.
        """
        self.assertEqual(math_lib.log(100,10), 2)
        self.assertEqual(math_lib.log(10,2), 3.3219280949)
        self.assertEqual(math_lib.log(2.5,2.5), 1)
        self.assertEqual(math_lib.log(13.25, 1.25), 11.5799786156)
        self.assertEqual(math_lib.log(5, 8.42), 0.7553883827)
        self.assertEqual(math_lib.log(7.52, 20), 0.6734801223)

        self.assertRaises(ValueError, math_lib.log, -5, 10)
        self.assertRaises(ValueError, math_lib.log, 10, -2)
        self.assertRaises(ValueError, math_lib.log, -10, -20)
        self.assertRaises(ValueError, math_lib.log, 0, 1)
        self.assertRaises(ValueError, math_lib.log, 1, 0)
        self.assertRaises(ValueError, math_lib.log, -5.25, 10)
        self.assertRaises(ValueError, math_lib.log, 2, -5.78)
        self.assertRaises(ValueError, math_lib.log, -5.97, -8.46)
        self.assertRaises(ValueError, math_lib.log, 0, 0)

    def test_change_sign(self):
        """! @brief Method test_change_sign for testing math_lib.change_sign.
        """
        self.assertEqual(math_lib.change_sign(100), -100)
        self.assertEqual(math_lib.change_sign(-100), 100)
        self.assertEqual(math_lib.change_sign(5.27), -5.27)
        self.assertEqual(math_lib.change_sign(-5.27), 5.27)
        self.assertEqual(math_lib.change_sign(-10.48941025679), 10.4894102568)
        self.assertEqual(math_lib.change_sign(0), 0)
    
if __name__ == '_main_':
    unittest.main()