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
            d = os.path.dirname(self.filename)
            if len(d) > 0 :
                if not os.path.exists(d):
                    os.makedirs(d)
            open(self.filename, 'w+')            
        f = open(self.filename, 'r')
        raw = f.read()
        return str(raw)
    
    def save(self, state):  
        f = open(self.filename, 'w+')
        statestr = str(state)
        f.write(statestr)
        
        