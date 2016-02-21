'''
Created on 21 lut 2016

@author: luk
'''

class MathDiffComparator():
    '''
    classdocs
    '''
    def compare(self, previous_state, current_state):
        
        diff_value = current_state - previous_state
        return {
            'changed' : True,
            'value' : diff_value
        }

class MathLenComparator():
    def compare(self, previous_state, current_state):
        
        diff_value = len(current_state) - len(previous_state)
        return {
            'changed' : True,
            'value' : diff_value
        }
