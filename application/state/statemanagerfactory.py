'''
Created on 21 lut 2016

@author: luk
'''
from state.statemanager import StatefulManager
from state.filestatemanager import FileStateManager

class StateManagerFactory(object):
    '''
    classdocs
    '''


    def get(self, params):    
            if (params['stateManager']['type'] == 'stateful') :
                return StatefulManager(initialState="")
            if (params['stateManager']['type'] == 'file') :
                return FileStateManager(params)            