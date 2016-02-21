'''
Created on 21 lut 2016

@author: luk
'''
from application.state.statemanager import StatefulManager

class StateManagerFactory(object):
    '''
    classdocs
    '''


    def get(self, params):    
            if (params['stateManager']['type'] == 'stateful') :
                return StatefulManager(initialState="")