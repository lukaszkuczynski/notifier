'''
Created on 21 lut 2016

@author: luk
'''

import os

class FileStateManager():
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.filename = params['stateManager']['filename']
    
    def read(self):
        if not os.path.isfile(self.filename) :
            open(self.filename, 'w+')            
        f = open(self.filename, 'rb')        
        return f.read()
    
    def save(self, state):  
        f = open(self.filename, 'wb+')
        f.write(state)
        
        