'''
Created on 21 lut 2016

@author: luk
'''
from application.notifier.debugnotifier import DebugNotifier

class NotifierFactory(object):
    '''
    classdocs
    '''


    def get(self, params):    
        if (params['notifier']['type'] == 'debug') :
            return DebugNotifier()