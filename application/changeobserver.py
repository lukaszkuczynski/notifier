'''
Created on 21 lut 2016

@author: luk
'''

from datareceiver import DataReceiver
from statemanager import StateManager
from comparator import Comparator
from notifier import Notifier

class ChangeObserver(object):
    '''
    classdocs
    '''
    


    def __init__(self, params=None):
        '''
        Constructor
        '''
        self.dataReceiver = DataReceiver()
        self.stateManager = StateManager(initialState=0)
        self.comparator = Comparator()
        self.notifier = Notifier()         
        
    def notify_if_changed(self) :
        current_state = self.dataReceiver.receive()
        saved_state = self.stateManager.read()
        diff = self.comparator.compare(previous_state=saved_state, current_state=current_state)
        if (diff['changed']) :
            self.notifier.notify(diff)
            
            


if __name__ == '__main__' :
    observer = ChangeObserver()
    observer.notify_if_changed()
    