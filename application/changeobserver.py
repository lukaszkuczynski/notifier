'''
Created on 21 lut 2016

@author: luk
'''

from comparator.comparatorfactory import ComparatorFactory
from application.input.inputfactory import InputFactory
from application.notifier.notifierfactory import NotifierFactory
from application.state.statemanagerfactory import StateManagerFactory
import time

class ChangeObserver(object):
    '''
    Defines rule of observing changes. After receiving data and comparing with previous state notifies about change
    '''
    


    def __init__(self, params=None):
        '''
        Constructor
        '''
        self.dataReceiver = InputFactory().get(params)
        self.stateManager = StateManagerFactory().get(params)
        self.comparator = ComparatorFactory().get(params)
        self.notifier = NotifierFactory().get(params)         
        
    def notify_if_changed(self) :
        current_state = self.dataReceiver.receive()
        saved_state = self.stateManager.read()
        print('saved ',saved_state,'current',current_state)
        diff = self.comparator.compare(previous_state=saved_state, current_state=current_state)
        self.stateManager.save(current_state)
        if (diff['changed']) :
            self.notifier.notify(diff)
            return diff
            


if __name__ == '__main__' :
    params = {
        'input' : {
            'type' : 'url.content',
            'url' :'http://www.timeapi.org/pdt/this+friday+at+noon'
        },
        'stateManager' : {
            'type' : 'stateful',
        },
        'comparator' : {
            'type' : 'text'
        },
        'notifier' : {
            'type' : 'debug'
        }                        
    }
    observer = ChangeObserver(params)
    
    for i in range(1,20) :   
        print('checking')     
        observer.notify_if_changed()
        time.sleep(1)
        
    