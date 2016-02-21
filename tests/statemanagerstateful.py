'''
Created on 21 lut 2016

@author: luk
'''
import unittest
from application.state.statemanager import StatefulManager


class Test(unittest.TestCase):


    def test_hasInitial_afterInit(self):
        sut = StatefulManager('aa')
        assert sut.read() == 'aa'

    def test_afterUpdate_doesntChangeOriginal(self):
        saved = 'aa'
        sut = StatefulManager(saved)
        current = 'bb'
        sut.save(current)
        assert saved != current

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()