'''
Created on 21 lut 2016

@author: luk
'''
from comparator.mathcomparators import MathDiffComparator, MathLenComparator
from comparator.textcomparators import TextComparator
from comparator.listcomparator import ListComparator

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
        if (params['comparator']['type'] == 'list') :
            return ListComparator()