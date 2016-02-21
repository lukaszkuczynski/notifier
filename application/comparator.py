'''
Created on 21 lut 2016

@author: luk
'''

class Comparator(object):
    '''
    classdocs
    '''


    def __init__(self, params=None):
        '''
        Constructor
        '''
        
    def compare(self, previous_state, current_state):
        
        diff_value = current_state - previous_state
        return {
            'changed' : True,
            'value' : diff_value
        }