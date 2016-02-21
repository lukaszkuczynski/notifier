'''
Created on 21 lut 2016

@author: luk
'''

class TextComparator():
    '''
    classdocs
    '''


    def compare(self, previous_state, current_state):        
        diff_value = "<text_diff>"
        changed = previous_state != current_state
        return {
            'changed' : changed,
            'value' : diff_value
        }