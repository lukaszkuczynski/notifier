'''
Created on 21 lut 2016

@author: luk
'''
from state.statemanager import StatefulManager
from state.filestatemanager import FileStateManager
from state.raw_state_manager import RawStateManager

class StateManagerFactory(object):
    '''
    classdocs
    '''


    def get(self, params):    
            if (params['stateManager']['type'] == 'stateful') :
                return StatefulManager(initialState="")
            if (params['stateManager']['type'] == 'file') :
                return FileStateManager(params)
            if (params['stateManager']['type'] == 'raw') :
                return RawStateManager(params)