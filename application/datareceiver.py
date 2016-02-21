'''
Created on 21 lut 2016

@author: luk
'''

class DataReceiver(object):
    '''
    classdocs
    '''


    def __init__(self, params=None):
        '''
        Constructor
        '''
        self.n = 1
        
    def receive(self):
        self.n += 1
        return self.n