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
#         changed = str(previous_state) != str(current_state)
        changed = previous_state != current_state
        return {
            'changed' : changed,
            'value' : diff_value,
            'previous_state' : previous_state,
            "current_state" : current_state 
        }