'''
Created on 21 lut 2016

@author: luk
'''
from application.comparator.mathcomparators import MathDiffComparator, MathLenComparator
from application.comparator.textcomparators import TextComparator

class ComparatorFactory(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def get(self, params):    
        if (params['comparator']['type'] == 'math.difference') :
            return MathDiffComparator()
        if (params['comparator']['type'] == 'text') :
            return TextComparator()        