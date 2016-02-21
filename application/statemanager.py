'''
Created on 21 lut 2016

@author: luk
'''

class StateManager(object):
    '''
    classdocs
    '''


    def __init__(self, initialState):
        '''
        Constructor
        '''
        self.state = initialState
    
    def read(self):
        return self.state
    
    def save(self, state):
        self.state = state