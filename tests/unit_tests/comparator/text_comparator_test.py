'''
Created on 21 lut 2016

@author: luk
'''
import unittest
from application.comparator.textcomparators import TextComparator


class TextComparatorTest(unittest.TestCase):

#     sut = TextComparator()

    def test_comparator_givenTheSameContent_returnsNOTChanged(self):
        sut = TextComparator()
        diff = sut.compare("aa", "aa")
        assert(diff['changed'] == False)

    def test_comparator_givenDifferentContent_returnsChanged(self):
        sut = TextComparator()
        diff = sut.compare("aa", "ab")
        assert(diff['changed'] == True)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()